# lab-test-recommender
AI-Powered Lab Test Recommender (Streamlit App)
# 🧪 AI-Powered Lab Test Recommender

An interactive Streamlit-based machine learning application that recommends suitable diagnostic lab tests based on patient age, gender, and symptoms.

## 🚀 Overview

This project aims to demonstrate a clinical decision-support system using machine learning. The model predicts which lab test (e.g., CBC, MRI, X-Ray) is most appropriate based on user inputs. It’s ideal for learning AI implementation in healthcare and showcasing ML app deployment with Streamlit.

## 🎯 Features

- Accepts patient inputs: Age, Gender, and Symptom
- Uses a trained Random Forest Classifier for prediction
- Instant lab test recommendation with one click
- Clean and responsive Streamlit user interface
- Fully compatible with deployment on [Streamlit Cloud](https://streamlit.io/cloud)

## 🧰 Tech Stack

- Python 3
- Streamlit
- scikit-learn
- pandas
- joblib

## 📂 Project Structure

ab-test-recommender/
├── app.py # Streamlit app interface
├── model.pkl # Trained ML model
├── le_gender.pkl # LabelEncoder for gender
├── le_symptom.pkl # LabelEncoder for symptoms
├── le_test.pkl # LabelEncoder for lab tests
├── requirements.txt # Dependencies for Streamlit Cloud
└── README.md # Project documentation
##how to run
goto anaconda prompt-
cd lab-test-recommender

streamlit run app.py

Then visit 👉 http://localhost:8501
<img width="1762" height="890" alt="image" src="https://github.com/user-attachments/assets/322def7c-e3b5-4cb0-89de-fb3cba5166a7" />
<img width="1610" height="937" alt="image" src="https://github.com/user-attachments/assets/43cfd827-3997-4f14-aefc-6e1710981214" />

