import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Profit Trends",
    page_icon="📈",
    layout="wide"
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
st.title("📈 Profit Trends")

# Load Data
sales_df = pd.read_csv("data/sales.csv")
expenses_df = pd.read_csv("data/expenses.csv")
shops_df = pd.read_csv("data/shops.csv")

# Shop Selector
selected_shop = st.selectbox(
    "Select Business",
    shops_df["ShopName"]
)

shop_id = shops_df[
    shops_df["ShopName"] == selected_shop
]["ShopID"].iloc[0]

sales = sales_df[
    sales_df["ShopID"] == shop_id
]

expenses = expenses_df[
    expenses_df["ShopID"] == shop_id
]

# Convert dates
sales["Date"] = pd.to_datetime(sales["Date"])
expenses["Date"] = pd.to_datetime(expenses["Date"])

# Revenue by date
daily_revenue = (
    sales.groupby("Date")["Revenue"]
    .sum()
    .reset_index()
)

# Expenses by date
daily_expenses = (
    expenses.groupby("Date")["Amount"]
    .sum()
    .reset_index()
)

# Merge
profit_df = pd.merge(
    daily_revenue,
    daily_expenses,
    on="Date",
    how="outer"
).fillna(0)

profit_df["Profit"] = (
    profit_df["Revenue"]
    - profit_df["Amount"]
)

# KPI
total_profit = profit_df["Profit"].sum()

st.metric(
    "Net Profit",
    f"₹{total_profit:,.0f}"
)

# Daily Profit Trend
st.markdown("---")
st.subheader("📈 Daily Profit Trend")

fig1 = px.line(
    profit_df,
    x="Date",
    y="Profit",
    markers=True,
    title="Daily Profit Trend"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# Profit Distribution
st.markdown("---")
st.subheader("💰 Profit Distribution")

fig2 = px.bar(
    profit_df,
    x="Date",
    y="Profit",
    title="Profit by Date"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# Growth Calculation
if len(profit_df) > 1:

    first_profit = profit_df["Profit"].iloc[0]
    last_profit = profit_df["Profit"].iloc[-1]

    if first_profit != 0:

        growth = (
            (last_profit - first_profit)
            / abs(first_profit)
        ) * 100

    else:

        growth = 0

else:

    growth = 0

st.markdown("---")

st.subheader("🚀 Profit Growth")

st.metric(
    "Growth %",
    f"{growth:.1f}%"
)

# Business Performance Score
if growth > 20:
    score = 95
elif growth > 10:
    score = 85
elif growth > 0:
    score = 75
else:
    score = 60

st.metric(
    "Business Performance Score",
    f"{score}/100"
)

# Insight
st.markdown("---")

st.subheader("🤖 Profit Insight")

if growth > 10:

    st.success(
        "Business profitability is growing steadily."
    )

elif growth > 0:

    st.info(
        "Business is profitable with moderate growth."
    )

else:

    st.warning(
        "Profit growth is slowing. Monitor expenses closely."
    )

    from utils.theme import apply_theme

apply_theme()