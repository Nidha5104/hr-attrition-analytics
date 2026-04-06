import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="HR Dashboard", layout="wide")

st.title("📊 HR Attrition Dashboard")

# Load data
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Convert target
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# ================= KPI =================
col1, col2 = st.columns(2)

attrition_rate = df['Attrition'].mean() * 100
avg_income = df['MonthlyIncome'].mean()

col1.metric("Attrition Rate (%)", f"{attrition_rate:.2f}")
col2.metric("Average Income", f"{avg_income:.0f}")

st.markdown("---")

# ================= AGE DISTRIBUTION =================
fig_age = px.histogram(
    df,
    x="Age",
    color="Attrition",
    barmode="overlay",
    title="Attrition by Age"
)
st.plotly_chart(fig_age, use_container_width=True)

# ================= DEPARTMENT =================
fig_dept = px.histogram(
    df,
    x="Department",
    color="Attrition",
    barmode="group",
    title="Attrition by Department"
)
st.plotly_chart(fig_dept, use_container_width=True)

# ================= INCOME =================
fig_income = px.box(
    df,
    x="Attrition",
    y="MonthlyIncome",
    title="Income Distribution"
)
st.plotly_chart(fig_income, use_container_width=True)

# ================= NEW GRAPHS =================

st.markdown("## 🔍 Advanced Insights")

col3, col4 = st.columns(2)

# OVERTIME
fig_ot = px.histogram(
    df,
    x="OverTime",
    color="Attrition",
    barmode="group",
    title="Attrition vs OverTime"
)
col3.plotly_chart(fig_ot, use_container_width=True)

# JOB SATISFACTION
fig_js = px.histogram(
    df,
    x="JobSatisfaction",
    color="Attrition",
    barmode="group",
    title="Attrition vs Job Satisfaction"
)
col4.plotly_chart(fig_js, use_container_width=True)

col5, col6 = st.columns(2)

# WORK LIFE BALANCE
fig_wlb = px.histogram(
    df,
    x="WorkLifeBalance",
    color="Attrition",
    barmode="group",
    title="Attrition vs Work-Life Balance"
)
col5.plotly_chart(fig_wlb, use_container_width=True)

# YEARS AT COMPANY
fig_years = px.box(
    df,
    x="Attrition",
    y="YearsAtCompany",
    title="Years at Company vs Attrition"
)
col6.plotly_chart(fig_years, use_container_width=True)
