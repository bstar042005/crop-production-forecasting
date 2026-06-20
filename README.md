# 🌾 Crop Yield Prediction using Machine Learning

## 📌 Overview
This project focuses on predicting **crop yield** using historical **climate and agricultural input data**, including rainfall, temperature, and pesticide usage.  
Multiple regression models were trained, evaluated, and compared, with **XGBoost achieving the best performance**.

The project demonstrates a complete **end-to-end machine learning pipeline** from data preprocessing to model evaluation and comparison.

---

## 🎯 Problem Statement
Accurate crop yield prediction is essential for:
- Agricultural planning
- Food security
- Policy and decision-making

The goal of this project is to build and compare machine learning models that can effectively predict crop yield based on environmental and agricultural factors.

---

## 📊 Dataset
The dataset includes:
- Annual rainfall (mm)
- Average temperature (°C)
- Pesticide usage (tonnes)
- Crop yield

The data was cleaned, standardized, and merged using common spatial (Area) and temporal (Year) keys.

---

## ⚙️ Machine Learning Pipeline
1. Data loading and preprocessing  
2. Feature engineering and selection  
3. Train–test split  
4. Model training  
5. Model evaluation  
6. Visualization of results  
7. Model comparison and selection  

---

## 🤖 Models Used
- Linear Regression  
- Random Forest Regressor  
- XGBoost Regressor  

---

## 📏 Evaluation Metrics
Models were evaluated using:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- R² Score

---

## 📈 Model Performance Comparison

| Model              | MSE ↓ | MAE ↓ | R² ↑ |
|-------------------|-------|-------|------|
| Linear Regression | 1.82  | 1.01  | 0.62 |
| Random Forest     | 0.74  | 0.53  | 0.84 |
| XGBoost           | 0.41  | 0.31  | 0.91 |

> Lower MSE and MAE indicate better accuracy, while a higher R² score indicates a better model fit.

---

## 🏆 Key Results
- XGBoost achieved the **lowest prediction error** and **highest R² score**
- Tree-based models significantly outperformed Linear Regression
- Rainfall and pesticide usage were the most influential features
- XGBoost reduced prediction error by approximately **45%** compared to Linear Regression

---

## 📊 Visualizations
The project includes:
- Boxplots comparing prediction error distributions
- Actual vs Predicted Yield plots
- Residual analysis
- Feature importance analysis for tree-based models

These visualizations help interpret model performance and stability.

---

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Matplotlib, Seaborn  
- Jupyter Notebook  

---

## 📁 Project Structure
