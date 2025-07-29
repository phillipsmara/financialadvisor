import streamlit as st
import numpy as np

st.title("Financial Advisor")
st.markdown("### Input Your Data Below to See If Your Are on Track to Meet Your Financial Goals")

# User Inputs
goal = st.number_input("Target Amount ($)", min_value=1000)
years = st.slider("Time Frame of Investment (Years)", 1, 40)
monthly_income = st.number_input("Monthly Income ($)", min_value=0)
monthly_expenses = st.number_input("Monthly Expenses ($)", min_value=0)
risk = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])

# Logic
monthly_saving = monthly_income - monthly_expenses
total_months = years * 12

# Estimated return rates
if risk == "Low":
    rate = 0.04
elif risk == "Medium":
    rate = 0.06
else:
    rate = 0.08

# Future Value Calculation (compound interest)
future_value = monthly_saving * (((1 + rate / 12) ** total_months - 1) / (rate / 12))

# Output
st.markdown("### 🧾 Plan Summary")
st.write(f"Monthly Saving Capacity: ${monthly_saving:.2f}")
st.write(f"Estimated Portfolio Value in {years} years: ${future_value:,.2f}")

if future_value >= goal:
    st.success("🎯 You’re on track to reach your goal!")
else:
    needed = goal - future_value
    st.warning(f"⚠️ You’ll need to increase your savings or timeline by ~${needed:,.2f}.")
