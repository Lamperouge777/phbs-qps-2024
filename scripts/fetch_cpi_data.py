import pandas_datareader as pdr
from datetime import datetime, timedelta


def fetch_us_cpi_data():

    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    cpi_data = pdr.get_data_fred('CPIAUCSL', start_date, end_date)

    last_four_quarters = cpi_data.tail(4)

    return last_four_quarters


def calculate_inflation_rate(cpi_data):

    inflation_rates = cpi_data.pct_change() * 100

    return inflation_rates


if __name__ == "__main__":
    cpi_data = fetch_us_cpi_data()
    inflation_rates = calculate_inflation_rate(cpi_data)
    print(inflation_rates)
