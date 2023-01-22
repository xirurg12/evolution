# -*- coding: utf-8 -*-
import requests
import apimoex
import pandas as pd
import description


with requests.Session() as session:

    data = apimoex.get_market_candle_borders(session, 'SNGSP')
    df = pd.DataFrame(data)
    print(df)

    data_candel = apimoex.get_market_candles(
        session,
        'SNGSP',
        start="2023-01-20",
        end="2023-01-21",
        interval=10
    )
    print(data_candel)
    df_candle = pd.DataFrame(data_candel)
    df_candle = df_candle.rename(columns={'begin': 'Date'})

    df_candle['Date'] = pd.to_datetime(df_candle['Date'])
    df_candle.set_index('Date')
    print(df_candle)

    finplot.candlestick_ochl(df_candle[['open', 'close', 'high', 'low']])
    finplot.show()
