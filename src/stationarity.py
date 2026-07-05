from statsmodels.tsa.stattools import adfuller


def adf_test(series):

    result = adfuller(series.dropna())

    print("ADF Statistic :", result[0])

    print("P-value :", result[1])

    print()

    print("Critical Values")

    for key, value in result[4].items():

        print(key, value)

    if result[1] < 0.05:

        print("\nSeries is Stationary")

    else:

        print("\nSeries is NOT Stationary")