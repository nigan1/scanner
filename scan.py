from binance.client import Client
import pandas as pd


api_key=''
api_secret=''

client=Client(api_key=api_key, api_secret=api_secret)

pd.set_option("display.max_rows", None, "display.max_columns", None)

monedas=[]


futures_exchange_info = client.futures_ticker()

for element in futures_exchange_info:
    if 'USDT' in element['symbol'] and float(element['quoteVolume'])>200000000.00 and float(element['lastPrice'])<5:
        monedas.append(element)


ticker_dataframe = pd.DataFrame(monedas)
ticker_dataframe=ticker_dataframe[['symbol','lastPrice','quoteVolume']]
ticker_dataframe=ticker_dataframe.sort_values(by='quoteVolume',ascending=True)
ticker_dataframe=ticker_dataframe.reset_index(drop=True)
print(ticker_dataframe)
