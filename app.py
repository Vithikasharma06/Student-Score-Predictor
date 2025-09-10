import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

model = joblib.load("best_model.pkl")
Student = st
st.title("Student Exam Score Predictor")

study_hours = st.slider("Study Hours Per Day", 0.0, 12.0, 2.0)
attendance = st.slider("Attendance Percentage", 0.0, 100.0, 80.0)
mental_health = st.slider("Mental Health Rating (1-10)", 1, 10, 5)
sleep_hours = st.slider("Sleep Hours Per Night", 0.0, 12.0, 7.0)
part_time_job = st.selectbox("Part-Time Job", ["No", "Yes"])

ptj_encoder = 1 if part_time_job == "Yes" else 0

if st.button("Predict Exam Score"):
    input_data = np.array([[study_hours, attendance, mental_health, sleep_hours, ptj_encoder]])
    prediction = model.predict(input_data)[0]
    
    prediction = max(0, min(100, prediction))
    
    st.success(f"Predicted Exam Score: {prediction:.2f}")
    
    