import pandas as pd


def clean_data(df):
    """Cleans the grocery/gas prices DataFrame.

    - Converts 'date' to a datetime type
    - Converts 'item' and 'category' to categorical types
    Returns a new DataFrame (the original is not changed).
    """
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    df['item'] = df['item'].astype('category')
    df['category'] = df['category'].astype('category')
    return df


def time_split(df, cutoff_date):
    """Splits df by date: rows before cutoff_date go to train, the rest to test.

    Run clean_data() first so the 'date' column is a real datetime.
    """
    cutoff = pd.to_datetime(cutoff_date)
    train = df[df['date'] < cutoff]
    test = df[df['date'] >= cutoff]
    return train, test