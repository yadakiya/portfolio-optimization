"""
data_loader.py

Downloads historical financial data from Yahoo Finance
for TSLA, SPY and BND.
"""

import os
import yfinance as yf


def download_data(ticker, start_date, end_date, save_path):
    """
    Download historical stock data.

    Parameters
    ----------
    ticker : str
        Stock ticker
    start_date : str
    end_date : str
    save_path : str
    """

    print(f"Downloading {ticker}...")

    df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        progress=False
    )

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    df.to_csv(save_path)

    print(f"{ticker} saved successfully.")
    print(df.head())

    return df


if __name__ == "__main__":

    START = "2015-01-01"
    END = "2026-06-30"

    download_data(
        "TSLA",
        START,
        END,
        "data/raw/TSLA.csv"
    )

    download_data(
        "SPY",
        START,
        END,
        "data/raw/SPY.csv"
    )

    download_data(
        "BND",
        START,
        END,
        "data/raw/BND.csv"
    )

    print("All datasets downloaded successfully.")