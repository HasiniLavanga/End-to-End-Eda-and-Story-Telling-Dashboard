# ============================================
# DAY 5: STREAMLIT DASHBOARD (BASIC UI)
# ============================================

import streamlit as st
import pandas as pd

print("\n📊 Starting Day 5: Streamlit Dashboard...\n")

# --------------------------------------------
# Page Config
# --------------------------------------------
st.set_page_config(page_title="EDA Dashboard", layout="wide")

# --------------------------------------------
# Title
# --------------------------------------------
st.title("📊 Housing Data Dashboard")

st.markdown("### End-to-End EDA & Storytelling Dashboard")

# --------------------------------------------
# Load Data
# --------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_housing.csv")
    return df

df = load_data()

# --------------------------------------------
# Sidebar Filters
# --------------------------------------------
st.sidebar.header("🔍 Filter Data")

furnishing = st.sidebar.selectbox(
    "Select Furnishing Status",
    options=df['furnishingstatus'].unique()
)

filtered_df = df[df['furnishingstatus'] == furnishing]

# --------------------------------------------
# KPIs
# --------------------------------------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Houses", len(filtered_df))
col2.metric("Average Price", int(filtered_df['price'].mean()))
col3.metric("Max Price", int(filtered_df['price'].max()))

# --------------------------------------------
# Show Data
# --------------------------------------------
st.subheader("📊 Filtered Dataset")

st.dataframe(filtered_df)

# --------------------------------------------
# END MESSAGE
# --------------------------------------------
st.success("🎉 Day 5 Completed Successfully! Dashboard UI Created.")
