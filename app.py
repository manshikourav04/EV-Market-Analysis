import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EV Market Analysis",
    page_icon="⚡",
    layout="wide"
)

@st.cache_data
def load_data():
    train = pd.read_csv("ev_market_train.csv")
    test = pd.read_csv("ev_market_test.csv")
    return train, test

train, test = load_data()

st.title("⚡ Electric Vehicle Market Analysis")
st.subheader("EV Market Trends and Insights")
st.success("Datasets loaded successfully!")

# Dataset Overview
st.header("Dataset Overview")

c1, c2, c3 = st.columns(3)
c1.metric("Training Records", len(train))
c2.metric("Testing Records", len(test))
c3.metric("Total Columns", len(train.columns))

# Dataset Preview
st.header("Training Dataset")
st.dataframe(train.head(10), width="stretch")

# Filters
st.header("EV Market Filters")

manufacturer = st.selectbox(
    "Select Manufacturer",
    ["All"] + sorted(train["manufacturer"].dropna().unique().tolist())
)

filtered = train.copy()

if manufacturer != "All":
    filtered = filtered[filtered["manufacturer"] == manufacturer]

st.write("Filtered Records:", len(filtered))

# Manufacturer Analysis
st.header("Manufacturer Analysis")
st.bar_chart(filtered["manufacturer"].value_counts().head(10))

# Vehicle Category Analysis
st.header("Vehicle Category Analysis")
st.bar_chart(filtered["category"].value_counts())

# Battery Analysis
st.header("Battery Type Analysis")
st.bar_chart(filtered["battery_type"].value_counts())

# Range Analysis
st.header("Average EV Range by Category")
range_data = filtered.groupby("category")["range_km"].mean()
st.bar_chart(range_data)

# Price Analysis
st.header("EV Price Analysis")
st.bar_chart(
    filtered.groupby("category")["price_usd"].mean()
)

st.success("EV Market Dashboard Completed Successfully!")