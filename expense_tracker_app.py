
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("expense_data_1_year.xlsx")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%B %Y")

# Title
st.title("Personal Expense Tracker")

# KPIs
total_spent = df["Amount"].sum()
top_category = df.groupby("Category")["Amount"].sum().idxmax()
st.metric("Total Spent", f"₹{total_spent:,.2f}")
st.metric("Top Category", top_category)

# Table of expenses
st.subheader("All Expenses")
st.dataframe(df)

# Monthly totals - Bar Chart
st.subheader("Monthly Totals")
monthly_totals = df.groupby("Month")["Amount"].sum().sort_index()
fig1, ax1 = plt.subplots()
monthly_totals.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Amount (₹)")
st.pyplot(fig1)

# Pie chart - Expense by category
st.subheader("Expenses by Category")
category_totals = df.groupby("Category")["Amount"].sum()
fig2, ax2 = plt.subplots()
category_totals.plot(kind="pie", autopct='%1.1f%%', ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)
