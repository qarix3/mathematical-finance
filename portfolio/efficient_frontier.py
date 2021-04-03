

@staticmethod
def get_my_targets():
    return np.arange(0, 1.5, 0.05)


@staticmethod
def get_end_date():
    return dt.date.today()


@staticmethod
def get_start_date(end_date):
    return end_date - dt.timedelta(days=settings.YearsToGoBack * 365)


# chart_plotter.py
class ChartPlotter:

    def __init__(self, mc):
        self.__mc = mc

    def plot_efficient_frontier(self, data):
        plt.plot(data['Risk'], data['Return'], 'r-x')

    def show_plots(self):
        plt.show()

    def plot_single_point(self, x, y, title, colour):
        plt.scatter(x=x, y=y, c=colour, marker='D', s=200)
        plt.annotate(title,  # this is the text
                     (x, y),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 10),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    def plot_portfolios(self, df):
        # find min Volatility & max sharpe values in the dataframe (df)

        max_sharpe_ratio = self.__mc.get_max_sharpe_ratio(df)
        min_risk = self.__mc.get_min_risk(df)

        plt.scatter(df['Risk'], df['Return'], c=df['SharpeRatio'], cmap='viridis', edgecolors='red')
        x = max_sharpe_ratio['Risk']
        y = max_sharpe_ratio['Return']
        name = max_sharpe_ratio['Portfolio']

        plt.title(str(len(df)) + " Portfolios Risk-Return")
        plt.xlabel("Risk")
        plt.ylabel("Return")

        self.plot_single_point(x, y, 'Max Sharpe Ratio: ' + name, 'green')
        x = min_risk['Risk']
        y = min_risk['Return']
        name = min_risk['Portfolio']
        self.plot_single_point(x, y, 'Min Risk: ' + name, 'red')

        equal_allocations_portfolio = df.loc[df['Portfolio'] == 'EqualAllocationPortfolio']
        x = equal_allocations_portfolio['Risk']
        y = equal_allocations_portfolio['Return']
        name = equal_allocations_portfolio['Portfolio']
        self.plot_single_point(x, y, 'Portfolio: ' + name, 'black')

    def plot_prices(self, closing_prices):
        ax = plt.gca()
        columns = [c for c in closing_prices.columns if c not in 'Date']
        closing_prices.plot(kind='line', use_index=True, y=columns, ax=ax, title='Asset (Stock) Prices')
        plt.show()

    def plot_returns(self, returns):
        ax = plt.gca()
        columns = [c for c in returns.columns if c not in 'Date']
        returns.plot(kind='line', use_index=True, y=columns, ax=ax, title='Asset (Stock) Returns')
        plt.show()

    def plot_correlation_matrix(self, df):
        cols = df.columns.values
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(df.corr(), interpolation='nearest')
        fig.colorbar(cax)

        ax.set_xticklabels(cols)
        ax.set_yticklabels(cols)
        plt.show()


class PortfoliosAllocationMapper:
    def __init__(self):
        pass

    @staticmethod
    def map_to_risk_return_ratios(input):
        portfolios = input.columns.values[2:]
        returns = input.loc[input['Symbol'] == 'Return'].values[0][2:]
        risks = input.loc[input['Symbol'] == 'Risk'].values[0][2:]
        sharpe_ratios = input.loc[input['Symbol'] == 'SharpeRatio'].values[0][2:]
        df = pd.DataFrame(
            {'Portfolio': portfolios,
             'Return': returns,
             'Risk': risks,
             'SharpeRatio': sharpe_ratios})
        return df


# file_repository.py
class FileRepository:

    def __init__(self, directory):
        self.__writer = pd.ExcelWriter(directory, engine='xlsxwriter')

    def save_to_file(self, data, sheet_name=None):
        data.to_excel(self.__writer, sheet_name=sheet_name, header=True)

    def close(self):
        self.__writer.save()


