import streamlit as st
import yfinance as yf
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

st.set_page_config(layout="wide")

st.title("My Trading Chart")
data = yf.download("^NSEI", period="5d", interval="5m", auto_adjust=False)
data = data.reset_index()
candles = []

for i in data.index:
    candles.append({
        "time": i.strftime("%Y-%m-%d %H:%M:%S"),
        "open": float(data.loc[i]["Open"]),
        "high": float(data.loc[i]["High"]),
        "low": float(data.loc[i]["Low"]),
        "close": float(data.loc[i]["Close"]),
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
