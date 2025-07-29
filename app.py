import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Page Title and Subheading

st.title("Automated Financial Advisor")
st.subheader("Input your Financial Info Into the Sidebar to See your Saving Predictions and Personalized Reccomendations")

# Sidebar with User Inputs

st.sidebar.header("Your Info")
goal = st.sidebar.number_input("Savings Target ($)", min_value = 500, value = 20000)
years = st.sidebar.slider("Time Horizon", 1, 40, value=5)
monthly_income = st.sidebar.number_input("Monthly Income", min_value = 0, value = 5000)
monthly_expenses = st.sidebar.number_input("Monthly Expenses", min_value = 0, value = 2000)
risk = st.sidebar.selectbox("Investment Risk Tolerance", ["Low", "Medium", "High"])

monthly_savings = max(0, monthly_income - monthly_expenses)
total_months = years * 12
rate = {"Low": 0.04, "Medium": 0.06, "High": 0.08}

# Initialize Tabs

tab1, tab2, tab3 = st.tabs(["Growth Over Time", "Portfolio Suggestions", "Download Report"])

# Tab 1
with tab1:
    st.header("Projected Investment Growth")

    balances = [monthly_savings * (((1 + rate / 12) ** i - 1) / (rate / 12)) for i in range(1, total_months + 1, 12)]
    years_range = list(range(1, years + 1))

    fig, ax = plt.subplots()
    ax.plot(years_range, balances, marker='o')
    ax.set_title("Projected Portfolio Value Over Time")
    ax.set_xlabel("Years")
    ax.set_ylabel("Value ($)")
    st.pyplot(fig)

    future_value = balances[-1] if balances else 0

    st.markdown("### Plan Summary")
    st.write(f"**Monthly Saving Capacity:** `${monthly_savings:.2f}`")
    st.write(f"**Estimated Portfolio Value in {years} years:** `${future_value:,.2f}`")

    if future_value >= goal:
        st.success("🎯 You’re on track to reach your goal!")
    else:
        needed = goal - future_value
        st.warning(f"⚠️ You need to increase your savings or timeline by ~`${needed:,.2f}`.")

                               
