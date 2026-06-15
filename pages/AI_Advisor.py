import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Advisor",
    page_icon="🤖",
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

st.title("🤖 EBLE AI Advisor")

sales_df = pd.read_csv("data/sales.csv")
expenses_df = pd.read_csv("data/expenses.csv")
shops_df = pd.read_csv("data/shops.csv")

selected_shop = st.selectbox(
    "🏪 Select Business",
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

revenue = pd.to_numeric(
    sales["Revenue"],
    errors="coerce"
).sum()

expense_total = pd.to_numeric(
    expenses["Amount"],
    errors="coerce"
).sum()

profit = revenue - expense_total

st.markdown("---")

# Best Product

if not sales.empty:

    top_product = (
        sales.groupby("Product")["Revenue"]
        .sum()
        .idxmax()
    )

    st.success(
        f"🏆 Best Selling Product: {top_product}"
    )

# Profit Analysis

if profit > 0:

    st.success(
        f"💰 Business Profit: ₹{profit:,.0f}"
    )

else:

    st.error(
        "⚠ Business currently running at a loss."
    )

# Revenue Analysis

if revenue >= 15000:

    st.success(
        "📈 Revenue performance is strong."
    )

else:

    st.warning(
        "📊 Revenue can be improved."
    )

# Expense Analysis

if expense_total > revenue * 0.5:

    st.warning(
        "💸 Expenses are relatively high."
    )

else:

    st.success(
        "✅ Expenses are under control."
    )

st.markdown("---")
st.subheader("🚀 AI Recommendations")

recommendations = []

if profit > 0:
    recommendations.append(
        "Increase inventory of best-selling products."
    )

if expense_total > revenue * 0.4:
    recommendations.append(
        "Reduce recurring operational expenses."
    )

recommendations.append(
    "Track revenue daily for better forecasting."
)

recommendations.append(
    "Maintain digital records for financial readiness."
)

recommendations.append(
    "Explore suitable government schemes and credit options."
)

for rec in recommendations:
    st.info(rec)

st.markdown("---")
st.subheader("📋 AI Summary")

st.info(
    f"""
Business: {selected_shop}

Revenue: ₹{revenue:,.0f}

Expenses: ₹{expense_total:,.0f}

Profit: ₹{profit:,.0f}

AI Status: Active Monitoring
"""
)

from utils.theme import apply_theme

apply_theme()