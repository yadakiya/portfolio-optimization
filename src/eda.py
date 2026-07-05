"""
Exploratory Data Analysis functions
"""

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")


def plot_close(df, ticker):

    plt.figure(figsize=(15,6))

    plt.plot(df.index, df["Close"], linewidth=2)

    plt.title(f"{ticker} Closing Price")

    plt.xlabel("Date")

    plt.ylabel("Price ($)")

    plt.grid(True)

    plt.show()


def plot_returns(df, ticker):

    plt.figure(figsize=(15,6))

    plt.plot(df.index, df["Daily Return"])

    plt.title(f"{ticker} Daily Returns")

    plt.grid(True)

    plt.show()


def plot_rolling(df, ticker):

    plt.figure(figsize=(15,6))

    plt.plot(df["Close"], label="Close")

    plt.plot(df["Rolling Mean"], label="30-Day Mean")

    plt.plot(df["Rolling Std"], label="30-Day Std")

    plt.legend()

    plt.title(f"{ticker} Rolling Statistics")

    plt.grid(True)

    plt.show()


def boxplot_returns(df, ticker):

    plt.figure(figsize=(8,5))

    sns.boxplot(y=df["Daily Return"])

    plt.title(f"{ticker} Daily Return Outliers")

    plt.show()