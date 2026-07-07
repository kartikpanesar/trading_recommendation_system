import yfinance as yf 

def get_data(symbol):
    df = yf.download(
            symbol,
            period="3mo",
            interval="1d",
            auto_adjust=False
            )

# flatten columns if multi-index
    if hasattr(df.columns, "droplevel"):
        df.columns = df.columns.droplevel(1)

    return df 

