import streamlit as st
import pandas as pd
import joblib

st.title("🤖 Attrition Risk Predictor")

# Load model and dataset
model = joblib.load("attrition_model.pkl")
df = pd.read_csv("dataset.csv")

# ---------------- INPUTS ---------------- #

st.subheader("Enter Employee Details")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 60, 30)
    income = st.number_input("Monthly Income", 1000, 20000, 5000)
    distance = st.slider("Distance From Home", 1, 30, 5)
    experience = st.slider("Total Working Years", 0, 40, 8)

with col2:
    overtime = st.selectbox("OverTime", ["No", "Yes"])
    job_level = st.selectbox("Job Level", [1,2,3,4,5])
    job_satisfaction = st.slider("Job Satisfaction", 1, 4, 3)
    work_life = st.slider("Work Life Balance", 1, 4, 3)

# ---------------- PREDICT ---------------- #

if st.button("Predict Attrition Risk"):

    input_data = df.iloc[[0]].copy()

    # Replace values
    input_data['Age'] = age
    input_data['MonthlyIncome'] = income
    input_data['DistanceFromHome'] = distance
    input_data['TotalWorkingYears'] = experience
    input_data['OverTime'] = overtime
    input_data['JobLevel'] = job_level
    input_data['JobSatisfaction'] = job_satisfaction
    input_data['WorkLifeBalance'] = work_life

    # Predict
    prob = model.predict_proba(input_data)[0][1]

    # Output
    if prob > 0.5:
        st.error(f"⚠️ High Attrition Risk: {prob*100:.2f}%")
    else:
        st.success(f"✅ Low Attrition Risk: {prob*100:.2f}%")
