"""Source of truth for data/formulas.json and data/topic_weights.json.
Formulas are standard finance/quant math, each numerically spot-checked in scripts/validate.py where testable.
Topic areas use the official names published by CFA Institute and GARP (see data/topic_weights.json for sources).
Run: python scripts/build_data.py"""
import json, csv, pathlib
D = "2026-10-12"
root = pathlib.Path(__file__).resolve().parent.parent
CFA1 = "https://www.cfainstitute.org/programs/cfa-program/candidate-resources/level-i-exam"
CFA2 = "https://www.cfainstitute.org/programs/cfa-program/candidate-resources/level-ii-exam"
GARP = "https://www.garp.org/frm"
GARP_W = "https://www.garp.org/hubfs/Website/FRM/PDF/Study%20Materials/2023/FRM2023-Learning-Objectives.pdf"
U = "https://uniprep2go.study/"
LINK = {"CFA Level I": U+"decks/cfa-level-1-formula-reference-2026", "CFA Level II": U+"decks/cfa-level-2-formula-reference-2026", "FRM Part I": U+"decks/frm-part-1-anki-deck"}
SRC = {"CFA Level I": CFA1, "CFA Level II": CFA2, "FRM Part I": GARP}

# ---- official topic weights (read from official pages on D) ----
W = []
def w(exam, session, topic, lo, hi, src, note=None):
    W.append({"exam": exam, "session": session, "topic": topic, "weight_min_pct": lo, "weight_max_pct": hi, "source_url": src, "source_checked": D, "notes": note})
for t, lo, hi in [("Ethical and Professional Standards",15,20),("Quantitative Methods",6,9),("Economics",6,9),("Financial Statement Analysis",11,14),("Corporate Issuers",6,9),("Equity Investments",11,14),("Fixed Income",11,14),("Derivatives",5,8),("Alternative Investments",7,10),("Portfolio Management",8,12)]:
    w("CFA Level I","2026",t,lo,hi,CFA1)
for t, lo, hi in [("Ethical and Professional Standards",10,15),("Quantitative Methods",11,14),("Economics",6,9),("Financial Statement Analysis",11,14),("Corporate Finance",6,9),("Equities",11,14),("Fixed Income",11,14),("Derivatives and Risk Management",6,9),("Alternative Investments",6,9),("Portfolio Construction",8,12)]:
    w("CFA Level I","2027",t,lo,hi,CFA1,"2027 session uses renamed topic areas.")
for t, lo, hi in [("Quantitative Methods",5,10),("Economics",5,10),("Financial Statement Analysis",10,15),("Corporate Finance",5,10),("Equities",10,15),("Fixed Income",10,15),("Derivatives and Risk Management",5,10),("Alternative Investments",5,10),("Portfolio Construction",10,15),("Ethical and Professional Standards",10,15)]:
    w("CFA Level II",None,t,lo,hi,CFA2,"Single weight table shown on the official Level II page (page links both 2026 and 2027 topic outlines); session not stated next to the table.")
for t, p in [("Foundations of Risk Management",20),("Quantitative Analysis",20),("Financial Markets and Products",30),("Valuation and Risk Models",30)]:
    w("FRM Part I","2023 curriculum",t,p,p,GARP_W,"Latest publicly downloadable GARP weights (2023 Learning Objectives PDF). The 2026 Learning Objectives are behind a form on garp.org; topic names confirmed current on garp.org/frm.")

# ---- formulas ----
F = []
def f(exam, topic, name, latex, variables, when, key=None):
    F.append({"id": None, "exam": exam, "topic": topic, "name": name, "latex": latex, "variables": variables, "when_used": when,
              "topic_source_url": SRC[exam], "source_checked": D, "uniprep2go_url": LINK[exam]})
