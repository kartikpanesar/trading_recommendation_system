import pandas_ta as ta

def  get_strategy(df, position):

    df["RSI"] = ta.rsi(df["Close"], length=14)
    rsi_today = df["RSI"].iloc[-1]
    rsi_yesterday = df["RSI"].iloc[-2]

    if not position:
        if(rsi_yesterday < 35 and rsi_today >=35):
            return 0  #BUY
        else:
            return 1  #Don't BUY

    else:
        if(rsi_yesterday > 65 and rsi_today <= 65):
            return 2  #SELL
        else:
            return 3  #HOLD

