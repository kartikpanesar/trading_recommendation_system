
def  get_strategy(df, position):

    l = 20
    s = 10

    l_avg = df["Close"].tail(l).mean()
    s_avg = df["Close"].tail(s).mean()

    if not position:
        if(s_avg < l_avg):
            return 0  #BUY
        else:
            return 1  #Don't BUY

    else:
        if(s_avg > l_avg):
            return 2  #SELL
        else:
            return 3  #HOLD



