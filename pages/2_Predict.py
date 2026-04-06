import streamlit as st
import pandas as pd
import joblib

st.title("🤖 Attrition Risk Predictor")

model = joblib.load("attrition_model.pkl")

age = st.slider("Age", 18, 60, 30)
income = st.number_input("Monthly Income", 1000, 20000, 5000)
overtime = st.selectbox("OverTime", ["No", "Yes"])
overtime = 1 if overtime == "Yes" else 0

if st.button("Predict"):

    input_data = pd.DataFrame([{
        'Age': age,
        'DailyRate': 500,
        'DistanceFromHome': 5,
        'Education': 3,
        'EnvironmentSatisfaction': 3,
        'Gender': 1,
        'HourlyRate': 60,
        'JobInvolvement': 3,
        'JobLevel': 2,
        'JobSatisfaction': 3,
        'MonthlyIncome': income,
        'MonthlyRate': 15000,
        'NumCompaniesWorked': 2,
        'OverTime': overtime,
        'PercentSalaryHike': 13,
        'PerformanceRating': 3,
        'RelationshipSatisfaction': 3,
        'StockOptionLevel': 1,
        'TotalWorkingYears': 8,
        'TrainingTimesLastYear': 2,
        'WorkLifeBalance': 3,
        'YearsAtCompany': 5,
        'YearsInCurrentRole': 3,
        'YearsSinceLastPromotion': 1,
        'YearsWithCurrManager': 3
    }])

    prob = model.predict_proba(input_data)[0][1]

    st.success(f"Attrition Risk: {prob*100:.2f}%")
