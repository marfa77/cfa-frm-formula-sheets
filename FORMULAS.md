# Formula sheet (CFA Level I, CFA Level II, FRM Part I)

Generated from `data/formulas.json` (v1.0.0). Rendered version: https://marfa77.github.io/cfa-frm-formula-sheets/


## CFA Level I


### Quantitative Methods

- **Future value (discrete compounding)** (`cfa1-001`): $$FV = PV\,(1+r)^{N}$$ 
  Variables: PV present value; r periodic rate; N number of periods. Used for: Growing a single cash flow forward.
- **Present value of an ordinary annuity** (`cfa1-002`): $$PV = A\,\frac{1-(1+r)^{-N}}{r}$$ 
  Variables: A level payment at end of each period; r periodic rate; N periods. Used for: Loan payments, bond coupons, retirement income.
- **Present value of a perpetuity** (`cfa1-003`): $$PV = \frac{A}{r}$$ 
  Variables: A constant payment per period; r discount rate. Used for: Preferred stock, consols.
- **Effective annual rate** (`cfa1-004`): $$EAR = \left(1+\frac{r_s}{m}\right)^{m}-1$$ 
  Variables: r_s stated annual rate; m compounding periods per year. Used for: Comparing rates with different compounding frequencies.
- **Continuous compounding** (`cfa1-005`): $$FV = PV\,e^{r_s N}$$ 
  Variables: r_s stated annual rate; N years. Used for: Continuously compounded returns and growth.
- **Holding period return** (`cfa1-006`): $$HPR = \frac{P_1 - P_0 + D_1}{P_0}$$ 
  Variables: P_0 beginning price; P_1 ending price; D_1 income received. Used for: Single-period return including income.
- **Geometric mean return** (`cfa1-007`): $$\bar R_G = \left[\prod_{t=1}^{T}(1+R_t)\right]^{1/T}-1$$ 
  Variables: R_t return in period t; T number of periods. Used for: Compound average growth rate over multiple periods.
- **Sample variance** (`cfa1-008`): $$s^2 = \frac{\sum_{i=1}^{n}(X_i-\bar X)^2}{n-1}$$ 
  Variables: X_i observations; \bar X sample mean; n sample size. Used for: Dispersion of a sample.
- **Coefficient of variation** (`cfa1-009`): $$CV = \frac{s}{\bar X}$$ 
  Variables: s sample standard deviation; \bar X sample mean. Used for: Risk per unit of return.
- **Sharpe ratio** (`cfa1-010`): $$S_p = \frac{\bar R_p - R_f}{\sigma_p}$$ 
  Variables: \bar R_p portfolio mean return; R_f risk-free rate; \sigma_p portfolio standard deviation. Used for: Risk-adjusted performance.
- **Sample correlation** (`cfa1-011`): $$r_{XY} = \frac{s_{XY}}{s_X\, s_Y}$$ 
  Variables: s_{XY} sample covariance; s_X, s_Y sample standard deviations. Used for: Strength of linear relationship.
- **Bayes' formula** (`cfa1-012`): $$P(A\mid B) = \frac{P(B\mid A)\,P(A)}{P(B)}$$ 
  Variables: P(A) prior; P(B|A) likelihood; P(B) unconditional probability. Used for: Updating probabilities with new information.
- **z-statistic / standardization** (`cfa1-013`): $$z = \frac{X-\mu}{\sigma}$$ 
  Variables: X value; \mu mean; \sigma standard deviation. Used for: Standard normal probabilities.
- **t-statistic for a mean** (`cfa1-014`): $$t = \frac{\bar X-\mu_0}{s/\sqrt{n}}$$ 
  Variables: \bar X sample mean; \mu_0 hypothesized mean; s sample std dev; n sample size (df = n-1). Used for: Hypothesis test of a population mean.
- **Simple linear regression slope** (`cfa1-015`): $$\hat b_1 = \frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}$$ 
  Variables: Cov(X,Y) covariance; Var(X) variance of the independent variable. Used for: Estimating the slope coefficient.
- **Coefficient of determination (simple regression)** (`cfa1-016`): $$R^2 = \frac{SSR}{SST} = 1-\frac{SSE}{SST}$$ 
  Variables: SSR regression sum of squares; SSE sum of squared errors; SST total sum of squares. Used for: Share of variation explained.

### Economics

