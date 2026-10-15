import pandas as pd


def remove_missing_values(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Return a copy of the dataframe without missing rows."""
    return df.dropna().copy()