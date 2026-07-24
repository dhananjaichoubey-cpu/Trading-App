import streamlit as st
import yfinance as yf
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

st.set_page_config(layout="wide")

st.title("My Trading Chart")
tf = st.radio(
    "Timeframe",
    ["1m", "5m", "15m", "30m", "1h", "1d"],
    horizontal=True
)
interval_map = {
    "1m": "1m",
    "5m": "5m",
    "15m": "15m",
    "30m": "30m",
    "1h": "60m",
    "1d": "1d"
}

interval = interval_map[tf]
data = yf.download("^NSEI", period="5d", interval=interval, auto_adjust=False)
data = data.reset_index()
data.columns = data.columns.get_level_values(0)
candles = []

for _, row in data.iterrows():
    candles.append({
    "time": int(row[data.columns[0]].timestamp()),
    "open": float(row["Open"]),
    "high": float(row["High"]),
    "low": float(row["Low"]),
    "close": float(row["Close"]),
})

chart = [{
    "chart": {
        "height": 600,
        "timeScale": {
            "timeVisible": True,
            "secondsVisible": False
        }
    },
    "series": [{
        "type": "Candlestick",
        "data": candles
    }]
}]

renderLightweightCharts(chart, "chart")
