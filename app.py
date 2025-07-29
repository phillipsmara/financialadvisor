import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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


                               
