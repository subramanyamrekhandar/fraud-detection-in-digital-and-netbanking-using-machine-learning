import streamlit as st
import pandas as pd

# Streamlit UI
st.title("Online Payments Fraud Detection")

uploaded_file = st.file_uploader("Upload Transaction Dataset (CSV)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Dataset")
    st.write(df)
    
    type_ = st.selectbox("Select Transaction Type", df['type'].unique())
    amount = st.number_input("Enter Transaction Amount", min_value=0.0, format="%.2f")
    oldbalanceOrg = st.number_input("Enter Original Balance", min_value=0.0, format="%.2f")
    newbalanceOrig = st.number_input("Enter New Balance", min_value=0.0, format="%.2f")
    
    if st.button("Check Fraud"):
        match = df[(df['type'] == type_) & 
                   (df['amount'] == amount) & 
                   (df['oldbalanceOrg'] == oldbalanceOrg) & 
                   (df['newbalanceOrig'] == newbalanceOrig)]
        
        if not match.empty:
            fraud_status = "Fraudulent Transaction" if match['isFraud'].iloc[0] == 1 else "Valid Transaction"
            st.write(f"### Alert: {fraud_status}")
        else:
            st.write("### No matching transaction found in dataset")