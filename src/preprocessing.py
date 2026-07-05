"""
preprocessing.py

Functions for loading and preprocessing financial datasets.
"""

import pandas as pd


def load_dataset(path):
    """
    Load a CSV file and prepare it for analysis.
    """

    df = pd.read_csv(path)

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Set Date as index
    df.set_index("Date", inplace=True)

    # Sort chronologically
    df.sort_index(inplace=True)

    return df


def check_missing_values(df):
    """Return missing values."""
    return df.isnull().sum()


def fill_missing_values(df):
    """
    Forward-fill then back-fill missing values.
    """
    df = df.ffill().bfill()
    return df


def descriptive_statistics(df):
    """Return descriptive statistics."""
    return df.describe()


def add_daily_return(df):
    """Calculate daily percentage return."""
    df["Daily Return"] = df["Close"].pct_change()
    return df


def add_rolling_statistics(df, window=30):
    """Calculate rolling mean and volatility."""
    df["Rolling Mean"] = df["Close"].rolling(window).mean()
    df["Rolling Std"] = df["Close"].rolling(window).std()
    return df