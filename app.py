import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("model.pkl")
le_gender = joblib.load("le_gender.pkl")
le_symptom = joblib.load("le_symptom.pkl")
le_test = joblib.load("le_test.pkl")

st.set_page_config(page_title="Lab Test Recommender", page_icon="🧪")
st.title("🧠 AI-Powered Lab Test Recommender")

age = st.number_input("Enter Age", min_value=0, max_value=120, value=30)
gender = st.selectbox("Select Gender", le_gender.classes_)
symptom = st.selectbox("Select Symptom", le_symptom.classes_)

if st.button("Predict Recommended Test"):
    input_data = {
        'Age': age,
        'Gender': le_gender.transform([gender])[0],
        'Symptom': le_symptom.transform([symptom])[0]
    }
    X_input = pd.DataFrame([input_data])
    prediction = model.predict(X_input)[0]
    recommended_test = le_test.inverse_transform([prediction])[0]
    
    st.success(f"✅ Recommended Lab Test: **{recommended_test}**")
