import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================
# PAGE CONFIG
# ==================================
st.markdown("""
<div style="
padding:30px;
border-radius:20px;
background:linear-gradient(90deg,#00E5FF,#0066FF);
color:white;
">

<h1>📊 Executive Dashboard</h1>

<h3>Monitor Revenue, Expenses, Profit & Growth</h3>

<p>
Real-time business intelligence powered by AI.
</p>

</div>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="EBLE Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ==================================
# TITLE
# ==================================

st.title("🚀 EBLE Dashboard")
st.caption("Empowering Every Business to Level Up")

# ==================================
# LOAD DATA
# ==================================

sales_df = pd.read_csv("data/sales.csv")
expenses_df = pd.read_csv("data/expenses.csv")
shops_df = pd.read_csv("data/shops.csv")

# ==================================
# CLEAN DATA
# ==================================

sales_df["Revenue"] = pd.to_numeric(
    sales_df["Revenue"],
    errors="coerce"
)

expenses_df["Amount"] = pd.to_numeric(
    expenses_df["Amount"],
    errors="coerce"
)

# ==================================
# SHOP SELECTOR
# ==================================

selected_shop = st.selectbox(
    "🏪 Select Business",
    shops_df["ShopName"]
)

shop_id = shops_df[
    shops_df["ShopName"] == selected_shop
]["ShopID"].iloc[0]

# ==================================
# FILTER DATA
# ==================================

sales = sales_df[
    sales_df["ShopID"] == shop_id
]

expenses = expenses_df[
    expenses_df["ShopID"] == shop_id
]

# ==================================
# KPI CALCULATIONS
# ==================================

revenue = sales["Revenue"].sum()
expense_total = expenses["Amount"].sum()
profit = revenue - expense_total

if revenue > 0:
    margin = (profit / revenue) * 100
else:
    margin = 0

# Readiness Score

readiness_score = 50

if revenue > 10000:
    readiness_score += 20

if profit > 5000:
    readiness_score += 15

if len(sales) >= 2:
    readiness_score += 10

if len(expenses) >= 2:
    readiness_score += 5

if readiness_score > 100:
    readiness_score = 100

forecast = revenue * 1.10

# ==================================
# KPI ROW
# ==================================

c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    st.metric(
        "💰 Revenue",
        f"₹{revenue:,.0f}"
    )

with c2:
    st.metric(
        "💸 Expenses",
        f"₹{expense_total:,.0f}"
    )

with c3:
    st.metric(
        "📈 Profit",
        f"₹{profit:,.0f}"
    )

with c4:
    st.metric(
        "📊 Margin",
        f"{margin:.1f}%"
    )

with c5:
    st.metric(
        "📑 Readiness",
        f"{readiness_score}/100"
    )

with c6:
    st.metric(
        "🔮 Forecast",
        f"₹{forecast:,.0f}"
    )

st.markdown("---")

# ==================================
# REVENUE TREND
# ==================================

st.subheader("📈 Revenue Trend")

if not sales.empty:

    sales["Date"] = pd.to_datetime(
        sales["Date"],
        errors="coerce"
    )

    revenue_trend = (
        sales.groupby("Date")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        revenue_trend,
        x="Date",
        y="Revenue",
        markers=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==================================
# TWO COLUMN SECTION
# ==================================

left, right = st.columns(2)

with left:

    st.subheader("🏆 Top Products")

    if (
        not sales.empty
        and "Product" in sales.columns
    ):

        top_products = (
            sales.groupby("Product")["Revenue"]
            .sum()
            .reset_index()
            .sort_values(
                by="Revenue",
                ascending=False
            )
        )

        st.dataframe(
            top_products,
            use_container_width=True
        )

with right:

    st.subheader("💸 Expense Breakdown")

    if (
        not expenses.empty
        and "Expense_Type" in expenses.columns
    ):

        expense_summary = (
            expenses.groupby("Expense_Type")["Amount"]
            .sum()
            .reset_index()
        )

        fig2 = px.pie(
            expense_summary,
            names="Expense_Type",
            values="Amount",
            hole=0.5
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

# ==================================
# AI INSIGHTS
# ==================================

st.markdown("---")

st.subheader("🤖 AI Insights")

if profit > 0:

    st.success(
        f"Business generated ₹{profit:,.0f} profit."
    )

else:

    st.warning(
        "Business is currently operating at a loss."
    )

if readiness_score >= 80:

    st.success(
        "🏦 Highly loan-ready business."
    )

elif readiness_score >= 60:

    st.info(
        "📑 Financial readiness is improving."
    )

else:

    st.warning(
        "⚠ Continue recording business transactions."
    )

# ==================================
# EXECUTIVE SUMMARY
# ==================================

st.markdown("---")

st.subheader("📋 Executive Summary")

st.info(
    f"""
Business: {selected_shop}

Revenue: ₹{revenue:,.0f}

Expenses: ₹{expense_total:,.0f}

Profit: ₹{profit:,.0f}

Readiness Score: {readiness_score}/100

Forecast Revenue: ₹{forecast:,.0f}
"""
)

from utils.theme import apply_theme

apply_theme()