import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Credit Hub",
    page_icon="🏦",
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

st.title("🏦 Credit Hub")

st.markdown("""
Discover funding opportunities, loan schemes and
credit options based on your business profile.
""")

# Load Data
sales_df = pd.read_csv("data/sales.csv")
expenses_df = pd.read_csv("data/expenses.csv")
shops_df = pd.read_csv("data/shops.csv")

# Business Selector
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

# Metrics
revenue = pd.to_numeric(
    sales["Revenue"],
    errors="coerce"
).sum()

expense_total = pd.to_numeric(
    expenses["Amount"],
    errors="coerce"
).sum()

profit = revenue - expense_total

# Credit Score
credit_score = 50

credit_score += min(revenue / 500, 25)
credit_score += min(profit / 250, 25)

credit_score = min(int(credit_score), 100)

# KPI
c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "💳 Credit Score",
        f"{credit_score}/100"
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

st.markdown("---")

st.subheader("🏦 Funding Eligibility")

if credit_score >= 80:

    st.success("""
    Eligible For:

    ✅ MSME Loans

    ✅ Mudra Tarun

    ✅ Working Capital Loans

    ✅ Business Expansion Funding
    """)

elif credit_score >= 60:

    st.info("""
    Eligible For:

    ✅ Mudra Kishor

    ✅ Merchant Loans

    ✅ Small Business Credit
    """)

else:

    st.warning("""
    Build stronger financial records
    before applying for major funding.
    """)

st.markdown("---")

st.subheader("💡 AI Credit Recommendations")

if profit > 10000:

    st.success(
        "Strong profitability improves funding chances."
    )

elif profit > 5000:

    st.info(
        "Maintain profitability and transaction history."
    )

else:

    st.warning(
        "Increase profit margins before seeking larger loans."
    )

st.markdown("---")

st.subheader("📄 Documents Typically Required")

st.info("""
• Aadhaar Card

• PAN Card

• Bank Statements

• UPI Transaction History

• Sales Records

• Expense Records

• GST Registration (if applicable)

• Business Address Proof
""")

st.markdown("---")

st.subheader("📋 Credit Summary")

st.info(
    f"""
Business: {selected_shop}

Revenue: ₹{revenue:,.0f}

Profit: ₹{profit:,.0f}

Credit Score: {credit_score}/100

Funding Status:
{'Excellent' if credit_score >= 80 else 'Moderate' if credit_score >= 60 else 'Needs Improvement'}
"""
)

from utils.theme import apply_theme

apply_theme()