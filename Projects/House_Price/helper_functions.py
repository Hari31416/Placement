def get_detail(column):
    """Prints the details of a column

    Attributes:
    -----------
        column (str): the column name

    Returns:
    --------
        None
    """

    text = ""
    with open("data_description.txt") as f:
        text = f.read()

    try:
        start = text.find(f"{column}:")
        end = text.find(":", start + len(column) + 5)
        texts_found = text[start:end].strip().split("\n")
        print("\n".join(texts_found[:-2]))
    except:
        print("No such column")


def percentage_none(column, df):
    """
    Calculate the percentage of missing values in a column

    Attributes:
    -----------
        column (str): the column name
        df (pandas.DataFrame): the dataframe to calculate the percentage of missing values

    Returns:
    --------
        float: the percentage of missing values in the column
            Default: train
    """
    none_rows = df[column].isnull().sum()
    return none_rows / len(df)


def fill_na_for_none(column, dfs=[train, test]):
    """Fills NA with 'None' for the column

    Attributes:
    -----------
        column (str): the column name
        dfs (list): the dataframes to fill the NA with 'None'

    Returns:
    --------
        None
    """
    print("Filling NaN for {}".format(column))
    print("Percenatge of NA before...")
    for df in dfs:
        print(percentage_none(column, df))
        df[column].fillna("None", inplace=True)

    print("Percentage of NA after...")
    for df in dfs:
        print(percentage_none(column, df))
