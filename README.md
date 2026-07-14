# Trading Recommendation System

A Python tool that scans a watchlist of NSE-listed stocks and generates **BUY / SELL / HOLD / DON'T BUY** signals based on a technical indicator strategy, tracking position state across runs.

## How It Works

1. **Data fetch** — For each symbol in the watchlist, recent daily price history (3 months) is pulled via `yfinance`.
2. **Signal generation** — The active strategy computes a 14-period RSI (via `pandas_ta`) and checks for threshold crossovers:
   - If **not currently holding** the stock: a **BUY** signal fires when RSI crosses **up through 35** (recovering from oversold).
   - If **currently holding** the stock: a **SELL** signal fires when RSI crosses **down through 65** (falling from overbought).
   - Otherwise, the signal is **DON'T BUY** or **HOLD**, depending on position state.
3. **Position tracking** — `watchlist.json` stores a `true`/`false` flag per symbol representing whether a position is currently held. This is updated automatically after each run based on the signal generated.
4. **Output** — Each recommendation (symbol, signal, date) is appended to `recommendation.txt`.


## Project Structure

```
├── main.py              # Entry point — loops through watchlist, fetches data, generates signals
├── data.py               # Fetches historical price data via yfinance
├── strategy_rsi.py       # RSI-based signal logic (currently active strategy)
├── strategy.py           # SMA crossover-based signal logic (alternate strategy)
├── notification.py       # Writes signal output to recommendation.txt
├── config.py             # Basic configuration (e.g. capital)
├── watchlist.json        # Tracked symbols and their current position state
└── recommendation.txt    # Generated log of buy/sell/hold recommendations
```

## Requirements

- Python 3.8+
- [yfinance](https://pypi.org/project/yfinance/)
- [pandas](https://pypi.org/project/pandas/)
- [pandas-ta](https://pypi.org/project/pandas-ta/)

Install dependencies:

```bash
pip install yfinance pandas pandas-ta
```

## Usage

1. Add or remove symbols in `watchlist.json` (NSE tickers use the `.NS` suffix, e.g. `"RELIANCE.NS": false`). Set the value to `false` if you don't currently hold a position, or `true` if you do.
2. Run the script:

```bash
python main.py
```

3. Check `recommendation.txt` for the generated signals. `watchlist.json` is updated in place to reflect any position changes triggered by BUY/SELL signals.

## Sample Output (`recommendation.txt`)

```
RELIANCE.NS
BUY
2026-07-10

TCS.NS
HOLD
2026-07-10
```

## Limitations & Disclaimer

- This is a learning project exploring rules-based technical signal generation and is **not intended for real trading decisions**.
- The RSI thresholds (35/65) and lookback period (14) are fixed and not optimized or validated against out-of-sample data.
- No transaction costs, slippage, or risk management (position sizing, stop-loss) are modeled.
- Past signal performance does not guarantee future results.

## Possible Improvements

- Backtest the RSI strategy against historical data to evaluate performance before further use.
- Add configurable strategy parameters (RSI thresholds, moving average windows) via `config.py`.
- Support multiple strategies running in parallel with signal comparison.
- Add automated scheduling (e.g. cron) to run daily after market close.
