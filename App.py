import streamlit as st
import yfinance as yf
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

st.set_page_config(layout="wide")

st.title("My Trading Chart")
data = yf.download("^NSEI", period="5d", interval="5m", auto_adjust=False)
data = data.reset_index()
data.columns = data.columns.get_level_values(0)
candles = []

for _, row in data.iterrows():
    candles.append({
    "time": row["Datetime"].strftime("%Y-%m-%d %H:%M:%S"),
    "open": float(row["Open"]),
    "high": float(row["High"]),
    "low": float(row["Low"]),
    "close": float(row["Close"]),
})

chart = [{
    "chart": {
        "height": 600
    },
    "series": [{
        "type": "Candlestick",
        "data": candles          
    }]
}]

renderLightweightCharts(chart, "chart")
