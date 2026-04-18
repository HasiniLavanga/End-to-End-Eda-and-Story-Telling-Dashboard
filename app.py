import streamlit as st
import pandas as pd

print("\n🚀 Launching Streamlit Dashboard...\n")

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
# UPDATED MESSAGE (instead of Day 5)
# --------------------------------------------
st.success("✅ Basic dashboard interface created successfully.")

# ============================================

import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------
# Page Config
# --------------------------------------------
st.set_page_config(page_title="EDA Dashboard", layout="wide")

# --------------------------------------------
# Title
# --------------------------------------------
st.title("📊 Housing Data Interactive Dashboard")
st.markdown("### End-to-End EDA & Storytelling Dashboard")

# --------------------------------------------
# Load Data
# --------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_housing.csv")

df = load_data()

# --------------------------------------------
# Sidebar Filter
# --------------------------------------------
st.sidebar.header("🔍 Filter Data")

furnishing = st.sidebar.selectbox(
    "Select Furnishing Status",
    options=df['furnishingstatus'].unique(),
    key="furnishing_filter"
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
# Histogram
# --------------------------------------------
st.subheader("📊 Price Distribution")

fig1 = px.histogram(filtered_df, x="price", nbins=30)
st.plotly_chart(fig1, use_container_width=True)

# --------------------------------------------
# Scatter Plot
# --------------------------------------------
st.subheader("📉 Area vs Price")

fig2 = px.scatter(
    filtered_df,
    x="area",
    y="price",
    color="bedrooms",
    size="bathrooms"
)

st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------
# Heatmap
# --------------------------------------------
st.subheader("🔥 Correlation Heatmap")

corr = filtered_df.corr(numeric_only=True)

fig3 = px.imshow(corr, text_auto=True)
st.plotly_chart(fig3, use_container_width=True)

# --------------------------------------------
# Data Table
# --------------------------------------------
st.subheader("📋 Filtered Dataset")

st.dataframe(filtered_df)

# --------------------------------------------
# UPDATED MESSAGE (instead of Day 6)
# --------------------------------------------
st.success("✅ Interactive dashboard with visual insights is successfully implemented.")