- **Price elasticity of demand** (`cfa1-017`): $$E_P = \frac{\%\Delta Q_d}{\%\Delta P}$$ 
  Variables: Q_d quantity demanded; P price. Used for: Responsiveness of demand to price.
- **Covered interest rate parity (forward rate)** (`cfa1-018`): $$F_{f/d} = S_{f/d}\,\frac{1+i_f\left(\frac{\text{days}}{360}\right)}{1+i_d\left(\frac{\text{days}}{360}\right)}$$ 
  Variables: S spot rate (price currency f per base currency d); i_f, i_d money-market rates. Used for: Pricing currency forwards.

### Financial Statement Analysis

- **Current ratio** (`cfa1-019`): $$\text{Current ratio} = \frac{\text{Current assets}}{\text{Current liabilities}}$$ 
  Variables: —. Used for: Short-term liquidity.
- **Cash conversion cycle** (`cfa1-020`): $$CCC = DOH + DSO - \text{Days of payables}$$ 
  Variables: DOH days of inventory on hand; DSO days of sales outstanding. Used for: Working-capital efficiency.
- **DuPont (three-step) ROE** (`cfa1-021`): $$ROE = \frac{NI}{\text{Sales}}\times\frac{\text{Sales}}{\text{Assets}}\times\frac{\text{Assets}}{\text{Equity}}$$ 
  Variables: NI net income; average assets and equity. Used for: Decomposing return on equity.
- **Basic EPS** (`cfa1-022`): $$EPS = \frac{NI - \text{Preferred dividends}}{\text{Weighted avg. common shares}}$$ 
  Variables: NI net income. Used for: Earnings per common share.
- **Interest coverage** (`cfa1-023`): $$\text{Interest coverage} = \frac{EBIT}{\text{Interest payments}}$$ 
  Variables: EBIT earnings before interest and taxes. Used for: Solvency.

### Corporate Issuers

- **Weighted average cost of capital** (`cfa1-024`): $$WACC = w_d\,r_d\,(1-t) + w_p\,r_p + w_e\,r_e$$ 
  Variables: w weights (market values); r_d before-tax cost of debt; t marginal tax rate; r_p cost of preferred; r_e cost of equity. Used for: Hurdle rate for average-risk projects.
- **Net present value** (`cfa1-025`): $$NPV = \sum_{t=0}^{N}\frac{CF_t}{(1+r)^t}$$ 
  Variables: CF_t cash flow at t (CF_0 usually negative); r required return. Used for: Capital budgeting accept/reject.
- **Degree of operating leverage** (`cfa1-026`): $$DOL = \frac{\%\Delta EBIT}{\%\Delta \text{Sales}} = \frac{Q(P-V)}{Q(P-V)-F}$$ 
  Variables: Q units; P price; V variable cost per unit; F fixed operating costs. Used for: Operating risk.
- **Degree of financial leverage** (`cfa1-027`): $$DFL = \frac{\%\Delta NI}{\%\Delta EBIT} = \frac{Q(P-V)-F}{Q(P-V)-F-C}$$ 
  Variables: C fixed financial costs (interest). Used for: Financial risk.
- **CAPM cost of equity** (`cfa1-028`): $$r_e = R_f + \beta\,[E(R_M)-R_f]$$ 
  Variables: R_f risk-free rate; \beta equity beta; E(R_M) expected market return. Used for: Required return on equity.

### Equity Investments

- **Gordon (constant) growth model** (`cfa1-029`): $$V_0 = \frac{D_1}{r-g}$$ 
  Variables: D_1 next dividend; r required return; g constant growth rate (g < r). Used for: Valuing mature dividend payers.
- **Justified forward P/E** (`cfa1-030`): $$\frac{P_0}{E_1} = \frac{D_1/E_1}{r-g}$$ 
  Variables: D_1/E_1 payout ratio; r required return; g growth. Used for: Relative valuation from fundamentals.
- **Preferred stock value** (`cfa1-031`): $$V_0 = \frac{D_p}{r_p}$$ 
  Variables: D_p fixed preferred dividend; r_p required return. Used for: Non-callable perpetual preferred shares.
- **Margin call price (long)** (`cfa1-032`): $$P_{call} = P_0\,\frac{1-IM}{1-MM}$$ 
  Variables: P_0 purchase price; IM initial margin; MM maintenance margin. Used for: Leveraged long position.