L1, L2, FR = "CFA Level I", "CFA Level II", "FRM Part I"
QM, EC, FSA, CI, EQ, FI, DV, AI, PM = "Quantitative Methods","Economics","Financial Statement Analysis","Corporate Issuers","Equity Investments","Fixed Income","Derivatives","Alternative Investments","Portfolio Management"
# CFA Level I (2026 topic names)
f(L1,QM,"Future value (discrete compounding)",r"FV = PV\,(1+r)^{N}",r"PV present value; r periodic rate; N number of periods",r"Growing a single cash flow forward")
f(L1,QM,"Present value of an ordinary annuity",r"PV = A\,\frac{1-(1+r)^{-N}}{r}",r"A level payment at end of each period; r periodic rate; N periods",r"Loan payments, bond coupons, retirement income")
f(L1,QM,"Present value of a perpetuity",r"PV = \frac{A}{r}",r"A constant payment per period; r discount rate",r"Preferred stock, consols")
f(L1,QM,"Effective annual rate",r"EAR = \left(1+\frac{r_s}{m}\right)^{m}-1",r"r_s stated annual rate; m compounding periods per year",r"Comparing rates with different compounding frequencies")
f(L1,QM,"Continuous compounding",r"FV = PV\,e^{r_s N}",r"r_s stated annual rate; N years",r"Continuously compounded returns and growth")
f(L1,QM,"Holding period return",r"HPR = \frac{P_1 - P_0 + D_1}{P_0}",r"P_0 beginning price; P_1 ending price; D_1 income received",r"Single-period return including income")
f(L1,QM,"Geometric mean return",r"\bar R_G = \left[\prod_{t=1}^{T}(1+R_t)\right]^{1/T}-1",r"R_t return in period t; T number of periods",r"Compound average growth rate over multiple periods")
f(L1,QM,"Sample variance",r"s^2 = \frac{\sum_{i=1}^{n}(X_i-\bar X)^2}{n-1}",r"X_i observations; \bar X sample mean; n sample size",r"Dispersion of a sample")
f(L1,QM,"Coefficient of variation",r"CV = \frac{s}{\bar X}",r"s sample standard deviation; \bar X sample mean",r"Risk per unit of return")
f(L1,QM,"Sharpe ratio",r"S_p = \frac{\bar R_p - R_f}{\sigma_p}",r"\bar R_p portfolio mean return; R_f risk-free rate; \sigma_p portfolio standard deviation",r"Risk-adjusted performance")
f(L1,QM,"Sample correlation",r"r_{XY} = \frac{s_{XY}}{s_X\, s_Y}",r"s_{XY} sample covariance; s_X, s_Y sample standard deviations",r"Strength of linear relationship")
f(L1,QM,"Bayes' formula",r"P(A\mid B) = \frac{P(B\mid A)\,P(A)}{P(B)}",r"P(A) prior; P(B|A) likelihood; P(B) unconditional probability",r"Updating probabilities with new information")
f(L1,QM,"z-statistic / standardization",r"z = \frac{X-\mu}{\sigma}",r"X value; \mu mean; \sigma standard deviation",r"Standard normal probabilities")
f(L1,QM,"t-statistic for a mean",r"t = \frac{\bar X-\mu_0}{s/\sqrt{n}}",r"\bar X sample mean; \mu_0 hypothesized mean; s sample std dev; n sample size (df = n-1)",r"Hypothesis test of a population mean")
f(L1,QM,"Simple linear regression slope",r"\hat b_1 = \frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}",r"Cov(X,Y) covariance; Var(X) variance of the independent variable",r"Estimating the slope coefficient")
f(L1,QM,"Coefficient of determination (simple regression)",r"R^2 = \frac{SSR}{SST} = 1-\frac{SSE}{SST}",r"SSR regression sum of squares; SSE sum of squared errors; SST total sum of squares",r"Share of variation explained")
f(L1,EC,"Price elasticity of demand",r"E_P = \frac{\%\Delta Q_d}{\%\Delta P}",r"Q_d quantity demanded; P price",r"Responsiveness of demand to price")
f(L1,EC,"Covered interest rate parity (forward rate)",r"F_{f/d} = S_{f/d}\,\frac{1+i_f\left(\frac{\text{days}}{360}\right)}{1+i_d\left(\frac{\text{days}}{360}\right)}",r"S spot rate (price currency f per base currency d); i_f, i_d money-market rates",r"Pricing currency forwards")
f(L1,FSA,"Current ratio",r"\text{Current ratio} = \frac{\text{Current assets}}{\text{Current liabilities}}",r"—",r"Short-term liquidity")
f(L1,FSA,"Cash conversion cycle",r"CCC = DOH + DSO - \text{Days of payables}",r"DOH days of inventory on hand; DSO days of sales outstanding",r"Working-capital efficiency")
f(L1,FSA,"DuPont (three-step) ROE",r"ROE = \frac{NI}{\text{Sales}}\times\frac{\text{Sales}}{\text{Assets}}\times\frac{\text{Assets}}{\text{Equity}}",r"NI net income; average assets and equity",r"Decomposing return on equity")
f(L1,FSA,"Basic EPS",r"EPS = \frac{NI - \text{Preferred dividends}}{\text{Weighted avg. common shares}}",r"NI net income",r"Earnings per common share")
f(L1,FSA,"Interest coverage",r"\text{Interest coverage} = \frac{EBIT}{\text{Interest payments}}",r"EBIT earnings before interest and taxes",r"Solvency")
f(L1,CI,"Weighted average cost of capital",r"WACC = w_d\,r_d\,(1-t) + w_p\,r_p + w_e\,r_e",r"w weights (market values); r_d before-tax cost of debt; t marginal tax rate; r_p cost of preferred; r_e cost of equity",r"Hurdle rate for average-risk projects")
f(L1,CI,"Net present value",r"NPV = \sum_{t=0}^{N}\frac{CF_t}{(1+r)^t}",r"CF_t cash flow at t (CF_0 usually negative); r required return",r"Capital budgeting accept/reject")
f(L1,CI,"Degree of operating leverage",r"DOL = \frac{\%\Delta EBIT}{\%\Delta \text{Sales}} = \frac{Q(P-V)}{Q(P-V)-F}",r"Q units; P price; V variable cost per unit; F fixed operating costs",r"Operating risk")
f(L1,CI,"Degree of financial leverage",r"DFL = \frac{\%\Delta NI}{\%\Delta EBIT} = \frac{Q(P-V)-F}{Q(P-V)-F-C}",r"C fixed financial costs (interest)",r"Financial risk")
f(L1,CI,"CAPM cost of equity",r"r_e = R_f + \beta\,[E(R_M)-R_f]",r"R_f risk-free rate; \beta equity beta; E(R_M) expected market return",r"Required return on equity")
f(L1,EQ,"Gordon (constant) growth model",r"V_0 = \frac{D_1}{r-g}",r"D_1 next dividend; r required return; g constant growth rate (g < r)",r"Valuing mature dividend payers")
f(L1,EQ,"Justified forward P/E",r"\frac{P_0}{E_1} = \frac{D_1/E_1}{r-g}",r"D_1/E_1 payout ratio; r required return; g growth",r"Relative valuation from fundamentals")
f(L1,EQ,"Preferred stock value",r"V_0 = \frac{D_p}{r_p}",r"D_p fixed preferred dividend; r_p required return",r"Non-callable perpetual preferred shares")
f(L1,EQ,"Margin call price (long)",r"P_{call} = P_0\,\frac{1-IM}{1-MM}",r"P_0 purchase price; IM initial margin; MM maintenance margin",r"Leveraged long position")
f(L1,FI,"Bond price from yield",r"P = \sum_{t=1}^{N}\frac{PMT}{(1+r)^t} + \frac{FV}{(1+r)^N}",r"PMT coupon per period; FV par value; r market discount rate per period; N periods",r"Pricing option-free bonds")
f(L1,FI,"Modified duration",r"\text{ModDur} = \frac{\text{MacDur}}{1+r}",r"MacDur Macaulay duration; r yield per period",r"Price sensitivity to yield")
f(L1,FI,"Percentage price change (duration + convexity)",r"\%\Delta P \approx -\text{AnnModDur}\,\Delta y + \tfrac12\,\text{AnnConvexity}\,(\Delta y)^2",r"\Delta y change in annual yield (decimal)",r"Estimating price change for a yield shift")
f(L1,FI,"Money duration and PVBP",r"\text{MoneyDur} = \text{AnnModDur}\times P^{\text{full}}, \quad PVBP = \frac{PV_- - PV_+}{2}",r"P^full full price; PV_- / PV_+ prices for 1 bp down / up yield",r"Dollar interest-rate exposure")
f(L1,FI,"Forward rate from spot rates",r"(1+S_{A+B})^{A+B} = (1+S_A)^A\,(1+{}_AF_B)^B",r"S spot rates; {}_AF_B forward rate starting at A for B periods",r"Implied forward rates / bootstrapping")
f(L1,DV,"Forward price (no income)",r"F_0(T) = S_0\,(1+r)^T",r"S_0 spot price; r risk-free rate; T years",r"No-arbitrage forward pricing")
f(L1,DV,"Put–call parity",r"S_0 + p_0 = c_0 + \frac{X}{(1+r)^T}",r"S_0 spot; p_0, c_0 European put/call; X strike; r risk-free; T years",r"Relating European put and call prices")
f(L1,DV,"One-period binomial risk-neutral probability",r"\pi = \frac{1+r-d}{u-d}",r"u, d up/down factors; r risk-free rate per period",r"Binomial option pricing")
f(L1,PM,"Two-asset portfolio variance",r"\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\rho_{12}\sigma_1\sigma_2",r"w weights; \sigma std devs; \rho_{12} correlation",r"Diversification effect")
f(L1,PM,"Beta",r"\beta_i = \frac{\operatorname{Cov}(R_i,R_m)}{\sigma_m^2} = \rho_{i,m}\frac{\sigma_i}{\sigma_m}",r"R_i asset return; R_m market return",r"Systematic risk")
f(L1,PM,"Treynor ratio and Jensen's alpha",r"T_p = \frac{R_p-R_f}{\beta_p},\quad \alpha_p = R_p - [R_f + \beta_p(R_m-R_f)]",r"R_p portfolio return; \beta_p portfolio beta",r"Performance vs systematic risk")
f(L1,AI,"Hedge fund 2-and-20 fee (simplified)",r"\text{Fee} = 0.02\,AUM + 0.20\,\max(0,\ \text{Profit}-\text{Hurdle})",r"AUM assets under management; hurdle/high-water mark terms vary by fund",r"Net-of-fee return calculations")
# CFA Level II (topic names as on official Level II page)
EQ2, FI2, DV2, PC2, QM2, FSA2, CF2 = "Equities","Fixed Income","Derivatives and Risk Management","Portfolio Construction","Quantitative Methods","Financial Statement Analysis","Corporate Finance"
f(L2,QM2,"Adjusted R-squared",r"\bar R^2 = 1-\left[\frac{n-1}{n-k-1}\right](1-R^2)",r"n observations; k independent variables",r"Comparing multiple regression models")
f(L2,QM2,"F-statistic (regression)",r"F = \frac{SSR/k}{SSE/(n-k-1)}",r"SSR regression SS; SSE error SS; k slopes; n observations",r"Joint significance of slope coefficients")
f(L2,QM2,"AR(1) mean-reverting level",r"\hat x_t = \frac{b_0}{1-b_1}",r"b_0, b_1 AR(1) coefficients (|b_1| < 1)",r"Time-series forecasting")
f(L2,EQ2,"Free cash flow to the firm",r"FCFF = NI + NCC + Int(1-t) - FCInv - WCInv",r"NCC non-cash charges; Int interest expense; FCInv fixed capital investment; WCInv working capital investment",r"FCFF valuation")
f(L2,EQ2,"Free cash flow to equity",r"FCFE = FCFF - Int(1-t) + \text{Net borrowing}",r"—",r"FCFE valuation")
f(L2,EQ2,"Sustainable growth rate",r"g = b \times ROE",r"b earnings retention ratio",r"Long-run growth input for DDM")
f(L2,EQ2,"Residual income",r"RI_t = E_t - r\,B_{t-1}",r"E_t earnings; r cost of equity; B_{t-1} beginning book value",r"Residual income valuation")
f(L2,EQ2,"Residual income model",r"V_0 = B_0 + \sum_{t=1}^{\infty}\frac{E_t - rB_{t-1}}{(1+r)^t}",r"B_0 current book value per share",r"Valuing firms with no/irregular dividends")
f(L2,FI2,"Binomial interest-rate tree node value",r"V = \frac{0.5\,(V_H + C) + 0.5\,(V_L + C)}{1+i}",r"V_H, V_L values at next nodes; C coupon; i one-period forward rate at the node",r"Valuing bonds with embedded options")
f(L2,FI2,"Value of callable / putable bond",r"V_{call} = V_{straight} - V_{call\ option},\quad V_{put} = V_{straight} + V_{put\ option}",r"—",r"Embedded option valuation")
f(L2,FI2,"Credit valuation adjustment",r"CVA = \sum_{t}\text{LGD}_t \times \text{POD}_t \times DF_t",r"LGD loss given default; POD probability of default; DF discount factor",r"Valuing risky bonds")
f(L2,DV2,"Forward with carry benefits/costs",r"F_0(T) = (S_0 - PV_0(I) + PV_0(C))(1+r)^T",r"PV_0(I) PV of income; PV_0(C) PV of carry costs",r"Forwards on income-paying assets")
f(L2,DV2,"Black–Scholes–Merton call price",r"c_0 = S_0 N(d_1) - e^{-rT}X\,N(d_2),\ d_1 = \frac{\ln(S_0/X)+(r+\sigma^2/2)T}{\sigma\sqrt T},\ d_2 = d_1 - \sigma\sqrt T",r"N(·) standard normal CDF; \sigma volatility; r continuously compounded rate",r"European option pricing")
f(L2,DV2,"Swap fixed rate",r"s_N = \frac{1 - PV_N}{\sum_{i=1}^{N} PV_i}",r"PV_i discount factor for period i",r"Pricing plain-vanilla interest rate swaps")
f(L2,PC2,"Arbitrage pricing theory",r"E(R_p) = R_F + \lambda_1\beta_{p,1} + \dots + \lambda_K\beta_{p,K}",r"\lambda_j factor risk premium; \beta_{p,j} factor sensitivity",r"Multifactor expected return")
f(L2,PC2,"Parametric VaR (single asset)",r"VaR = (z_\alpha\,\sigma - \mu)\,V",r"z_\alpha standard normal quantile; \mu, \sigma period mean/std of return; V position value",r"Downside risk measurement")
# FRM Part I (GARP topic names)
FRM_, QA, FMP, VRM = "Foundations of Risk Management","Quantitative Analysis","Financial Markets and Products","Valuation and Risk Models"
f(FR,FRM_,"CAPM expected return",r"E(R_i) = R_F + \beta_i\,[E(R_M)-R_F]",r"\beta_i asset beta",r"Required return / performance evaluation")
f(FR,FRM_,"Information ratio",r"IR = \frac{R_P - R_B}{\sigma(R_P-R_B)}",r"R_B benchmark return; denominator tracking error",r"Active-management skill")
f(FR,FRM_,"Sortino ratio",r"\text{Sortino} = \frac{R_P - R_{min}}{\sigma_{downside}}",r"R_min minimum acceptable return; downside deviation",r"Downside-risk-adjusted performance")
f(FR,QA,"Variance of a sum",r"\operatorname{Var}(aX+bY) = a^2\operatorname{Var}(X) + b^2\operatorname{Var}(Y) + 2ab\operatorname{Cov}(X,Y)",r"a, b constants",r"Portfolio and aggregation math")
f(FR,QA,"OLS slope and intercept",r"\hat\beta = \frac{\sum (X_i-\bar X)(Y_i-\bar Y)}{\sum (X_i-\bar X)^2},\quad \hat\alpha = \bar Y - \hat\beta\bar X",r"—",r"Linear regression estimation")
f(FR,QA,"EWMA volatility",r"\sigma_t^2 = \lambda\,\sigma_{t-1}^2 + (1-\lambda)\,r_{t-1}^2",r"\lambda decay factor (e.g. 0.94 in RiskMetrics)",r"Volatility forecasting")
f(FR,QA,"GARCH(1,1)",r"\sigma_t^2 = \omega + \alpha\,r_{t-1}^2 + \beta\,\sigma_{t-1}^2,\quad \sigma_L^2 = \frac{\omega}{1-\alpha-\beta}",r"\omega constant; \alpha, \beta weights (\alpha+\beta < 1); \sigma_L long-run variance",r"Volatility forecasting with mean reversion")
f(FR,FMP,"Minimum-variance hedge ratio",r"h^* = \rho\,\frac{\sigma_S}{\sigma_F}",r"\rho correlation of spot and futures changes; \sigma_S, \sigma_F std devs",r"Futures hedging")
f(FR,FMP,"Optimal number of futures contracts",r"N^* = h^*\,\frac{Q_A}{Q_F}",r"Q_A size of position hedged; Q_F size of one contract",r"Futures hedging")
f(FR,FMP,"Equity beta hedge",r"N^* = (\beta^* - \beta)\,\frac{P}{F}",r"\beta target beta; P portfolio value; F value of one futures contract",r"Changing portfolio beta with index futures")
f(FR,FMP,"Futures price with storage cost and yield",r"F_0 = S_0\,e^{(r+u-q)T}",r"u storage cost rate; q income/convenience yield rate (continuous)",r"Commodity and asset futures pricing")
f(FR,FMP,"Interest rate parity (continuous)",r"F_0 = S_0\,e^{(r-r_f)T}",r"r domestic rate; r_f foreign rate (continuous)",r"FX forward pricing")
f(FR,VRM,"Parametric VaR",r"VaR_\alpha = -\mu + z_\alpha\,\sigma",r"z_\alpha standard normal quantile (e.g. 1.645 at 95%); \mu, \sigma of P&L/returns",r"Market risk measurement")
f(FR,VRM,"Expected shortfall (normal)",r"ES_\alpha = -\mu + \sigma\,\frac{\phi(z_\alpha)}{1-\alpha}",r"\phi standard normal pdf; \alpha confidence level",r"Tail risk beyond VaR")
f(FR,VRM,"Expected loss (credit)",r"EL = PD \times LGD \times EAD",r"PD probability of default; LGD loss given default; EAD exposure at default",r"Credit risk")
f(FR,VRM,"Option delta (BSM, non-dividend call/put)",r"\Delta_c = N(d_1),\quad \Delta_p = N(d_1) - 1",r"N(d_1) from BSM",r"Delta hedging")
f(FR,VRM,"Effective duration and convexity",r"D_{eff} = \frac{V_- - V_+}{2V_0\,\Delta y},\quad C_{eff} = \frac{V_- + V_+ - 2V_0}{V_0\,(\Delta y)^2}",r"V_-/V_+ values for yield down/up by \Delta y",r"Interest rate risk (incl. embedded options)")
for i, r in enumerate(F, 1):
    r["id"] = {"CFA Level I":"cfa1","CFA Level II":"cfa2","FRM Part I":"frm1"}[r["exam"]] + f"-{i:03d}"
FF = list(F[0].keys())
json.dump({"name":"cfa-frm-formula-sheets","version":"1.0.0","source_checked":D,"license":"CC-BY-4.0","entries":F}, open(root/"data/formulas.json","w"), indent=2, ensure_ascii=False)
json.dump({"source_checked":D,"entries":W}, open(root/"data/topic_weights.json","w"), indent=2, ensure_ascii=False)
for name, rows in (("formulas", F), ("topic_weights", W)):
    with open(root/f"data/{name}.csv","w",newline="") as fh:
        wr = csv.DictWriter(fh, list(rows[0].keys())); wr.writeheader(); [wr.writerow({k:("" if v is None else v) for k,v in r.items()}) for r in rows]
print(len(F), "formulas;", len(W), "weight rows")
