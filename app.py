import streamlit as st
import joblib
import pandas as pd
import numpy as np

# --------------------------
# Load artifacts
# --------------------------
MODEL_FILE = "gradient_boosting_model.pkl"
SCALER_FILE = "scaler.pkl"
FEATURES_FILE = "model_features.pkl"

model = joblib.load(MODEL_FILE)
scaler = joblib.load(SCALER_FILE)
model_features = joblib.load(FEATURES_FILE)

# --------------------------
# Define categorical and numeric features
# --------------------------
categorical_inputs = {
    "Water Source Type": ["Lake", "Well", "Pond", "Tap", "River", "Spring"],
    "Water Treatment Method": ["Filtration", "Boiling", "Chlorination"],
    "Region": ["North", "West", "Central", "East", "South"],
}

numeric_inputs = [
    "Contaminant Level (ppm)",
    "pH Level",
    "Turbidity (NTU)",
    "Dissolved Oxygen (mg/L)",
    "Nitrate Level (mg/L)",
    "Lead Concentration (µg/L)",
    "Bacteria Count (CFU/mL)",
    "Access to Clean Water (% of Population)",
    "GDP per Capita (USD)",
    "Healthcare Access Index (0-100)",
    "Urbanization Rate (%)",
    "Sanitation Coverage (% of Population)",
    "Rainfall (mm per year)",
    "Temperature (°C)",
    "Population Density (people per km²)",
]

# --------------------------
# Page setup
# --------------------------
st.set_page_config(page_title="Cholera Risk Prediction", page_icon="💧", layout="wide")
st.title("Cholera Risk Prediction")
st.write("Fill in the form below and click **Submit** to see the prediction.")

# --------------------------
# Input Form
# --------------------------
with st.form("prediction_form"):

    # --- Categorical inputs first
    st.subheader("Categorical Inputs")
    user_cats = {}
    for label, choices in categorical_inputs.items():
        selection = st.selectbox(label, ["Unknown/Other"] + choices, index=0)
        user_cats[label] = selection

    # --- Numeric inputs
    st.subheader("Numeric Inputs")
    user_numeric = {}
    for f in numeric_inputs:
        if f == "pH Level":
            user_numeric[f] = st.number_input(f, min_value=0.0, max_value=14.0, value=7.0, step=0.1)
        elif "%" in f or "Index" in f or "Rate" in f:
            user_numeric[f] = st.number_input(f, min_value=0.0, max_value=100.0, value=50.0)
        elif "Temperature" in f:
            user_numeric[f] = st.number_input(f, min_value=-10.0, max_value=50.0, value=25.0)
        elif "Rainfall" in f:
            user_numeric[f] = st.number_input(f, min_value=0.0, value=500.0)
        else:
            user_numeric[f] = st.number_input(f, value=0.0)

    # --- Submit button
    submitted = st.form_submit_button("Submit")

# --------------------------
# Run prediction when submitted
# --------------------------
if submitted:
    # Build input row
    input_row = pd.DataFrame(np.zeros((1, len(model_features)), dtype=float), columns=model_features)

    # Fill numeric values
    for f, val in user_numeric.items():
        if f in input_row.columns:
            input_row.at[0, f] = float(val)

    # Fill categorical values
    for label, selection in user_cats.items():
        if selection == "Unknown/Other":
            continue
        col_name = f"{label}_{selection}"
        if col_name in input_row.columns:
            input_row.at[0, col_name] = 1.0

    # Scale numeric features
    try:
        numeric_features_in_model = [f for f in numeric_inputs if f in input_row.columns]
        if numeric_features_in_model:
            input_row[numeric_features_in_model] = scaler.transform(input_row[numeric_features_in_model])
    except Exception as e:
        st.error(f"Scaler transform failed: {e}")
        st.stop()

    # Prediction
    try:
        pred = model.predict(input_row)[0]
        proba = model.predict_proba(input_row)[0] if hasattr(model, "predict_proba") else None
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.stop()

    # Show results
    st.subheader("Prediction Result")
    if pred == 1:
        st.error("High Risk of Cholera")
    else:
        st.success("Low Risk of Cholera")

    if proba is not None:
        st.write("Prediction probabilities:")
        st.write(f"- Low risk: {proba[0]*100:.2f}%")
        st.write(f"- High risk: {proba[1]*100:.2f}%")

    # Debug: Show feature row (optional)
    with st.expander("See processed feature vector"):
        st.dataframe(input_row.T)

