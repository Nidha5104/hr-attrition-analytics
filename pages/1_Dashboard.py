import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 HR Attrition Dashboard")

df = pd.read_csv("dataset.csv")

# KPI
attrition_rate = df['Attrition'].value_counts(normalize=True).get('Yes', 0) * 100
avg_income = df['MonthlyIncome'].mean()

col1, col2 = st.columns(2)

col1.metric("Attrition Rate (%)", f"{attrition_rate:.2f}")
col2.metric("Average Income", f"{int(avg_income)}")

st.divider()

# Charts
fig1 = px.histogram(df, x="Age", color="Attrition", title="Attrition by Age")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.histogram(df, x="Department", color="Attrition", title="Attrition by Department")
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.box(df, x="Attrition", y="MonthlyIncome", title="Income Distribution")
st.plotly_chart(fig3, use_container_width=True)
