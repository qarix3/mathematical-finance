# Examples

## Portfolio Visualizer

### Portfolio Modeling

Backtest Asset Allocation
Backtest Portfolio Performance

### Monte Carlo Simulations

Monte Carlo Simulation
Monte Carlo Simulation Using Forward Looking Capital Market Expectations
Financial Goals Planning

### Portfolio Optimization

Efficient Frontier
Resampled Efficient Frontier
Mean Variance Optimization
Risk Parity Optimization
Constrained Optimization
Portfolio Optimization Using Forward Looking Capital Market Expectations
Risk Factor Based Allocation

### Asset Analytics

Asset Correlations
Factor Regression Analysis

### Timing Models

Moving Averages
Relative Strength
Dual Momentum
Adaptive Allocation
Target Volatility

---

## Asset Allocation

Compare historical performance and risk vs. return profile of different asset allocations:

**Portfolio #1**
60% Total US Stock Market
40% Total US Bond Market

**Portfolio #2**
40% Total US Stock Market
20% International ex-US Stock Market
10% Real Estate
30% Total US Bond Market

## Portfolio Performance

40% Vanguard Total Stock Market Index Fund (VTSMX)
20% Vanguard Total International Stock Index Fund (VGTSX)
10% Vanguard Real Estate Index Fund (VGSIX)
30% Vanguard Total Bond Market Index Fund (VBMFX)

## Monte Carlo Simulation

Use the Monte Carlo simulation tool to model the probability of
different outcomes based on the given portfolio asset allocation and cashflows.

## Monte Carlo Simulation Using Forward Looking Capital Market Expectations

Simulate portfolio performance with forward looking return and volatility
assumptions rather than relying on historical estimates for asset returns.

Sample Capital Market Expectations

|Asset Class|Expected Return|
| :----------- | :----------- |
|US Equities|5.5%|
|International Equities|5.7%|
|US Bonds|1.8%|
|REITs|5.0%|

Sample assumptions for expected annual returns

## Financial Goals Planning

Use Monte Carlo simulation to test portfolio growth and survival
against specified financial goals both during career and retirement.

* Save $1,500 per month during career
* Support college education for one child with $40,000 per year for 4 years
* Withdraw $3,500 per month during retirement

## Efficient Frontier

Visualize the efficient frontier for any asset classes or funds.

What asset mix has provided the best risk adjusted return historically?

How has the efficient frontier changed from decade to decade?

## Resampled Efficient Frontier

Use resampling to mitigate the impact of input estimate errors
in the mean variance optimization and to improve diversification
in the efficient frontier portfolios

## Mean Variance Optimization

Use the portfolio optimization tool to optimize portfolios based on risk adjusted performance or other target criteria.

Vanguard Total Stock Market ETF (VTI)
iShares S&P SmallCap 600 Value Index Fund ETF (IJS)
iShares MSCI EAFE Index Fund ETF (EFA)
Vanguard Emerging Markets ETF (VWO)
Vanguard Real Estate ETF (VNQ)
iShares Barclays 20 Year Treasury Bond Fund ETF (TLT)
iShares Corporate Bond Fund ETF (LQD)
SPDR Gold Shares ETF (GLD)

## Risk Parity Optimization

Use optimization to find the risk parity portfolio that equalizes the risk contributions of portfolio assets.

Allocation constraints
|Asset|Risk Contribution Target|
| :----------- | :----------- |
|Vanguard Total Stock Market ETF (VTI)|25%|
|Vanguard Total International Stock ETF (VXUS)|25%|
|Vanguard Real Estate ETF (VNQ)|25%|
|Vanguard Total Bond Market ETF (BND)|25%|

## Constrained Optimization

Use allocation weight constraints at both asset and asset group level to enforce specific minimum and maximum allocation weights.

|Asset|Group|Min Weight|Max Weight|
| :----------- | :----------- | :----------- |:-----------|
|SPDR S&P 500 ETF|Equity|5%|40%|
|iShares S&P Small-Cap 600 Value ETF|Equity|5%|20%|
|iShares MSCI EAFE ETF|Equity|5%|30%|
|iShares MSCI Emerging Markets ETF|Equity|5%|15%|
|iShares 20+ Year Treasury Bond ETF|Fixed Income|5%|30%|
|iShares 7-10 Year Treasury Bond ETF|Fixed Income|5%|30%|
|iShares iBoxx $ Invmt Grade Corp Bd ETF|Fixed Income|5%|20%|

## Market Timing - Moving Averages

Backtest moving average timing models for a single asset or for a portfolio of assets.
For example, test market timing with the S&P 500 index using VFINX with 10-month simple moving average (SMA) from 1990 onwards.

## Market Timing - Relative Strength

How well did momentum based asset class rotation work in the past?
Backtest asset class ETF momentum strategy rotating across asset classes based on past 5-month performance:

iShares Russell 1000 Index (IWB)
iShares Russell 2000 Index (IWM)
iShares MSCI EAFE Index Fund (EFA)
iShares MSCI Emerging Markets Index (EEM)
SPDR Dow Jones REIT ETF (RWR)
PowerShares DB Commodity Index Fund (DBC)
SPDR Gold Shares (GLD)
iShares 20+ Year Treasury Bond ETF (TLT)
T-Bills/Cash
Compare the results against buy-and-hold portfolios. How would the results change based on different time periods?

## Market Timing - Dual Momentum

Explore dual momentum timing model combining relative momentum with an absolute momentum based trend-following filter:

Momentum Assets:
Vanguard 500 Index Fund (VFINX)
Vanguard Total International Stock Index Fund (VGTSX)
Fixed Income Asset:
Vanguard Total Bond Market Index Fund (VBMFX)

## Market Timing - Adaptive Allocation

Adaptive asset allocation model combining relative strength momentum model
with inverse volatility or minimum variance based asset weights.

Hold top two best performing assets with risk parity weighting:

Vanguard Total Stock Market Index Fund (VTSMX)
Vanguard Total International Stock Index Fund (VGTSX)
Vanguard Real Estate Index Fund (VGSIX)
Vanguard Total Bond Market Index Fund (VBMFX)

## Market Timing - Target Volatility

Use target volatility model to keep portfolio within preferred risk tolerance.
Compare drawdowns and risk adjusted performance against annually rebalanced buy-and-hold portfolio.

Portfolio assets for 8% annualized volatility target:

40% Vanguard Total Stock Market Index Fund (VTSMX)
20% Vanguard Total International Stock Index Fund (VGTSX)
10% Vanguard Real Estate Index Fund (VGSIX)
30% Vanguard Total Bond Market Index Fund (VBMFX)