### Fixed Income

- **Bond price from yield** (`cfa1-033`): $$P = \sum_{t=1}^{N}\frac{PMT}{(1+r)^t} + \frac{FV}{(1+r)^N}$$ 
  Variables: PMT coupon per period; FV par value; r market discount rate per period; N periods. Used for: Pricing option-free bonds.
- **Modified duration** (`cfa1-034`): $$\text{ModDur} = \frac{\text{MacDur}}{1+r}$$ 
  Variables: MacDur Macaulay duration; r yield per period. Used for: Price sensitivity to yield.
- **Percentage price change (duration + convexity)** (`cfa1-035`): $$\%\Delta P \approx -\text{AnnModDur}\,\Delta y + \tfrac12\,\text{AnnConvexity}\,(\Delta y)^2$$ 
  Variables: \Delta y change in annual yield (decimal). Used for: Estimating price change for a yield shift.
- **Money duration and PVBP** (`cfa1-036`): $$\text{MoneyDur} = \text{AnnModDur}\times P^{\text{full}}, \quad PVBP = \frac{PV_- - PV_+}{2}$$ 
  Variables: P^full full price; PV_- / PV_+ prices for 1 bp down / up yield. Used for: Dollar interest-rate exposure.
- **Forward rate from spot rates** (`cfa1-037`): $$(1+S_{A+B})^{A+B} = (1+S_A)^A\,(1+{}_AF_B)^B$$ 
  Variables: S spot rates; {}_AF_B forward rate starting at A for B periods. Used for: Implied forward rates / bootstrapping.

### Derivatives

- **Forward price (no income)** (`cfa1-038`): $$F_0(T) = S_0\,(1+r)^T$$ 
  Variables: S_0 spot price; r risk-free rate; T years. Used for: No-arbitrage forward pricing.
- **Put–call parity** (`cfa1-039`): $$S_0 + p_0 = c_0 + \frac{X}{(1+r)^T}$$ 
  Variables: S_0 spot; p_0, c_0 European put/call; X strike; r risk-free; T years. Used for: Relating European put and call prices.
- **One-period binomial risk-neutral probability** (`cfa1-040`): $$\pi = \frac{1+r-d}{u-d}$$ 
  Variables: u, d up/down factors; r risk-free rate per period. Used for: Binomial option pricing.

### Portfolio Management

- **Two-asset portfolio variance** (`cfa1-041`): $$\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\rho_{12}\sigma_1\sigma_2$$ 
  Variables: w weights; \sigma std devs; \rho_{12} correlation. Used for: Diversification effect.
- **Beta** (`cfa1-042`): $$\beta_i = \frac{\operatorname{Cov}(R_i,R_m)}{\sigma_m^2} = \rho_{i,m}\frac{\sigma_i}{\sigma_m}$$ 
  Variables: R_i asset return; R_m market return. Used for: Systematic risk.
- **Treynor ratio and Jensen's alpha** (`cfa1-043`): $$T_p = \frac{R_p-R_f}{\beta_p},\quad \alpha_p = R_p - [R_f + \beta_p(R_m-R_f)]$$ 
  Variables: R_p portfolio return; \beta_p portfolio beta. Used for: Performance vs systematic risk.

### Alternative Investments

- **Hedge fund 2-and-20 fee (simplified)** (`cfa1-044`): $$\text{Fee} = 0.02\,AUM + 0.20\,\max(0,\ \text{Profit}-\text{Hurdle})$$ 
  Variables: AUM assets under management; hurdle/high-water mark terms vary by fund. Used for: Net-of-fee return calculations.

## CFA Level II


### Quantitative Methods

- **Adjusted R-squared** (`cfa2-045`): $$\bar R^2 = 1-\left[\frac{n-1}{n-k-1}\right](1-R^2)$$ 
  Variables: n observations; k independent variables. Used for: Comparing multiple regression models.
- **F-statistic (regression)** (`cfa2-046`): $$F = \frac{SSR/k}{SSE/(n-k-1)}$$ 
  Variables: SSR regression SS; SSE error SS; k slopes; n observations. Used for: Joint significance of slope coefficients.
- **AR(1) mean-reverting level** (`cfa2-047`): $$\hat x_t = \frac{b_0}{1-b_1}$$ 
  Variables: b_0, b_1 AR(1) coefficients (|b_1| < 1). Used for: Time-series forecasting.

