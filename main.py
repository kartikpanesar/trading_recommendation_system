from data import get_data
from strategy_rsi import get_strategy
from notification import notify
import json

with open("watchlist.json", "r") as f:
    watchlist = json.load(f)

with open("recommendation.txt" , "w") as file:
    pass

for symbol, position in watchlist.items():
    df = get_data(symbol)
    signal = get_strategy(df, position)
    date = df.index[-1].date()

    if signal == 0:
        watchlist[symbol] = True
    
    elif signal == 3:
        watchlist[symbol] = False

    notify(symbol, signal, date)

with open("watchlist.json", "w") as f:
    json.dump(watchlist, f, indent=4)
