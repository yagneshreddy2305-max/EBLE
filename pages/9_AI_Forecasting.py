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
background:linear-gradient(90deg,#7B61FF,#4A00E0);
color:white;
">

<h1>🔮 AI Forecasting</h1>

<h3>Predict Business Growth Before It Happens</h3>

<p>
Revenue Forecasts, Growth Scores and Expansion Insights.
</p>

</div>
""", unsafe_allow_html=True)
st.set_page_config(
    page_title="AI Forecasting",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 AI Forecasting")

st.markdown("""
AI-powered revenue forecasting and business growth intelligence.
""")

# ==================================
# LOAD DATA
# ==================================

sales_df = pd.read_csv("data/sales.csv")
shops_df = pd.read_csv("data/shops.csv")

# ==================================
# CLEAN DATA
# ==================================

sales_df["Revenue"] = pd.to_numeric(
    sales_df["Revenue"],
    errors="coerce"
)

# ==================================
# BUSINESS SELECTOR
# ==================================

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

# ==================================
# CALCULATIONS
# ==================================
# ==================================
# CALCULATIONS
# ==================================

revenue = sales["Revenue"].sum()

avg_sale = sales["Revenue"].mean()

if pd.isna(avg_sale):
    avg_sale = 0

month1 = revenue + (avg_sale * 5)
month2 = revenue + (avg_sale * 10)
month3 = revenue + (avg_sale * 15)

expense_total = 0
profit = revenue

# ==================================
# KPI CARDS
# ==================================

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Current Revenue",
        f"₹{revenue:,.0f}"
    )

with c2:
    st.metric(
        "Next Month",
        f"₹{month1:,.0f}"
    )

with c3:
    st.metric(
        "2 Months",
        f"₹{month2:,.0f}"
    )

with c4:
    st.metric(
        "3 Months",
        f"₹{month3:,.0f}"
    )

# ==================================
# FORECAST GRAPH
# ==================================

st.markdown("---")

st.subheader("📈 Revenue Forecast")

forecast_df = pd.DataFrame({
    "Period": [
        "Current",
        "Month 1",
        "Month 2",
        "Month 3"
    ],
    "Revenue": [
        revenue,
        month1,
        month2,
        month3
    ]
})

fig = px.line(
    forecast_df,
    x="Period",
    y="Revenue",
    markers=True,
    title="Projected Revenue Growth"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==================================
# GROWTH SCORE
# ==================================

st.markdown("---")

st.subheader("🚀 AI Growth Score")

growth_score = 50

if revenue > 10000:
    growth_score += 20

if revenue > 20000:
    growth_score += 10

if month3 > revenue:
    growth_score += 20

growth_score = min(growth_score, 100)

st.metric(
    "Growth Potential Score",
    f"{growth_score}/100"
)

if growth_score >= 80:

    st.success(
        "🚀 High Growth Business"
    )

elif growth_score >= 60:

    st.info(
        "📈 Moderate Growth Business"
    )

else:

    st.warning(
        "⚠ Early Stage Business"
    )

# ==================================
# AI BUSINESS INTELLIGENCE
# ==================================

st.markdown("---")

st.subheader("🤖 AI Business Intelligence")

if revenue >= 20000:

    st.success(
        "🚀 Revenue is strong. Consider opening a second outlet or expanding inventory."
    )

elif revenue >= 10000:

    st.info(
        "📈 Revenue growth is healthy. Focus on increasing customer retention and repeat purchases."
    )

else:

    st.warning(
        "⚠ Revenue is relatively low. Consider local promotions and product bundling strategies."
    )

# ==================================
# FORECAST ANALYSIS
# ==================================

growth_percent = (
    ((month3 - revenue) / revenue) * 100
    if revenue > 0
    else 0
)

st.info(
    f"📊 AI predicts approximately {growth_percent:.1f}% revenue growth over the next 3 months."
)

# ==================================
# RISK ANALYSIS
# ==================================

st.subheader("⚠ Risk Analysis")

if revenue < 5000:

    st.error(
        "🔴 High Risk: Current revenue levels may limit business expansion opportunities."
    )

elif revenue < 15000:

    st.warning(
        "🟡 Moderate Risk: Focus on controlling expenses and increasing sales volume."
    )

else:

    st.success(
        "🟢 Low Risk: Business demonstrates stable revenue performance."
    )

# ==================================
# FUNDING READINESS
# ==================================

st.subheader("🏦 Funding Readiness")

if revenue >= 15000:

    st.success(
        "Business appears eligible for micro-business loans and government credit schemes."
    )

else:

    st.info(
        "Continue recording transactions regularly to improve credit readiness."
    )

# ==================================
# STRATEGIC RECOMMENDATIONS
# ==================================

st.subheader("🤖 Personalized AI Recommendations")

if not sales.empty:

    top_product = (
        sales.groupby("Product")["Revenue"]
        .sum()
        .idxmax()
    )

    st.success(
        f"🏆 Best Selling Product: {top_product}"
    )

    if top_product == "Rice":
        st.info(
            "Increase rice inventory and wholesale purchasing."
        )

    elif top_product == "Milk":
        st.info(
            "Expand dairy product offerings."
        )

    elif top_product == "Tea":
        st.info(
            "Introduce tea + snacks combo offers."
        )

    else:
        st.info(
            f"Focus on expanding sales of {top_product}."
        )

expense_ratio = (
    (expense_total / revenue) * 100
    if revenue > 0 else 0
)

if expense_ratio > 50:
    st.warning(
        "Expenses are consuming more than 50% of revenue."
    )
else:
    st.success(
        "Expenses are under control."
    )

if growth_score >= 80:
    st.success(
        "Business has high growth potential."
    )
elif growth_score >= 60:
    st.info(
        "Business has moderate growth potential."
    )
else:
    st.warning(
        "Focus on increasing revenue before expansion."
    )

# ==================================
# EXECUTIVE SUMMARY
# ==================================

st.markdown("---")

st.subheader("📋 Executive Summary")

st.info(
    f"""
Business: {selected_shop}

Current Revenue: ₹{revenue:,.0f}

Forecast (1 Month): ₹{month1:,.0f}

Forecast (2 Months): ₹{month2:,.0f}

Forecast (3 Months): ₹{month3:,.0f}

Growth Score: {growth_score}/100

Expected Growth: {growth_percent:.1f}%
"""
)

from utils.theme import apply_theme

apply_theme()