### Equities

- **Free cash flow to the firm** (`cfa2-048`): $$FCFF = NI + NCC + Int(1-t) - FCInv - WCInv$$ 
  Variables: NCC non-cash charges; Int interest expense; FCInv fixed capital investment; WCInv working capital investment. Used for: FCFF valuation.
- **Free cash flow to equity** (`cfa2-049`): $$FCFE = FCFF - Int(1-t) + \text{Net borrowing}$$ 
  Variables: —. Used for: FCFE valuation.
- **Sustainable growth rate** (`cfa2-050`): $$g = b \times ROE$$ 
  Variables: b earnings retention ratio. Used for: Long-run growth input for DDM.
- **Residual income** (`cfa2-051`): $$RI_t = E_t - r\,B_{t-1}$$ 
  Variables: E_t earnings; r cost of equity; B_{t-1} beginning book value. Used for: Residual income valuation.
- **Residual income model** (`cfa2-052`): $$V_0 = B_0 + \sum_{t=1}^{\infty}\frac{E_t - rB_{t-1}}{(1+r)^t}$$ 
  Variables: B_0 current book value per share. Used for: Valuing firms with no/irregular dividends.

### Fixed Income

- **Binomial interest-rate tree node value** (`cfa2-053`): $$V = \frac{0.5\,(V_H + C) + 0.5\,(V_L + C)}{1+i}$$ 
  Variables: V_H, V_L values at next nodes; C coupon; i one-period forward rate at the node. Used for: Valuing bonds with embedded options.
- **Value of callable / putable bond** (`cfa2-054`): $$V_{call} = V_{straight} - V_{call\ option},\quad V_{put} = V_{straight} + V_{put\ option}$$ 
  Variables: —. Used for: Embedded option valuation.
- **Credit valuation adjustment** (`cfa2-055`): $$CVA = \sum_{t}\text{LGD}_t \times \text{POD}_t \times DF_t$$ 
  Variables: LGD loss given default; POD probability of default; DF discount factor. Used for: Valuing risky bonds.

### Derivatives and Risk Management

- **Forward with carry benefits/costs** (`cfa2-056`): $$F_0(T) = (S_0 - PV_0(I) + PV_0(C))(1+r)^T$$ 
  Variables: PV_0(I) PV of income; PV_0(C) PV of carry costs. Used for: Forwards on income-paying assets.
- **Black–Scholes–Merton call price** (`cfa2-057`): $$c_0 = S_0 N(d_1) - e^{-rT}X\,N(d_2),\ d_1 = \frac{\ln(S_0/X)+(r+\sigma^2/2)T}{\sigma\sqrt T},\ d_2 = d_1 - \sigma\sqrt T$$ 
  Variables: N(·) standard normal CDF; \sigma volatility; r continuously compounded rate. Used for: European option pricing.
- **Swap fixed rate** (`cfa2-058`): $$s_N = \frac{1 - PV_N}{\sum_{i=1}^{N} PV_i}$$ 
  Variables: PV_i discount factor for period i. Used for: Pricing plain-vanilla interest rate swaps.

### Portfolio Construction

- **Arbitrage pricing theory** (`cfa2-059`): $$E(R_p) = R_F + \lambda_1\beta_{p,1} + \dots + \lambda_K\beta_{p,K}$$ 
  Variables: \lambda_j factor risk premium; \beta_{p,j} factor sensitivity. Used for: Multifactor expected return.
- **Parametric VaR (single asset)** (`cfa2-060`): $$VaR = (z_\alpha\,\sigma - \mu)\,V$$ 
  Variables: z_\alpha standard normal quantile; \mu, \sigma period mean/std of return; V position value. Used for: Downside risk measurement.

## FRM Part I


### Foundations of Risk Management

- **CAPM expected return** (`frm1-061`): $$E(R_i) = R_F + \beta_i\,[E(R_M)-R_F]$$ 
  Variables: \beta_i asset beta. Used for: Required return / performance evaluation.
- **Information ratio** (`frm1-062`): $$IR = \frac{R_P - R_B}{\sigma(R_P-R_B)}$$ 
  Variables: R_B benchmark return; denominator tracking error. Used for: Active-management skill.
