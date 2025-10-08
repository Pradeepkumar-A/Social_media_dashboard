#installed the libraries such as flask, pandas, plotly, requests, and tweepy instaloader
#pip install streamlit pandas plotly
#pip install streamlit-autorefresh
import streamlit as st
import pandas as pd
import plotly.express as px
import random

# --- Page Setup ---
st.set_page_config(page_title="Social Media Dashboard", page_icon="📊", layout="wide")

# --- Auto Refresh (every 10 seconds = 10000 ms) ---
from streamlit_autorefresh import st_autorefresh

# Refresh the dashboard every 10 seconds
count = st_autorefresh(interval=10000, limit=None, key="frefresh")

st.title("📊 Social Media Dashboard (Auto Refresh)")
st.markdown("This dashboard updates every **10 seconds** with new random data.")

# --- Simulated Social Media Data ---
platforms = ["Instagram", "Twitter", "YouTube", "LinkedIn"]
followers = [random.randint(1000, 5000) for _ in platforms]
growth = [round(random.uniform(-2, 5), 2) for _ in platforms]

df = pd.DataFrame({
    "Platform": platforms,
    "Followers": followers,
    "Growth (%)": growth
})

# --- Layout & Charts ---
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(df, x="Platform", y="Followers", color="Platform", title="Followers Count")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.line(df, x="Platform", y="Growth (%)", markers=True, title="Growth Rate (%)")
    st.plotly_chart(fig2, use_container_width=True)

st.dataframe(df)