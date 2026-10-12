#!/usr/bin/env python3
"""Validate data: schema, CSV sync, topic names vs official topic-weight tables, numeric spot-checks of formulas, URL checks.
Usage: python scripts/validate.py [--no-net] [--strict]"""
import csv, json, sys, math, pathlib, urllib.request, urllib.error, concurrent.futures as cf
root = pathlib.Path(__file__).resolve().parent.parent
try: import jsonschema
except ImportError: sys.exit("pip install jsonschema")
data = json.load(open(root/"data/formulas.json")); W = json.load(open(root/"data/topic_weights.json"))["entries"]
fail = False
for e in jsonschema.Draft202012Validator(json.load(open(root/"schema/formulas.schema.json"))).iter_errors(data): print("SCHEMA:", list(e.path), e.message); fail = True
E = data["entries"]; ids = [x["id"] for x in E]
if len(set(ids)) != len(ids): print("DUPLICATE ids"); fail = True
if [r["id"] for r in csv.DictReader(open(root/"data/formulas.csv"))] != ids: print("CSV out of sync"); fail = True
official = {(w["exam"], w["topic"]) for w in W}
for x in E:
    if (x["exam"], x["topic"]) not in official: print("TOPIC not in official table:", x["id"], x["topic"]); fail = True
# --- numeric spot-checks (independent computations) ---
N = lambda z: 0.5*(1+math.erf(z/math.sqrt(2)))
checks = {}
r, n, A = 0.05, 10, 100.0
checks["annuity PV"] = abs(A*(1-(1+r)**-n)/r - sum(A/(1+r)**t for t in range(1,n+1))) < 1e-9
checks["EAR"] = abs((1+0.12/12)**12-1 - 0.126825) < 1e-6
def price(y, c=5, fv=100, T=10): return sum(c/(1+y)**t for t in range(1,T+1)) + fv/(1+y)**T
y = 0.06; P = price(y); mac = (sum(t*5/(1+y)**t for t in range(1,11)) + 10*100/(1+y)**10)/P
num_mod = -(price(y+1e-6)-price(y-1e-6))/(2e-6)/P
checks["modified duration = MacDur/(1+r)"] = abs(mac/(1+y) - num_mod) < 1e-5
S, X, rr, T, s = 100, 95, 0.03, 0.5, 0.25
d1 = (math.log(S/X)+(rr+s*s/2)*T)/(s*math.sqrt(T)); d2 = d1 - s*math.sqrt(T)
c = S*N(d1) - math.exp(-rr*T)*X*N(d2); p = math.exp(-rr*T)*X*N(-d2) - S*N(-d1)
checks["BSM satisfies put-call parity"] = abs(S + p - c - X*math.exp(-rr*T)) < 1e-9
dc = (lambda S2: S2*N((math.log(S2/X)+(rr+s*s/2)*T)/(s*math.sqrt(T))) - math.exp(-rr*T)*X*N((math.log(S2/X)+(rr-s*s/2)*T)/(s*math.sqrt(T))))
checks["BSM call delta = N(d1)"] = abs((dc(S+1e-4)-dc(S-1e-4))/2e-4 - N(d1)) < 1e-6
u, d, rf = 1.2, 0.8, 0.05; pi = (1+rf-d)/(u-d)
checks["risk-neutral prob prices the stock"] = abs((pi*u*100+(1-pi)*d*100)/(1+rf) - 100) < 1e-9
s1, s2 = (1.03)**1, (1.035)**2; f12 = s2/s1 - 1
checks["forward from spots"] = abs((1.03)*(1+f12) - 1.035**2) < 1e-12
D1, rq, g = 2.0, 0.09, 0.04
checks["Gordon = PV of growing dividends"] = abs(D1/(rq-g) - sum(D1*(1+g)**(t-1)/(1+rq)**t for t in range(1,5000))) < 1e-6
dfs = [1/1.02, 1/1.025**2, 1/1.03**3]; sw = (1-dfs[-1])/sum(dfs)
checks["swap rate prices a par bond"] = abs(sum(sw*df for df in dfs) + dfs[-1] - 1) < 1e-12
w1, a, b = 0.6, 0.2, 0.3
checks["two-asset variance (rho=1) = (w1 s1 + w2 s2)^2"] = abs(w1**2*a**2+(1-w1)**2*b**2+2*w1*(1-w1)*a*b - (w1*a+(1-w1)*b)**2) < 1e-12
om, al, be = 0.000002, 0.08, 0.9; v = om/(1-al-be)
checks["GARCH long-run variance is fixed point"] = abs(om + al*v + be*v - v) < 1e-15
from statistics import NormalDist
z = NormalDist().inv_cdf(0.975); es = NormalDist().pdf(z)/0.025
mc = sorted(NormalDist().samples(400000, seed=1)); tail = mc[:int(0.025*len(mc))]
checks["normal ES formula ~ Monte Carlo"] = abs(-sum(tail)/len(tail) - es) < 0.02
for k, ok in checks.items():
    print(("OK  " if ok else "FAIL"), "check:", k); fail |= not ok
print(f"{len(E)} formulas ({', '.join(f'{x}: {sum(e['exam']==x for e in E)}' for x in sorted({e['exam'] for e in E}))}); {len(W)} weight rows")
if "--no-net" not in sys.argv:
    urls = sorted({x["topic_source_url"] for x in E} | {x["uniprep2go_url"] for x in E if x["uniprep2go_url"]} | {w["source_url"] for w in W})
    def chk(u):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent":"Mozilla/5.0 (cfa-frm-formula-sheets validator)"}), timeout=25) as r: return u, r.status
        except urllib.error.HTTPError as e: return u, e.code
        except Exception as e: return u, type(e).__name__
    with cf.ThreadPoolExecutor(8) as ex:
        for u, st in ex.map(chk, urls):
            tag = "OK  " if st == 200 else ("FAIL" if "--strict" in sys.argv or st in (404, 410) else "WARN")
            fail |= tag == "FAIL"; print(tag, st, u)
print("RESULT:", "FAIL" if fail else "PASS"); sys.exit(1 if fail else 0)
