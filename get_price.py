import requests
import pandas as pd
res = requests.get('https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1415502567&end=1615702567&period=86400')

df = pd.DataFrame(res.json())
df['date'] = pd.to_datetime(df['date'],unit = 's')
df.to_csv('./bit_price.csv')