# monte_carlo.py
class MonteCarlo:
    def __init__(self, mc, risk_function, return_function, numberOfPortfolios):
        self.__numberOfPortfolios = numberOfPortfolios
        self.__risk_function = risk_function
        self.__return_function = return_function
        self.__mc = mc

    def generate_portfolios(self, returns, covariance, risk_free_rate):

        portfolios_allocations_df = pd.DataFrame({'Symbol': returns.index, 'MeanReturn': returns.values})
        extra_data = pd.DataFrame({'Symbol': ['Return', 'Risk', 'SharpeRatio'], 'MeanReturn': [0, 0, 0]})
        portfolios_allocations_df = portfolios_allocations_df.append(extra_data, ignore_index=True)

        portfolio_size = len(returns.index)
        np.random.seed(0)

        # Adding equal allocation so I can assess how good/bad it is
        equal_allocations = get_equal_allocations(portfolio_size)
        portfolio_id = 'EqualAllocationPortfolio'
        self.compute_portfolio_risk_return_sharpe_ratio(portfolio_id, equal_allocations, portfolios_allocations_df,
                                                        returns, covariance, risk_free_rate)

        # Generating portfolios
        counter_to_print = int(self.__numberOfPortfolios / 10)
        for i in range(self.__numberOfPortfolios):
            portfolio_id = 'Portfolio_' + str(i)
            allocations = get_random_allocations(portfolio_size)
            self.compute_portfolio_risk_return_sharpe_ratio(portfolio_id, allocations, portfolios_allocations_df,
                                                            returns, covariance, risk_free_rate)

            # printing approx 10x
            if (i % counter_to_print == 0):
                print('Completed Generating ' + str(i) + 'Portfolios')

        return portfolios_allocations_df

    def compute_portfolio_risk_return_sharpe_ratio(self, portfolio_id, allocations, portfolios_allocations_df, returns,
                                                   covariance, risk_free_rate):

        # Calculate expected returns of portfolio
        expected_returns = self.__return_function(returns, allocations)
        # Calculate risk of portfolio
        risk = self.__risk_function(allocations, covariance)
        # Calculate Sharpe ratio of portfolio
        sharpe_ratio = self.__mc.calculate_sharpe_ratio(risk, expected_returns, risk_free_rate)

        portfolio_data = allocations
        portfolio_data = np.append(portfolio_data, expected_returns)
        portfolio_data = np.append(portfolio_data, risk)
        portfolio_data = np.append(portfolio_data, sharpe_ratio)
        # add data to the dataframe
        portfolios_allocations_df[portfolio_id] = portfolio_data

    def get_random_allocations(portfolio_size):
        allocations = np.random.rand(portfolio_size)
        allocations /= sum(allocations)
        return allocations

    def get_equal_allocations(portfolio_size):
        n = float(1 / portfolio_size)
        allocations = np.repeat(n, portfolio_size)
        return allocations


# object_factory.py
class ObjectFactory:

    def __init__(self, settings):
        self.__settings = settings

    def get_price_extractor(self, companies):
        return price_extractor(self.__settings.API, companies)

    def get_metrics_calculator(self):
        return metrics_calculator

    def get_charts_plotter(self):
        return chart_plotter(self.get_metrics_calculator())

    def get_companies_extractor(self):
        return static_companies_extractor(self.__settings.MyCompanies)

    def get_portfolio_generator(self):
        return monte_carlo_simulator(self.get_metrics_calculator(), self.__settings.RiskFunction,
                                     self.__settings.ReturnFunction, self.__settings.NumberOfPortfolios)

    def get_file_repository(self):
        return file_repository(self.__settings.PortfolioOptimisationPath)

    def get_optimiser(self, targets, size):
        return optimiser_factory.optimiser(self.get_metrics_calculator(), self.__settings.RiskFunction,
                                           self.__settings.ReturnFunction, targets, size)


# optimiser_factory.py
class Optimiser:
    Constraints = []

    def __init__(self, mc, risk_function, return_function, targets, portfolio_size):
        self.__portfolio_size = portfolio_size
        self.__targets = targets
        self.__mc = mc
        self.__risk_function = risk_function
        self.__return_function = return_function

    def generate_portfolios(self, returns, covariance, risk_free_rate):
        x0 = np.ones(self.__portfolio_size) * (1.0 / self.__portfolio_size)
        bounds = ((0, 1),) * (self.__portfolio_size)

        portfolios_allocations_df = pd.DataFrame({'Symbol': returns.index, 'MeanReturn': returns.values})
        extra_data = pd.DataFrame({'Symbol': ['Return', 'Risk', 'SharpeRatio'], 'MeanReturn': [0, 0, 0]})
        portfolios_allocations_df = portfolios_allocations_df.append(extra_data, ignore_index=True)

        i = 0
        counter_to_print = int(len(self.__targets) / 10)
        for my_return in self.__targets:
            constraints = []
            constraints.append({'type': 'eq', 'fun': lambda inputs: 1.0 - np.sum(inputs)})
            constraints.append({'type': 'eq', 'args': (returns,),
                                'fun': lambda allocations, returns:
                                my_return - self.__return_function(returns, allocations)})

            # optimised allocations
            allocations = self.solve(x0, constraints, bounds, covariance).x
            expectedreturns = self.__return_function(returns, allocations)

            # Calculate volatility
            volatility = self.__risk_function(allocations, covariance)

            sharpe_ratio = self.__mc.calculate_sharpe_ratio(volatility, expectedreturns, risk_free_rate)

            portfolio_data = allocations
            portfolio_data = np.append(portfolio_data, expectedreturns)
            portfolio_data = np.append(portfolio_data, volatility)
            portfolio_data = np.append(portfolio_data, sharpe_ratio)

            i = i + 1
            portfolio_id = 'Portfolio_' + str(i)
            portfolios_allocations_df[portfolio_id] = portfolio_data

            # printing approx 10x
            if (i % counter_to_print == 0):
                print('Completed Generating ' + str(i) + ' Portfolios')
        return portfolios_allocations_df

    def solve(self, x0, constraints, bounds, covariance):
        return minimize(self.__risk_function, x0,
                        args=(covariance), method='SLSQP',
                        # prints covergence msgs
                        options={'disp': True},
                        constraints=constraints,
                        bounds=bounds)


