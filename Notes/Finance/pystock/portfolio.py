import pandas as pd
import datetime
from tabulate import tabulate
from pystock.utils import *
from pystock.exceptions import *

FREQUENCY = {
    "D": "Daily",
    "W": "Weekly",
    "M": "Monthly",
    "Q": "Quarterly",
    "Y": "Yearly",
}


class Stock:
    """
    A class to represent a stock.
    Have methods to load data from a csv file and calculate the return of the stock.
    """

    def __init__(self, name, directory) -> None:
        self.name = name
        self.directory = directory
        self.loaded = False
        self.return_ = {}

    def __str__(self) -> str:
        return f"Stock name: {self.name}"

    def __repr__(self) -> str:
        return f"Stock(name={self.name})"

    def __eq__(self, o: object) -> bool:
        """
        Checks if two stocks are equal. Two stocks are equal if they have the same name.
        """
        if isinstance(o, Stock):
            return self.name == o.name
        return False

    def freq_return(self, frequency="D", mean=True, column="Close"):
        """
        Calculates the return of the stock for a given frequency

        Parameters
        ----------
        frequency : str, optional
            Frequency of the data, by default "D"
        mean : bool, optional
            Whether to return the mean of the return, by default True
        column : str, optional
            Column to calculate the return, by default "Close"

        Returns
        -------
        float
            Return of the stock
        """
        freq_data = self.data.asfreq(frequency, method="ffill").dropna()
        return_ = freq_data[column].pct_change()
        return_ = return_.dropna()
        if mean:
            self.return_[frequency] = return_.mean()
        else:
            self.return_[frequency] = return_
        return self.return_[frequency]

    def _convert_str_to_date(self, string, format="%Y-%m-%d"):
        """
        Convert string to date

        Parameters
        ----------
        string : str
            String to convert
        format : str, optional
            Format of the string, by default "%Y-%m-%d"

        Returns
        -------
        datetime.date
            Date
        """
        if isinstance(string, datetime.date):
            return string
        if not string:
            return None
        return datetime.datetime.strptime(string, format)

    def load_data(
        self,
        start_date=None,
        end_date=None,
        columns=None,
        frequency="D",
        rename_cols=None,
    ):
        """
        Read data from a csv file and return a dataframe.
        Assumes that the dataframe has column `Date` containing dates.

        Parameters
        ----------
        start_date : str, optional
            Start date of the data, by default None
        end_date : str, optional
            End date of the data, by default None
        columns : list, optional
            Columns to keep, by default None which means keep all columns
        frequency : str, optional
            Frequency of the data, by default "D"
        rename_cols : list, optional
            Columns to rename, by default None

        Returns
        -------
        pd.DataFrame
        """
        df = pd.read_csv(self.directory, parse_dates=["Date"], index_col="Date")

        df.sort_index(inplace=True)
        smallest_date = df.index[0]
        largest_date = df.index[-1]
        start_date = self._convert_str_to_date(start_date)
        end_date = self._convert_str_to_date(end_date)

        if start_date and start_date < smallest_date:
            raise StockException(
                "Start date is before the data starts. If you don't want to specify a start date, set it to None."
            )

        if end_date and end_date > largest_date:
            raise StockException(
                "End date is after the data ends. If you don't want to specify an end date, set it to None."
            )

        if not start_date:
            start_date = df.index[0]
        if not end_date:
            end_date = df.index[-1]
        date_range = (start_date, end_date)
        df = df[(df.index >= date_range[0]) & (df.index <= date_range[1])]
        if columns:
            try:
                df = df[columns]
            except KeyError:
                raise KeyError("Column not found. Please check the column names.")
        if rename_cols:
            try:
                df.columns = rename_cols
            except ValueError:
                raise ValueError(
                    "Number of columns to rename does not match the number of columns."
                )
        df = df.asfreq(frequency, "ffill").dropna()
        self.data = df
        self.columns = df.columns
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency
        self.loaded = True
        return df

    def change_frequency(self, frequency):
        """
        Changes the frequency of the data.

        Parameters
        ----------
        frequency : str
            Frequency of the data
        """
        self.frequency = frequency
        self.data = self.data.asfreq(frequency, "ffill").dropna()


