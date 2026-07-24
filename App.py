import streamlit as st

# Page Configuration for Mobile
st.set_page_config(page_title="Pro Trading Terminal", layout="wide")

# Custom CSS for dark theme look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #ffffff; text-align: center; font-size: 22px; }
    </style>
""", unsafe_allow_html=True)

st.title("📈 Pro Trading Terminal")

# 1. Index Selector (Nifty & Bank Nifty only)
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    selected_index = st.selectbox(
        "Select Index", 
        ["NIFTY 50", "BANK NIFTY"],
        index=0
    )

# Map selection to TradingView symbols
symbol_map = {
    "NIFTY 50": "NSE:NIFTY",
    "BANK NIFTY": "NSE:BANKNIFTY"
}
current_symbol = symbol_map[selected_index]

# 2. TradingView Live Chart Widget
tv_widget_html = f"""
<!DOCTYPE html>
<html>
<head>
</head>
<body style="margin:0;background-color:#131722;">
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container" style="height:600px;width:100%">
      <div class="tradingview-widget-container__widget" style="height:calc(100% - 32px);width:100%"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
      {{
        "autosize": true,
        "symbol": "{current_symbol}",
        "interval": "5",
        "timezone": "Asia/Kolkata",
        "theme": "dark",
        "style": "1",
        "locale": "in",
        "enable_publishing": false,
        "withdateranges": true,
        "hide_side_toolbar": false,
        "allow_symbol_change": false,
        "details": false,
        "hotlist": false,
        "calendar": false,
        "support_host": "https://www.tradingview.com"
      }}
      </script>
    </div>
    <!-- TradingView Widget END -->
</body>
</html>
"""

import streamlit.components.v1 as components
components.html(tv_widget_html, height=610, scrolling=False)

st.markdown("---")
st.info(f"💡 Active Chart: **{selected_index}** (5m / All Timeframes & Drawing tools enabled)")
