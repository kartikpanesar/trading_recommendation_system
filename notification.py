
def notify(symbol, signal, date):
    s = "s"
    if (signal==0):
        s = "BUY"
    elif(signal == 1):
        s = "DON'T BUY"
    elif(signal == 2):
        s = "SELL"
    elif(signal==3):
        s = "HOLD"
    else:
        s = "ERROR OCURRED"


    with open("recommendation.txt", "a") as file:
        file.write(f"{symbol}\n")
        file.write(f"{s}\n")
        file.write(f"{date}\n")
        file.write("\n")