class Portfolio:
    """
    Class for a portfolio of stocks. Contains a benchmark and a list of stocks.
    The class provides some useful methods for calculating the return of the portfolio.
    """

    def __init__(
        self,
        benchmark_dir,
        benchmark_name,
        stock_dirs=None,
        stock_names=None,
        weights="equal",
    ) -> None:
        self.benchmark_dir = benchmark_dir
        self.stock_dirs = stock_dirs
        self.benchmark_name = benchmark_name
        self.stock_names = stock_names
        self.benchmark = Stock(self.benchmark_name, self.benchmark_dir)
        self._create_stock_objects_()
        self.weights = self.set_weights(weights)

    def __str__(self) -> str:
        if not self.stocks:
            return f"Portfolio with benchmark {self.benchmark_name}"
        return f"Portfolio with benchmark {self.benchmark_name} and stocks {self.stock_names}"

    def __iter__(self):
        """
        Iterates over the stocks in the portfolio. Yields the stock object and the name of the stock.

        Yields
        ------
        Stock, str
            Stock object and name of the stock
        """
        all_stocks = [self.benchmark] + self.stocks
        all_names = [self.benchmark_name] + self.stock_names
        for stock, name in zip(all_stocks, all_names):
            yield stock, name

    def __contains__(self, stock_name):
        """
        Makes easy to use the `in` operator to check if a stock is in the portfolio. Works with the name of the stock or the stock object.
        """
        if isinstance(stock_name, Stock):
            stock_name = stock_name.name

        if stock_name == self.benchmark_name:
            return True
        return stock_name in self.stock_names

    def __getitem__(self, stock_name):
        """
        Used for easy access to the stocks in the portfolio. Name of the stock can be used as an index.
        """
        if stock_name == self.benchmark_name:
            return self.benchmark
        return self.stocks[self.stock_names.index(stock_name)]

    def __len__(self):
        """
        Number of stocks in the portfolio. Includes the benchmark.
        """
        return len(self.stocks) + 1

    def _return_of_stocks(self, column="Close", frequency="M"):
        """
        Calculates the returns of the stocks in the portfolio

        Parameters
        ----------
        column : str, optional
            Column to calculate the returns of, by default "Close"
        frequency : str, optional
            Frequency of the data, by default "M"

        Returns
        -------
        pd.DataFrame
            Returns of the stocks
        """
        df = pd.DataFrame()
        for stock, name in zip(self.stocks, self.stock_names):
            df[name] = stock.data[column].pct_change(freq=frequency).dropna()
        return df

    def get_cov_matrix(self, column="Close", frequency="M"):
        """
        Calculates the covariance matrix of the stocks in the portfolio

        Parameters
        ----------
        column : str, optional
            Column to calculate the covariance matrix of, by default "Close"
        frequency : str, optional
            Frequency of the data, by default "M"

        Returns
        -------
        pd.DataFrame
            Covariance matrix
        """
        temp_df = self._return_of_stocks(column=column, frequency=frequency)
        return temp_df.cov()

    def set_weights(self, weights="equal"):
        """
        Creates weights for the stocks

        Parameters
        ----------
        weights : str or list or np.ndarray, optional
            Type of weights to create, by default "equal"

        Returns
        ------
        np.ndarray
            Weights of the stocks
        """
        if isinstance(weights, str):
            return create_weight(len(self.stocks), weight_type=weights)
        elif isinstance(weights, list):
            return np.array(weights)
        elif isinstance(weights, np.ndarray):
            return weights

    def _create_stock_objects_(self):
        """
        Creates stock objects

        Raises
        ------
        ValueError
            If the number of stock directories and stock names are not the same

        AssertionError
            If there are no stock directories or stock names

        Returns
        -------
        None
        """
        if not self.stock_dirs:
            self.stock_dirs = []
            self.stock_names = []
            self.stocks = []
            self.wights = []

        if self.stock_names and len(self.stock_dirs) != len(self.stock_names):
            raise ValueError(
                "Number of stock directories and stock names are not the same.\nPass None to stock_names if you don't want to specify stock names."
            )
        if not self.stock_names:
            self.stock_names = [f"df{i+1}" for i in range(len(self.stock_dirs))]

        assert self.stock_dirs, "There must be at least one stock_dir"
        assert self.stock_names, "There must be some stock name"
        self.stocks = []
        for i, stock_dir in enumerate(self.stock_dirs):
            stock_name = self.stock_names[i]
            stock = Stock(stock_name, stock_dir)
            self.stocks.append(stock)

    def load_benchmark(
        self,
        start_date=None,
        end_date=None,
        columns=None,
        frequency="D",
        rename_cols=None,
    ):
        """
        Load benchmark data

        Parameters
        ----------
        start_date : str, optional
            Start date, by default None
        end_date : str, optional
            End date, by default None
        columns : list, optional
            Columns to keep, by default None
        frequency : str, optional
            Frequency of the data, by default "D"
        rename_cols : list, optional
            Columns to rename, by default None

        Returns
        -------
        pd.DataFrame
            Benchmark data
        """
        self.benchmark.load_data(
            start_date=start_date,
            end_date=end_date,
            columns=columns,
            frequency=frequency,
            rename_cols=rename_cols,
        )

    def change_benchmark(
        self,
        benchmark_dir,
        benchmark_name,
        load=True,
        use_prev=True,
        start_date=None,
        end_date=None,
        columns=None,
        frequency="D",
        rename_cols=None,
    ):
        """
        Change benchmark

        Parameters
        ----------
        benchmark_dir : str
            Directory of the benchmark
        benchmark_name : str
            Name of the benchmark
        load : bool, optional
            Load the data, by default True
        use_prev : bool, optional
            Use the values of start_date, end_date, columns, frequency, rename_cols from the previous benchmark, by default True
        start_date : str, optional
            Start date, by default None
        end_date : str, optional
            End date, by default None
        columns : list, optional
            Columns to keep, by default None
        frequency : str, optional
            Frequency of the data, by default "D"
        rename_cols : list, optional
            Columns to rename, by default None

        Returns
        -------
        None
        """
        self.benchmark_dir = benchmark_dir
        self.benchmark_name = benchmark_name
        if use_prev:
            if not start_date:
                start_date = self.benchmark.start_date
            if not end_date:
                end_date = self.benchmark.end_date
            if not columns:
                columns = self.benchmark.columns
            if not rename_cols:
                rename_cols = self.benchmark.columns
            if not freq:
                freq = self.benchmark.frequency
        self.benchmark = Stock(self.benchmark_name, self.benchmark_dir)
        if load:
            self.benchmark.load_data(
                start_date=start_date,
                end_date=end_date,
                columns=columns,
                frequency=frequency,
                rename_cols=rename_cols,
            )

    def load_one_stock(
        self,
        name,
        start_date=None,
        end_date=None,
        columns=None,
        frequency="D",
        rename_cols=None,
        overwrite=False,
    ):
        """
        Loads one stock data and returns it

        Parameters
        ----------
        name: str
            Name of the stock
        start_date : str, optional
            Start date, by default None
        end_date : str, optional
            End date, by default None
        columns : list, optional
            Columns to keep, by default None
        freq : str, optional
            Frequency of the data, by default "D"
        rename_cols : list, optional
            Columns to rename, by default None
        overwrite : bool, optional
            Overwrite the data, by default False

        Returns
        -------
        pd.DataFrame
            Stock data
        """
        if not self.stocks:
            raise ValueError("The stock list is empty")
        for stock in self.stocks:
            if stock.name == name:
                if stock.loaded and not overwrite:
                    return stock.data
                else:
                    stock.load_data(
                        start_date=start_date,
                        end_date=end_date,
                        columns=columns,
                        frequency=frequency,
                        rename_cols=rename_cols,
                    )
                    return stock.data

    def load_all(
        self,
        start_date=None,
        end_date=None,
        columns=None,
        frequency="D",
        rename_cols=None,
        overwrite=False,
    ):
        """
        Load stock data

        Parameters
        ----------
        start_date : str, optional
            Start date, by default None
        end_date : str, optional
            End date, by default None
        columns : list, optional
            Columns to keep, by default None
        frequency : str, optional
            Frequency of the data, by default "D"
        rename_cols : list, optional
            Columns to rename, by default None
        overwrite : bool, optional
            Overwrite existing data, by default False

        Returns
        -------
        pd.DataFrame
            Stock data
        """
        for stock in self.stocks:

            if stock.loaded and not overwrite:
                continue
            stock.load_data(
                start_date=start_date,
                end_date=end_date,
                columns=columns,
                frequency=frequency,
                rename_cols=rename_cols,
            )

    def add_stocks(
        self,
        stock_dirs,
        stock_names=None,
        load_data=True,
        start_date=None,
        end_date=None,
        columns=None,
        frequency="D",
        rename_cols=None,
        overwrite=False,
    ):
        """
        Add a stock to the list of stocks

        Parameters
        ----------
        stock_dirs : list
            List of stock directories
        stock_names : list, optional
            List of stock names, by default None
        load_data : bool, optional
            Whether to load the data, by default True
        start_date : str, optional
            Start date, by default None
        end_date : str, optional
            End date, by default None
        columns : list, optional
            Columns to keep, by default None
        frequency : str, optional
            Frequency of the data, by default "D"
        rename_cols : list, optional
            Columns to rename, by default None
        overwrite : bool, optional
            Whether to overwrite existing stocks, by default False

        Returns
        -------
        stocks : list
            List of stocks
        """
        if not stock_names:
            stock_names = [
                f"df{i+1}"
                for i in range(len(self.stocks), len(self.stocks) + len(stock_dirs))
            ]
        if len(stock_dirs) != len(stock_names):
            raise ValueError(
                "Number of stock directories and stock names are not the same.\nPass None to stock_names if you don't want to specify stock names."
            )

        for stock_dir, stock_name in zip(stock_dirs, stock_names):
            stock = Stock(stock_name, stock_dir)
            if stock in self.stocks:
                print(f"Stock {stock_name} already exists")
                if overwrite:
                    print("Overwriting...")
                    self.remove_stocks([stock_name])
                else:
                    print("You have not specified overwrite=True. Skipping...")
                    continue
            self.stocks.append(stock)
            if load_data:
                stock.load_data(
                    start_date=start_date,
                    end_date=end_date,
                    columns=columns,
                    frequency=frequency,
                    rename_cols=rename_cols,
                )
        self.stock_names.extend(stock_names)
        self.stock_dirs.extend(stock_dirs)
        self.weights = self.set_weights()
        return self.stocks

    def remove_stocks(self, names):
        """
        Remove a stock from the list of stocks

        Parameters
        ----------
        stock_name : str
            Name of the stock
        """
        ids = []
        for name in names:
            if name in self.stock_names:
                ids.append(self.stock_names.index(name))
        for id_ in ids:
            self.stock_names.pop(id_)
            self.stock_dirs.pop(id_)
            self.stocks.pop(id_)
        self.weights = self.set_weights()

    def change_benchmark_frequency(self, frequency, change_stocks=True):
        """
        Change the frequency of the benchmark data

        Parameters
        ----------
        frequency : str
            Frequency of the data
        change_stocks : bool, optional
            Whether to change the frequency of the stock data, by default True

        Returns
        -------
        None
        """
        self.benchmark.change_frequency(frequency)
        if change_stocks:
            for stock in self.stocks:
                stock.change_frequency(frequency)

    def all_stocks(self):
        """
        Get all the stock data and names

        Returns
        -------
        tuple
            A tuple of List of stock data and name
        """
        data = []
        names = []
        for stock, name in self:
            data.append(stock.data)
            names.append(name)
        return data, names

    def _merge_stocks(self, stocks, names=None, how="inner"):
        """
        Merges a number of the stock data

        Parameters
        ----------
        stocks : list
            List of stock data
        names : list, optional
            List of stock names, by default None. If None, the names will be df1, df2, etc.
        how : str, optional
            How to merge the data, by default "inner"

        Returns
        -------
        pd.DataFrame
            Merged data
        """
        merged_df = merge_dfs(stocks, df_names=names, join=how)
        return merged_df

    def benchmark_return(self, frequency="D", column="Close"):
        """
        Get the benchmark return

        Parameters
        ----------
        freq : str, optional
            Frequency of the return, by default "D"
        column : str, optional
            Column to calculate the return, by default "Close"

        Returns
        -------
        pd.DataFrame
            Benchmark return
        """
        return self.benchmark.freq_return(frequency=frequency, column=column)

    def merge_all(self):
        """
        Merge all the stock data

        Returns
        -------
        pd.DataFrame
            Merged data
        """
        data, names = self.all_stocks()
        return self._merge_stocks(data, names)

    def merge_stock_with_benchmark(self, name, how="inner"):
        """
        Merge the stock data with the benchmark data

        Parameters
        ----------
        name: str
            Name of the stock
        how : str, optional
            How to merge the data, by default "inner"

        Returns
        -------
        pd.DataFrame
            Merged data
        """
        try:
            data = [self.benchmark.data, self[name].data]
            names = [self.benchmark.name, name]
            return self._merge_stocks(data, names, how)
        except KeyError:
            raise StockException(f"Stock {name} not found")

    def __stock_params_prepare(self, name, how="inner", frequency="M", column="Close"):
        """
        Get the stock data and the benchmark data

        Parameters
        ----------
        name : str
            Name of the stock
        how : str, optional
            How to merge the data, by default "inner"
        frequency : str, optional
            Frequency of the data, by default "M"
        column : str, optional
            Column to use, by default "Close"

        Returns
        -------
        pd.DataFrame
            Stock data
        pd.DataFrame
            Benchmark data
        """
        try:
            stock = self[name]
        except KeyError:
            raise StockException(f"Stock {name} not found")

        if column not in stock.data.columns:
            raise StockException(f"Column {column} not found in {name}")

        if frequency != self.benchmark.frequency:
            self.change_benchmark_frequency(frequency)
        dfs_temp = self.merge_stock_with_benchmark(name, how)

        dfs = dfs_temp[[f"{name}_{column}", f"{self.benchmark.name}_{column}"]]
        dfs = dfs.pct_change().dropna()
        assert dfs.shape[0] > 0, "No data found"
        assert (
            dfs.shape[1] == 2
        ), f"Number of colmuns {dfs.shape[1]}, Data not merged properly."

        return dfs

    def get_stock_params(self, name, how="inner", frequency="M", column="Close"):
        """
        Get the stock data and the benchmark data

        Parameters
        ----------
        name : str
            Name of the stock
        how : str, optional
            How to merge the data, by default "inner"
        frequency : str, optional
            Frequency of the data, by default "M"
        column : str, optional
            Column of the data, by default "Close"

        Returns
        -------
        pd.DataFrame
            Stock data
        pd.DataFrame
            Benchmark data
        """
        dfs = self.__stock_params_prepare(name, how, frequency, column)
        y = dfs[f"{name}_{column}"]
        x = dfs[f"{self.benchmark.name}_{column}"]

        variance = x.var()
        covariance = x.cov(y)
        x_mean = x.mean()
        y_mean = y.mean()

        beta = covariance / variance
        alpha = y_mean - beta * x_mean
        self[name].alpha = alpha
        self[name].beta = beta
        return alpha, beta

    def get_all_stock_params(
        self, how="inner", frequency="M", column="Close", return_dict=False
    ):
        """
        Get the stock data and the benchmark data

        Parameters
        ----------
        how : str, optional
            How to merge the data, by default "inner"
        frequency : str, optional
            Frequency of the data, by default "M"
        column : str, optional
            Column to use, by default "Close"
        return_dict : bool, optional
            Return a dictionary instead of a dataframe, by default False

        Returns
        -------
        pd.DataFrame
            Stock data
        pd.DataFrame
            Benchmark data
        """
        alphas = []
        betas = []
        for name in self.stock_names:
            alpha, beta = self.get_stock_params(name, how, frequency, column)
            alphas.append(alpha)
            betas.append(beta)
        result_dict = {
            "Stock": self.stock_names,
            "Alpha": alphas,
            "Beta": betas,
        }
        self.betas = betas
        self.alphas = alphas
        if return_dict:
            return result_dict
        return pd.DataFrame(result_dict)

    def get_stock_return(self, name, frequency="M", column="Close"):
        """
        Get the stock returns

        Parameters
        ----------
        name : str
            Name of the stock
        frequency : str, optional
            Frequency of the data, by default "M"
        column : str, optional
            Column to use, by default "Close"

        Returns
        -------
        pd.DataFrame
            Stock returns
        """
        stock = self[name]
        if column not in stock.data.columns:
            raise StockException(f"Column {column} not found in {name}")

        return_ = stock.freq_return(frequency=frequency, column=column, mean=False)
        volatility = return_.std()
        return_ = return_.mean()
        return return_, volatility

    def get_all_stock_returns(self, frequency="M", column="Close"):
        """
        Get the stock returns

        Parameters
        ----------
        frequency : str, optional
            Frequency of the data, by default "M"
        column : str, optional
            Column to use, by default "Close"

        Returns
        -------
        pd.DataFrame
            Stock returns
        """
        returns = []
        volatilities = []
        for name in self.stock_names:
            return_, volatility = self.get_stock_return(name, frequency, column)
            returns.append(return_)
            volatilities.append(volatility)
        col_name = [
            f"{FREQUENCY[frequency]}_Mean_Return",
            f"{FREQUENCY[frequency]}_Return_STD",
        ]

        result_dict = {
            "Stock": self.stock_names,
            col_name[0]: returns,
            col_name[1]: volatilities,
        }

        return pd.DataFrame(result_dict)

    def portfolio_return(self, frequency="M", column="Close", weights="equal"):
        """
        Get the portfolio return

        Parameters
        ----------
        frequency : str, optional
            Frequency of the data, by default "M"
        column : str, optional
            Column to use, by default "Close"
        weights : list
            List of weights
        Returns
        -------
        float
            Portfolio return
        """
        weights = self.set_weights(weights=weights)
        df = self.get_all_stock_returns(frequency, column)
        returns = df.iloc[:, 1].values
        volatility = df.iloc[:, 2].values
        return_ = np.dot(weights, returns)
        volatility = np.sqrt(np.dot(weights.T, np.dot(np.diag(volatility), weights)))

        return return_, volatility

    def summary(self, frequency="M", column="Close", weights="equal"):
        """
        Get the portfolio return

        Parameters
        ----------
        frequency : str, optional
            Frequency of the data, by default "M"
        column : str, optional
            Column to use, by default "Close"
        weights : list
            List of weights
        Returns
        -------
        float
            Portfolio return
        """
        self.cov_matrix = self.get_cov_matrix(frequency=frequency, column=column)
        stock_summary = self.get_all_stock_returns(frequency, column)
        num_stocks = len(self.stocks)
        weights = self.set_weights(weights=weights)
        assert (
            len(weights) == num_stocks
        ), f"Number of weights {len(weights)} not equal to number of stocks {num_stocks}"

        portfolio_return, portfoio_volatility = self.portfolio_return(
            weights=weights, frequency=frequency, column=column
        )
        params = self.get_all_stock_params(
            return_dict=True, frequency=frequency, column=column
        )
        stock_summary["Alpha"] = params["Alpha"]
        stock_summary["Beta"] = params["Beta"]
        stock_summary["Weight"] = weights

        print("Portfolio Summary")
        print("*****************\n")
        print(str(self))
        print("Here are the summary of stocks in the portfolio")
        print(tabulate(stock_summary, headers="keys", tablefmt="psql"))
        print("The covariance matrix is as follows")
        print(tabulate(self.cov_matrix, headers="keys", tablefmt="psql"))
        print(f"Portfolio Return: {portfolio_return}")
        print(f"Portfolio Volatility: {portfoio_volatility}")
