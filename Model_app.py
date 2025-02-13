import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("DicisionTree_model.pkl", "rb"))

def predict_fraud(type_, amount, oldbalanceOrg, newbalanceOrig):
    type_mapping = {"CASH_OUT": 1, "PAYMENT": 2, "CASH_IN": 3, "TRANSFER": 4, "DEBIT": 5}
    val = type_mapping.get(type_, 0)
    
    # Add missing features (use 0 or appropriate default values)
    newbalanceDest = 0  # Change this if needed
    oldbalanceDest = 0  # Change this if needed
    isFlaggedFraud = 0  # Change this if needed

    # Ensure the input has 7 features as required by the model
    input_array = np.array([[val, amount, oldbalanceOrg, newbalanceOrig, newbalanceDest, oldbalanceDest, isFlaggedFraud]])
    prediction = model.predict(input_array)
    return "Fraudulent Transaction" if prediction[0] == 1 else "Legitimate Transaction"

# Streamlit UI
st.title("Online Payments Fraud Detection")

# Sidebar Navigation
page = st.sidebar.selectbox("Select Page", ["Home", "Fraud Prediction"])

if page == "Home":
    st.write("## Welcome to the Fraud Detection System")
    st.write("Use this tool to predict whether a financial transaction is fraudulent or legitimate.")

elif page == "Fraud Prediction":
    st.write("## Predict Fraud Transactions")   
    
    type_ = st.selectbox("Select Transaction Type", ["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT"])
    amount = st.number_input("Enter Transaction Amount", min_value=0.0, format="%.2f")
    oldbalanceOrg = st.number_input("Enter Original Balance", min_value=0.0, format="%.2f")
    newbalanceOrig = st.number_input("Enter New Balance", min_value=0.0, format="%.2f")
    
    if st.button("Predict"):
        result = predict_fraud(type_, amount, oldbalanceOrg, newbalanceOrig)
        st.write(f"### Prediction: {result}")
