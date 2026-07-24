import streamlit as st
import yfinance as yf
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts
import streamlit.components.v1 as components

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

#renderLightweightCharts(chart, "chart")
html = """

<div id="tvchart" style="width:100%;height:600px;"></div>

<script src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>

<script>
const chart = LightweightCharts.createChart(
    document.getElementById("tvchart"),
    {
        width: window.innerWidth - 40,
        height: 600,
    }
);

const candleSeries = chart.addCandlestickSeries();

candleSeries.setData([
    { time: "2026-07-21", open: 25000, high: 25100, low: 24950, close: 25080 },
    { time: "2026-07-22", open: 25080, high: 25200, low: 25050, close: 25150 },
    { time: "2026-07-23", open: 25150, high: 25250, low: 25100, close: 25220 }
]);
</script>
"""
components.html(html, height=700)
