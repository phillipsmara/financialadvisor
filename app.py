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

    balances = [monthly_savings * (((1 + rate[risk] / 12) ** i - 1) / (rate[risk] / 12)) for i in range(1, total_months + 1, 12)]
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

# Tab 2
with tab2:
    st.header("Recommended Portfolio Allocation")

    if risk == "Low":
        allocation = {"Stocks": 20, "Bonds": 70, "Cash": 10}
    elif risk == "Medium":
        allocation = {"Stocks": 60, "Bonds": 30, "Cash": 10}
    else:
        allocation = {"Stocks": 80, "Bonds": 15, "Cash": 5}

    st.write(f"Based on a **{risk}** risk profile, we suggest the following allocation:")

    alloc_df = pd.DataFrame({
        'Asset Class': list(allocation.keys()),
        'Allocation (%)': list(allocation.values())
    })

    st.bar_chart(alloc_df.set_index('Asset Class'))

# Tab 3
    st.header("Downloadable Savings Report")

    df_report = pd.DataFrame({
        "Year": years_range,
        "Projected Portfolio Value ($)": balances
    })

    st.dataframe(df_report)

    st.download_button(
        label="📥 Download as CSV",
        data=df_report.to_csv(index=False),
        file_name="automated_financial_advisor.csv",
        mime="text/csv"
    )

                               
