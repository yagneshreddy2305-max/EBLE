import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Expense Manager",
    page_icon="💸",
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

st.title("💸 Expense Manager")

# Load Data Safely
try:
    expenses_df = pd.read_csv("data/expenses.csv")
except:
    expenses_df = pd.DataFrame(
        columns=["ShopID", "Date", "Expense_Type", "Amount"]
    )

shops_df = pd.read_csv("data/shops.csv")

st.markdown("---")

with st.form("expense_form"):

    shop = st.selectbox(
        "Select Business",
        shops_df["ShopName"]
    )

    expense_date = st.date_input(
        "Date",
        value=date.today()
    )

    expense_type = st.selectbox(
        "Expense Type",
        [
            "Rent",
            "Electricity",
            "Salary",
            "Transport",
            "Marketing",
            "Raw Material",
            "Internet",
            "Other"
        ]
    )

    amount = st.number_input(
        "Amount (₹)",
        min_value=0,
        step=100
    )

    submitted = st.form_submit_button(
        "➕ Add Expense"
    )

if submitted:

    shop_id = shops_df[
        shops_df["ShopName"] == shop
    ]["ShopID"].iloc[0]

    new_expense = pd.DataFrame([{
        "ShopID": shop_id,
        "Date": str(expense_date),
        "Expense_Type": expense_type,
        "Amount": amount
    }])

    expenses_df = pd.concat(
        [expenses_df, new_expense],
        ignore_index=True
    )

    expenses_df.to_csv(
        "data/expenses.csv",
        index=False
    )

    st.success(
        "✅ Expense Added Successfully"
    )

st.markdown("---")

st.subheader("📋 Expense History")

st.dataframe(
    expenses_df,
    use_container_width=True
)

st.markdown("---")

st.subheader("📊 Total Expenses")

if not expenses_df.empty:

    st.metric(
        "Total Expenses",
        f"₹{expenses_df['Amount'].sum():,.0f}"
    )

    from utils.theme import apply_theme

apply_theme()