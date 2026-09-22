import pandas as pd

def read_data_pd(filepath):
    """Reads the grocery/gas prices dataset into a DataFrame."""
    df = pd.read_csv(filepath)
    return df