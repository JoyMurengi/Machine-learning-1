# Water Pollution & Disease Prediction  

## Overview  
Access to clean and safe water is a critical public health concern in Kenya and many parts of the world. Contaminated water sources contribute to waterborne diseases such as cholera, typhoid, and diarrhea.  

This project applies machine learning techniques to predict the risk of waterborne diseases based on water pollution indicators, enabling early interventions and informed public health decision-making.  

---

## Problem Statement  
The goal of this project is to predict the occurrence or risk of waterborne diseases using pollution measurements.  

By identifying high-risk areas early, stakeholders can:  
- Allocate resources more efficiently  
- Implement targeted interventions  
- Reduce disease incidence rates  

---

## Dataset  
- **Source**: Kaggle — Water Pollution & Disease  
- **Size**: ~3,000 rows  
- **Features**: 24 variables (chemical, physical, and microbial water indicators)  
- **Target**:  
  - **Classification**: Presence/absence of disease  
  - **Regression**: Incidence rate of disease  

---

## Methodology  

### 1. Data Preprocessing  
- Handled missing values  
- Encoded categorical features  
- Normalized/scaled numerical features  

### 2. Exploratory Data Analysis (EDA)  
- Analyzed distributions of features & target variable  
- Identified correlations between pollution indicators and disease  
- Created visualizations for insights  

### 3. Feature Engineering  
- Built interaction features  
- Reduced multicollinearity  
- Selected important predictors for better model performance  

### 4. Modeling  
- **Baseline models**: Logistic Regression / Linear Regression  
- **Advanced models**: Random Forest, Gradient Boosting, XGBoost  

### 5. Evaluation  
- **Classification**: Accuracy, Precision, Recall, F1-Score, ROC-AUC  
- **Regression**: RMSE, MAE, R²  

### 6. Interpretation  
- Feature importance analysis  
- Explainability using SHAP values and permutation importance  

---

## Results  
- Gradient Boosting and XGBoost outperformed baseline models.  
- Key pollution indicators such as microbial counts and chemical concentrations were the strongest predictors of disease prevalence.  

---

## Deployment  
The project includes:  
- **Interactive Streamlit App** for live model predictions  
- **Presentation Website (Lovable)** with  
    

---

## Expected Impact  
- Early detection of high-risk areas for waterborne diseases  
- Improved public health monitoring and timely response  
- Insights into key pollution factors driving disease prevalence  

---

## Target Audience  
- Public health organizations  
- Government agencies and NGOs  
- Data scientists and researchers in health and environment  
- Policy makers working in water and sanitation sectors  

 
