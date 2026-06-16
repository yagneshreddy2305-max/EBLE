import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configst.markdown("""

st.set_page_config(
    page_title="Analytics Center",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Analytics Center")

# Load Data
sales_df = pd.read_csv("data/sales.csv")
expenses_df = pd.read_csv("data/expenses.csv")
shops_df = pd.read_csv("data/shops.csv")

# Data Cleaning
sales_df["Revenue"] = pd.to_numeric(
    sales_df["Revenue"],
    errors="coerce"
)

sales_df["Quantity"] = pd.to_numeric(
    sales_df["Quantity"],
    errors="coerce"
)

expenses_df["Amount"] = pd.to_numeric(
    expenses_df["Amount"],
    errors="coerce"
)

sales_df["Date"] = pd.to_datetime(
    sales_df["Date"],
    errors="coerce"
)

expenses_df["Date"] = pd.to_datetime(
    expenses_df["Date"],
    errors="coerce"
)
st.markdown("""
<div style="
padding:30px;
border-radius:20px;
background:linear-gradient(90deg,#00E5FF,#0066FF);
color:white;
">

<h1>🚀 EBLE</h1>

<h3>Empowering Every Business to Level Up</h3>

<p>
AI-Powered Business Intelligence Platform
for Small Businesses, Vendors and Retailers.
</p>

</div>
""", unsafe_allow_html=True)

# Shop Selector
selected_shop = st.selectbox(
    "🏪 Select Business",
    shops_df["ShopName"]
)

shop_id = shops_df[
    shops_df["ShopName"] == selected_shop
]["ShopID"].iloc[0]

# Filter Data
sales = sales_df[
    sales_df["ShopID"] == shop_id
].copy()

expenses = expenses_df[
    expenses_df["ShopID"] == shop_id
].copy()

# KPI Calculations
revenue = sales["Revenue"].sum()
expense_total = expenses["Amount"].sum()
profit = revenue - expense_total

if revenue > 0:
    margin = (profit / revenue) * 100
else:
    margin = 0

# KPI Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Revenue",
        f"₹{revenue:,.0f}"
    )

with col2:
    st.metric(
        "💸 Expenses",
        f"₹{expense_total:,.0f}"
    )

with col3:
    st.metric(
        "📈 Profit",
        f"₹{profit:,.0f}"
    )

with col4:
    st.metric(
        "📊 Margin",
        f"{margin:.1f}%"
    )

# Revenue Trend
st.markdown("---")
st.subheader("📈 Revenue Trend")

if not sales.empty:

    revenue_trend = (
        sales.groupby("Date")["Revenue"]
        .sum()
        .reset_index()
    )

    fig1 = px.line(
        revenue_trend,
        x="Date",
        y="Revenue",
        markers=True
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

# Product Performance
st.markdown("---")
st.subheader("🏆 Product Performance")

if not sales.empty:

    product_sales = (
        sales.groupby("Product")["Revenue"]
        .sum()
        .reset_index()
    )

    fig2 = px.bar(
        product_sales,
        x="Product",
        y="Revenue",
        text_auto=True
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# Category Performance
st.markdown("---")
st.subheader("📦 Category Performance")

if not sales.empty:

    category_sales = (
        sales.groupby("Category")["Revenue"]
        .sum()
        .reset_index()
    )

    fig3 = px.pie(
        category_sales,
        names="Category",
        values="Revenue",
        hole=0.5
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# Expense Breakdown
st.markdown("---")
st.subheader("💸 Expense Breakdown")

if not expenses.empty:

    expense_summary = (
        expenses.groupby("Expense_Type")["Amount"]
        .sum()
        .reset_index()
    )

    fig4 = px.pie(
        expense_summary,
        names="Expense_Type",
        values="Amount",
        hole=0.5
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# Revenue vs Expenses
st.markdown("---")
st.subheader("⚖ Revenue vs Expenses")

comparison_df = pd.DataFrame({
    "Metric": ["Revenue", "Expenses"],
    "Amount": [revenue, expense_total]
})

fig5 = px.bar(
    comparison_df,
    x="Metric",
    y="Amount",
    text_auto=True
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# Top Products
st.markdown("---")
st.subheader("🔥 Top Products")

if not sales.empty:

    top_products = (
        sales.groupby("Product")["Revenue"]
        .sum()
        .reset_index()
        .sort_values(
            by="Revenue",
            ascending=False
        )
        .head(5)
    )

    st.dataframe(
        top_products,
        use_container_width=True
    )

# AI Insights
st.markdown("---")
st.subheader("🤖 AI Insights")

if not sales.empty:

    top_product = (
        sales.groupby("Product")["Revenue"]
        .sum()
        .idxmax()
    )

    st.success(
        f"🏆 Best Selling Product: {top_product}"
    )

if profit > 0:
    st.info(
        f"📈 Net Profit Generated: ₹{profit:,.0f}"
    )
else:
    st.warning(
        "⚠ Business is operating at a loss."
    )

# Executive Summary
st.markdown("---")
st.subheader("📋 Executive Summary")

st.info(
    f"""
Business: {selected_shop}

Revenue: ₹{revenue:,.0f}

Expenses: ₹{expense_total:,.0f}

Profit: ₹{profit:,.0f}

Profit Margin: {margin:.1f}%
"""
)

from utils.theme import apply_theme

apply_theme()