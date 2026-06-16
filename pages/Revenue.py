import streamlit as st
import pandas as pd
from datetime import date

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Revenue Manager",
    page_icon="💰",
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
st.title("💰 Revenue Manager")

# ==================================
# LOAD DATA
# ==================================

try:
    sales_df = pd.read_csv("data/sales.csv")
except:
    sales_df = pd.DataFrame(
        columns=[
            "ShopID",
            "Date",
            "Product",
            "Category",
            "Revenue",
            "Quantity"
        ]
    )

shops_df = pd.read_csv("data/shops.csv")

# ==================================
# DEBUG INFO
# ==================================

st.info(f"Total Revenue Records: {len(sales_df)}")

# ==================================
# ADD REVENUE FORM
# ==================================

st.markdown("---")
st.subheader("➕ Add Revenue")

with st.form("revenue_form"):

    shop = st.selectbox(
        "🏪 Select Business",
        shops_df["ShopName"]
    )

    revenue_date = st.date_input(
        "Date",
        value=date.today()
    )

    product = st.text_input(
        "Product Name"
    )

    category = st.selectbox(
        "Category",
        [
            "Grocery",
            "Retail",
            "Dairy",
            "Food",
            "Beverages",
            "Electronics",
            "Other"
        ]
    )

    revenue = st.number_input(
        "Revenue (₹)",
        min_value=0.0,
        step=100.0
    )

    quantity = st.number_input(
        "Quantity Sold",
        min_value=0,
        step=1
    )

    submitted = st.form_submit_button(
        "💾 Add Revenue"
    )

# ==================================
# SAVE REVENUE
# ==================================

if submitted:

    shop_id = shops_df[
        shops_df["ShopName"] == shop
    ]["ShopID"].iloc[0]

    new_row = pd.DataFrame([{
        "ShopID": shop_id,
        "Date": str(revenue_date),
        "Product": product,
        "Category": category,
        "Revenue": revenue,
        "Quantity": quantity
    }])

    sales_df = pd.concat(
        [sales_df, new_row],
        ignore_index=True
    )

    sales_df.to_csv(
        "data/sales.csv",
        index=False
    )

    st.success(
        "✅ Revenue Added Successfully"
    )

# ==================================
# KPI SECTION
# ==================================

st.markdown("---")

total_revenue = 0

if not sales_df.empty:

    sales_df["Revenue"] = pd.to_numeric(
        sales_df["Revenue"],
        errors="coerce"
    )

    total_revenue = sales_df["Revenue"].sum()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "💰 Total Revenue",
        f"₹{total_revenue:,.0f}"
    )

with col2:

    st.metric(
        "📦 Total Transactions",
        len(sales_df)
    )

# ==================================
# REVENUE HISTORY
# ==================================

st.markdown("---")
st.subheader("📋 Revenue History")

if not sales_df.empty:

    st.dataframe(
        sales_df,
        use_container_width=True
    )

else:

    st.warning(
        "No revenue records available."
    )

# ==================================
# TOP PRODUCTS
# ==================================

st.markdown("---")
st.subheader("🏆 Top Products")

if not sales_df.empty:

    product_summary = (
        sales_df.groupby("Product")["Revenue"]
        .sum()
        .reset_index()
        .sort_values(
            by="Revenue",
            ascending=False
        )
    )

    st.dataframe(
        product_summary,
        use_container_width=True
    )

# ==================================
# AI INSIGHT
# ==================================

st.markdown("---")
st.subheader("🤖 Revenue Insight")

if not sales_df.empty:

    top_product = (
        sales_df.groupby("Product")["Revenue"]
        .sum()
        .idxmax()
    )

    st.success(
        f"🏆 Best Performing Product: {top_product}"
    )

    st.info(
        f"💰 Current Revenue Recorded: ₹{total_revenue:,.0f}"
    )

else:

    st.warning(
        "No data available for analysis."
    )
