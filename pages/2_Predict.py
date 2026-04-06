import streamlit as st
import pandas as pd
import joblib

st.title("🤖 Attrition Risk Predictor")

# Load model
model = joblib.load("attrition_model.pkl")

st.subheader("Enter Employee Details")

# 🎯 USER INPUTS
age = st.slider("Age", 18, 60, 30)
income = st.number_input("Monthly Income", 1000, 20000, 5000)
distance = st.slider("Distance From Home", 1, 30, 5)
overtime = st.selectbox("OverTime", ["No", "Yes"])
job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
job_satisfaction = st.slider("Job Satisfaction", 1, 4, 3)
work_life = st.slider("Work Life Balance", 1, 4, 3)
experience = st.slider("Total Working Years", 0, 40, 8)

# 🎯 PREDICTION BUTTON
if st.button("Predict Attrition Risk"):

    # Step 1: Create input dictionary
    input_dict = {
        'Age': age,
        'DailyRate': 500,
        'DistanceFromHome': distance,
        'Education': 3,
        'EnvironmentSatisfaction': 3,
        'Gender': 1,
        'HourlyRate': 60,
        'JobInvolvement': 3,
        'JobLevel': job_level,
        'JobSatisfaction': job_satisfaction,
        'MonthlyIncome': income,
        'MonthlyRate': 15000,
        'NumCompaniesWorked': 2,
        'OverTime': 1 if overtime == "Yes" else 0,
        'PercentSalaryHike': 13,
        'PerformanceRating': 3,
        'RelationshipSatisfaction': 3,
        'StockOptionLevel': 1,
        'TotalWorkingYears': experience,
        'TrainingTimesLastYear': 2,
        'WorkLifeBalance': work_life,
        'YearsAtCompany': 5,
        'YearsInCurrentRole': 3,
        'YearsSinceLastPromotion': 1,
        'YearsWithCurrManager': 3
    }

    # Step 2: Convert to DataFrame
    input_data = pd.DataFrame([input_dict])

    # 🔥 Step 3: Ensure all required features exist
    for col in model.feature_names_in_:
        if col not in input_data.columns:
            input_data[col] = 0

    # 🔥 Step 4: Match exact feature order
    input_data = input_data[model.feature_names_in_]

    # Step 5: Prediction
    prob = model.predict_proba(input_data)[0][1]

    # Step 6: Output
    st.success(f"🔥 Attrition Risk: {prob*100:.2f}%")

    if prob > 0.5:
        st.error("⚠ High Risk Employee — Retention Needed")
    else:
        st.info("✅ Low Risk Employee")
