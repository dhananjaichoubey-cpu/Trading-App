import streamlit as st
import yfinance as yf
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

st.set_page_config(layout="wide")

st.title("My Trading Chart")

chart = [{
    "chart": {
        "height": 600
    },
    "series": [{
        "type": "Candlestick",
        "data": [
            {"time": "2026-07-21", "open": 25000, "high": 25100, "low": 24950, "close": 25080},
            {"time": "2026-07-22", "open": 25080, "high": 25200, "low": 25050, "close": 25150},
            {"time": "2026-07-23", "open": 25150, "high": 25250, "low": 25100, "close": 25220}
        ]
    }]
}]

renderLightweightCharts(chart, "chart")