def get_companies_list(self, current_portfolio=None):
    dfs = pd.read_html(self.__url, header=0)
    first_table = dfs[2]
    company_names = first_table
    return company_names


def get_companies_list(self, current_portfolio=None):
    return pd.DataFrame({'Ticker': companies})


print('Initialised Price Extractor')


def get_prices(self, event, start_date, end_date):
    prices = pd.DataFrame()
    symbols = self.companies['Ticker']
    tmp = {}
    for i in symbols:
        try:
            tmp = web.DataReader(i, self.__api, start_date, end_date)
            print('Fetched prices for: ' + i)
        except:
            print('Issue getting prices for: ' + i)
        else:
            prices[i] = tmp[event]
    return prices


# calculator.py
class RiskReturnCalculator:
    def __init__(self):
        pass

    @staticmethod
    def calculate_assets_expectedreturns(returns):
        return returns.mean() * 252

    @staticmethod
    def calculate_assets_covariance(returns):
        return returns.cov() * 252

    @staticmethod
    def calculate_portfolio_expectedreturns(returns, allocations):
        return sum(returns * allocations)

    @staticmethod
    def calculate_portfolio_risk(allocations, cov):
        return np.sqrt(reduce(np.dot, [allocations, cov, allocations.T]))

    @staticmethod
    def calculate_daily_asset_returns(stock_prices, return_type):
        return np.log(stock_prices / stock_prices.shift(1))


class metrics_calculator:

    @staticmethod
    def calculate_sharpe_ratio(risk, returns, risk_free_rate):
        return (returns - risk_free_rate) / risk

    @staticmethod
    def get_max_sharpe_ratio(df):
        return df.ix[df['SharpeRatio'].astype(float).idxmax()]

    @staticmethod
    def get_min_risk(df):
        return df.ix[df['Risk'].astype(float).idxmin()]


class PortfolioManager:
    def __init__(self):
        pass

    def get_portfolio(self, type):
        df = pd.DataFrame()
        df['Companies'] = []
        return df


# main.py
def generate_optimum_portfolio():
    obj_factory = object_factory(settings)
    ce = obj_factory.get_companies_extractor()
    cp = obj_factory.get_charts_plotter()
    mcs = obj_factory.get_portfolio_generator()
    fr = obj_factory.get_file_repository()
    mc = obj_factory.get_metrics_calculator()
    price_extractor = obj_factory.get_price_extractor(companies)

    print('1. Get companies')
    companies = ce.get_companies_list()

    print('2. Get company stock prices')

    end_date = settings.get_end_date()
    start_date = settings.get_start_date(end_date)
    closing_prices = price_extractor.get_prices(settings.PriceEvent, start_date, end_date)

    # plot stock prices & save data to a file
    cp.plot_prices(closing_prices)
    fr.save_to_file(closing_prices, 'StockPrices')

    print('3. Calculate Daily Returns')
    returns = settings.DailyAssetsReturnsFunction(closing_prices, settings.ReturnType)
    # plot stock prices & save data to a file
    cp.plot_returns(returns)
    fr.save_to_file(returns, 'Returns')

    print('4. Calculate Expected Mean Return & Covariance')
    expected_returns = settings.AssetsExpectedReturnsFunction(returns)
    covariance = settings.AssetsCovarianceFunction(returns)
    # Plot & Save covariance to file
    cp.plot_correlation_matrix(returns)
    fr.save_to_file(covariance, 'Covariances')

    print('5. Use Monte Carlo Simulation')
    # Generate portfolios with allocations
    portfolios_allocations_df = mcs.generate_portfolios(expected_returns, covariance, settings.RiskFreeRate)
    portfolio_risk_return_ratio_df = portfolios_allocation_mapper.map_to_risk_return_ratios(portfolios_allocations_df)

    # Plot portfolios, print max sharpe portfolio & save data
    cp.plot_portfolios(portfolio_risk_return_ratio_df)
    max_sharpe_portfolio = mc.get_max_sharpe_ratio(portfolio_risk_return_ratio_df)['Portfolio']
    max_shape_ratio_allocations = portfolios_allocations_df[['Symbol', max_sharpe_portfolio]]
    print(max_shape_ratio_allocations)
    fr.save_to_file(portfolios_allocations_df, 'MonteCarloPortfolios')
    fr.save_to_file(portfolio_risk_return_ratio_df, 'MonteCarloPortfolioRatios')

    print('6. Use an optimiser')
    # Generate portfolios
    targets = settings.get_my_targets()
    optimiser = obj_factory.get_optimiser(targets, len(expected_returns.index))
    portfolios_allocations_df = optimiser.generate_portfolios(expected_returns, covariance, settings.RiskFreeRate)
    portfolio_risk_return_ratio_df = portfolios_allocation_mapper.map_to_risk_return_ratios(portfolios_allocations_df)

    # plot efficient frontiers
    cp.plot_efficient_frontier(portfolio_risk_return_ratio_df)
    cp.show_plots()

    # save data
    print('7. Saving Data')
    fr.save_to_file(portfolios_allocations_df, 'OptimisationPortfolios')
    fr.close()


generate_optimum_portfolio()
