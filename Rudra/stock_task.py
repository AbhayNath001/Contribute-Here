import time                                                 #pip install python-time
from datetime import datetime, timedelta                    #pip install DateTime
from Speak import Say, Just_Say
import requests
import matplotlib.pyplot as plt

def StockExecution(tag,query):
    if "stock" in tag:
        API_KEY = "NE6NALNKAA4G9HJG"
        print("----------------------------------------")
        print("""Some stock symbols are:
        AAPL: Apple Inc.
        AMZN: Amazon.com Inc.
        GOOGL: Alphabet Inc. (formerly known as Google)
        MSFT: Microsoft Corporation
        FB: Facebook Inc.
        TSLA: Tesla Inc.
        JPM: JPMorgan Chase & Co.
        V: Visa Inc.
        WMT: Walmart Inc.
        NVDA: NVIDIA Corporation.
        DIS: The Walt Disney Company.
        NFLX: Netflix Inc.
        BA: Boeing Co.
        JNJ: Johnson & Johnson.
        GE: General Electric Company.
        BA: Boeing Co.
        NKE: Nike Inc.
        PFE: Pfizer Inc.
        KO: The Coca-Cola Company.
        GM: General Motors Company.
        AMD: Advanced Micro Devices Inc.
        CRM: Salesforce.com Inc.
        PYPL: PayPal Holdings Inc.
        NFLX: Netflix Inc.
        UBER: Uber Technologies Inc.
        VZ: Verizon Communications Inc.
        T: AT&T Inc.
        SBUX: Starbucks Corporation.
        DISCA: Discovery Inc.
        BA: Boeing Co.""")
        print("----------------------------------------\n")
        try:
            symbol = input("Enter the stock symbol: ")
            symbol = symbol.upper()
            start_date = input("Enter the starting date (yyyy-mm-dd): ")
            end_date = input("Enter the ending date (yyyy-mm-dd): ")
            print("Collecting data...")
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&outputsize=full"
            response = requests.get(url)
            data = response.json()
            prices = []
            dates = []
            for date in data["Time Series (Daily)"]:
                if date >= start_date and date <= end_date:
                    prices.append(float(data["Time Series (Daily)"][date]["4. close"]))
                    dates.append(date)
            print(f"Stock symbol: {symbol}")
            print(f"Start date: {start_date}")
            print(f"End date: {end_date}")
            Say(f"Number of trading days: {len(prices)}")
            Say(f"Minimum closing price: {min(prices)} USD on {dates[prices.index(min(prices))]}")
            Say(f"Maximum closing price: {max(prices)} USD on {dates[prices.index(max(prices))]}")
            plt.plot(dates, prices)
            plt.title(f"{symbol} Closing Prices")
            plt.xlabel("Date")
            plt.ylabel("Price(USD)")
            plt.xticks(rotation=90)
            plt.show()
        except:
            Say("Invalid stock symbol or date format")
            
    elif "bitcoin" in tag:
        try:
            str_date = input("Enter the starting date (yyyy-mm-dd): ")
            end_date = input("Enter the ending date (yyyy-mm-dd): ")
            start_date = str_date
            end_date = end_date
            print("collecting...")
            url = f"https://api.coindesk.com/v1/bpi/historical/close.json?start={start_date}&end={end_date}&currency="
            response = requests.get(url + "USD")
            usd_data = response.json()["bpi"]
            response = requests.get(url + "INR")
            inr_data = response.json()["bpi"]
            dates = []
            usd_prices = []
            inr_prices = []
            for date in usd_data:
                dates.append(date)
                usd_prices.append(usd_data[date])
                inr_prices.append(inr_data[date])
            plt.plot(dates, usd_prices, label='USD')
            plt.plot(dates, inr_prices, label='INR')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.title('Bitcoin Prices')
            plt.legend()
            plt.show()
            usd_max_price = max(usd_prices)
            usd_min_price = min(usd_prices)
            inr_max_price = max(inr_prices)
            inr_min_price = min(inr_prices)
            usd_max_date = dates[usd_prices.index(usd_max_price)]
            usd_min_date = dates[usd_prices.index(usd_min_price)]
            inr_max_date = dates[inr_prices.index(inr_max_price)]
            inr_min_date = dates[inr_prices.index(inr_min_price)]
            Say(f"Maximum price of 1 Bitcoin was {usd_max_price} US dollar and {inr_max_price} Indian Rupees on {usd_max_date}")
            Say(f"Minimum price of 1 Bitcoin was {usd_min_price} US dollar and {inr_min_price} Indian Ruppes on {usd_min_date}")
        except:
            Say("Invalid date format")