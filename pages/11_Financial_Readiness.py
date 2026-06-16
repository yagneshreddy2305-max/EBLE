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
background:linear-gradient(90deg,#00C853,#009624);
color:white;
">

<h1>📑 Financial Readiness</h1>

<h3>Understand Your Funding Potential</h3>

<p>
Assess Loan Eligibility and Financial Health.
</p>

</div>
""", unsafe_allow_html=True)
st.set_page_config(
    page_title="Financial Readiness",
    page_icon="📑",
    layout="wide"
)

st.title("📑 Financial Readiness Assessment")

st.markdown("""
Evaluate your business's readiness for loans, funding,
and financial growth opportunities.
""")

# ==================================
# LOAD DATA
# ==================================

sales_df = pd.read_csv("data/sales.csv")
expenses_df = pd.read_csv("data/expenses.csv")
shops_df = pd.read_csv("data/shops.csv")

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
# CALCULATIONS
# ==================================

revenue = pd.to_numeric(
    sales["Revenue"],
    errors="coerce"
).sum()

expense_total = pd.to_numeric(
    expenses["Amount"],
    errors="coerce"
).sum()

profit = revenue - expense_total

# Dynamic Readiness Score

score = 0

score += min(revenue / 500, 40)
score += min(profit / 250, 30)
score += min(len(sales) * 2, 20)
score += min(len(expenses), 10)

score = min(int(score), 100)

# ==================================
# STATUS
# ==================================

if score >= 80:
    status = "Excellent"
elif score >= 60:
    status = "Good"
elif score >= 40:
    status = "Moderate"
else:
    status = "Needs Improvement"

# ==================================
# KPI SECTION
# ==================================

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "📊 Readiness Score",
        f"{score}/100"
    )

with c2:
    st.metric(
        "💰 Revenue",
        f"₹{revenue:,.0f}"
    )

with c3:
    st.metric(
        "📈 Profit",
        f"₹{profit:,.0f}"
    )

with c4:
    st.metric(
        "🏆 Status",
        status
    )

# ==================================
# READINESS METER
# ==================================

st.markdown("---")

st.subheader("📈 Financial Readiness Meter")

readiness_df = pd.DataFrame({
    "Category": ["Score"],
    "Value": [score]
})

fig = px.bar(
    readiness_df,
    x="Category",
    y="Value",
    text="Value",
    title="Financial Readiness Score"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==================================
# LOAN ELIGIBILITY
# ==================================

st.markdown("---")

st.subheader("🏦 Loan Eligibility Assessment")

if score >= 80:

    st.success(
        "Eligible for MSME Loans, Mudra Loans and Small Business Funding."
    )

elif score >= 60:

    st.info(
        "Likely eligible for entry-level business credit products."
    )

else:

    st.warning(
        "Improve financial records before applying for business funding."
    )

# ==================================
# FINANCIAL STRENGTH CHECK
# ==================================

st.markdown("---")

st.subheader("💪 Financial Strength Indicators")

checks = {
    "Revenue Records Available": revenue > 0,
    "Profit Positive": profit > 0,
    "Sales History Available": len(sales) > 0,
    "Expense Records Available": len(expenses) > 0,
    "Consistent Business Activity": len(sales) >= 5
}

for item, status_check in checks.items():

    if status_check:
        st.success(f"✅ {item}")
    else:
        st.error(f"❌ {item}")

# ==================================
# DOCUMENT READINESS
# ==================================

st.markdown("---")

st.subheader("📄 Recommended Documents")

st.info("""
• Aadhaar Card

• PAN Card

• Bank Statements

• UPI Transaction History

• Sales Records

• Expense Records

• GST Registration (Optional)

• Business Address Proof
""")

# ==================================
# AI RECOMMENDATIONS
# ==================================

st.markdown("---")

st.subheader("🤖 AI Financial Advisor")

if score >= 80:

    st.success(
        "Your business has strong financial visibility. Consider applying for expansion funding."
    )

elif score >= 60:

    st.info(
        "Maintain consistent sales and expense tracking to improve your credit profile."
    )

else:

    st.warning(
        "Focus on building transaction history and improving profitability."
    )

# ==================================
# FUNDING OPTIONS
# ==================================

st.markdown("---")

st.subheader("💸 Suggested Funding Opportunities")

if score >= 80:

    st.success("""
    • MSME Business Loan

    • Mudra Tarun Loan

    • Small Business Expansion Funding

    • Working Capital Loans
    """)

elif score >= 60:

    st.info("""
    • Mudra Kishor Loan

    • Merchant Credit Products

    • Small Working Capital Loans
    """)

else:

    st.warning("""
    • Build business records first

    • Maintain sales history

    • Improve readiness score
    """)

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

Financial Readiness Score: {score}/100

Status: {status}
"""
)

from utils.theme import apply_theme

apply_theme()