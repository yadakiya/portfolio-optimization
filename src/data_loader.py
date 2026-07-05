import os
import yfinance as yf


def download_data(ticker, start_date, end_date, save_path):

    print(f"Downloading {ticker}...")

    df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=False,
        progress=False,
        group_by="column"
    )

    # Flatten MultiIndex columns if necessary
    if hasattr(df.columns, "levels"):
        df.columns = df.columns.get_level_values(0)

    # Make Date a normal column
    df.reset_index(inplace=True)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    df.to_csv(save_path, index=False)

    print(df.head())

    return df


if __name__ == "__main__":

    START = "2015-01-01"
    END = "2026-06-30"

    download_data("TSLA", START, END, "data/raw/TSLA.csv")
    download_data("SPY", START, END, "data/raw/SPY.csv")
    download_data("BND", START, END, "data/raw/BND.csv")

    print("Done.")