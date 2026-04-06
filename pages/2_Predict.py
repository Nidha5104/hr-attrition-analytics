import streamlit as st
import pandas as pd
import joblib

df = pd.read_csv("dataset.csv")
st.title("🤖 Attrition Risk Predictor")

model = joblib.load("attrition_model.pkl")

age = st.slider("Age", 18, 60, 30)
income = st.number_input("Monthly Income", 1000, 20000, 5000)
overtime = st.selectbox("OverTime", ["No", "Yes"])
overtime = 1 if overtime == "Yes" else 0

if st.button("Predict"):
input_data = df.iloc[[0]].copy()

input_data['Age'] = age
input_data['MonthlyIncome'] = income
input_data['OverTime'] = overtime

    prob = model.predict_proba(input_data)[0][1]

    st.success(f"Attrition Risk: {prob*100:.2f}%")