- **Sortino ratio** (`frm1-063`): $$\text{Sortino} = \frac{R_P - R_{min}}{\sigma_{downside}}$$ 
  Variables: R_min minimum acceptable return; downside deviation. Used for: Downside-risk-adjusted performance.

### Quantitative Analysis

- **Variance of a sum** (`frm1-064`): $$\operatorname{Var}(aX+bY) = a^2\operatorname{Var}(X) + b^2\operatorname{Var}(Y) + 2ab\operatorname{Cov}(X,Y)$$ 
  Variables: a, b constants. Used for: Portfolio and aggregation math.
- **OLS slope and intercept** (`frm1-065`): $$\hat\beta = \frac{\sum (X_i-\bar X)(Y_i-\bar Y)}{\sum (X_i-\bar X)^2},\quad \hat\alpha = \bar Y - \hat\beta\bar X$$ 
  Variables: —. Used for: Linear regression estimation.
- **EWMA volatility** (`frm1-066`): $$\sigma_t^2 = \lambda\,\sigma_{t-1}^2 + (1-\lambda)\,r_{t-1}^2$$ 
  Variables: \lambda decay factor (e.g. 0.94 in RiskMetrics). Used for: Volatility forecasting.
- **GARCH(1,1)** (`frm1-067`): $$\sigma_t^2 = \omega + \alpha\,r_{t-1}^2 + \beta\,\sigma_{t-1}^2,\quad \sigma_L^2 = \frac{\omega}{1-\alpha-\beta}$$ 
  Variables: \omega constant; \alpha, \beta weights (\alpha+\beta < 1); \sigma_L long-run variance. Used for: Volatility forecasting with mean reversion.

### Financial Markets and Products

- **Minimum-variance hedge ratio** (`frm1-068`): $$h^* = \rho\,\frac{\sigma_S}{\sigma_F}$$ 
  Variables: \rho correlation of spot and futures changes; \sigma_S, \sigma_F std devs. Used for: Futures hedging.
- **Optimal number of futures contracts** (`frm1-069`): $$N^* = h^*\,\frac{Q_A}{Q_F}$$ 
  Variables: Q_A size of position hedged; Q_F size of one contract. Used for: Futures hedging.
- **Equity beta hedge** (`frm1-070`): $$N^* = (\beta^* - \beta)\,\frac{P}{F}$$ 
  Variables: \beta target beta; P portfolio value; F value of one futures contract. Used for: Changing portfolio beta with index futures.
- **Futures price with storage cost and yield** (`frm1-071`): $$F_0 = S_0\,e^{(r+u-q)T}$$ 
  Variables: u storage cost rate; q income/convenience yield rate (continuous). Used for: Commodity and asset futures pricing.
- **Interest rate parity (continuous)** (`frm1-072`): $$F_0 = S_0\,e^{(r-r_f)T}$$ 
  Variables: r domestic rate; r_f foreign rate (continuous). Used for: FX forward pricing.

### Valuation and Risk Models

- **Parametric VaR** (`frm1-073`): $$VaR_\alpha = -\mu + z_\alpha\,\sigma$$ 
  Variables: z_\alpha standard normal quantile (e.g. 1.645 at 95%); \mu, \sigma of P&L/returns. Used for: Market risk measurement.
- **Expected shortfall (normal)** (`frm1-074`): $$ES_\alpha = -\mu + \sigma\,\frac{\phi(z_\alpha)}{1-\alpha}$$ 
  Variables: \phi standard normal pdf; \alpha confidence level. Used for: Tail risk beyond VaR.
- **Expected loss (credit)** (`frm1-075`): $$EL = PD \times LGD \times EAD$$ 
  Variables: PD probability of default; LGD loss given default; EAD exposure at default. Used for: Credit risk.
- **Option delta (BSM, non-dividend call/put)** (`frm1-076`): $$\Delta_c = N(d_1),\quad \Delta_p = N(d_1) - 1$$ 
  Variables: N(d_1) from BSM. Used for: Delta hedging.
- **Effective duration and convexity** (`frm1-077`): $$D_{eff} = \frac{V_- - V_+}{2V_0\,\Delta y},\quad C_{eff} = \frac{V_- + V_+ - 2V_0}{V_0\,(\Delta y)^2}$$ 
  Variables: V_-/V_+ values for yield down/up by \Delta y. Used for: Interest rate risk (incl. embedded options).
