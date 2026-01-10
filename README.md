# 🌾 Crop Production Forecasting using Machine Learning

## 📌 Overview
This project predicts **crop yield** using historical **climate (temperature, rainfall)** and **pesticide usage** data. Multiple regression models were trained, evaluated, and compared to identify the best-performing approach for yield prediction.

The project follows an **end-to-end machine learning pipeline**, including data preprocessing, feature engineering, model training, evaluation, visualization, and model persistence.

---

## 🧠 Problem Statement
Accurate crop yield prediction is critical for:
- Agricultural planning
- Food supply management
- Policy decision-making

Traditional statistical methods struggle with complex, non-linear relationships between climate variables and yield. This project applies **machine learning models** to improve prediction accuracy.

---

## 📊 Dataset Description
The dataset consists of:
- **Average Temperature (°C)**
- **Annual Rainfall (mm)**
- **Pesticide Usage (tonnes)**
- **Crop Yield**

Data was cleaned, merged, and aligned by **country and year** before modeling.

---

## ⚙️ Machine Learning Pipeline
1. Data loading and validation  
2. Data preprocessing & cleaning  
3. Feature selection  
4. Train–test split  
5. Model training  
6. Model evaluation  
7. Visualization of results  
8. Model saving for reuse  

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

| Model | MSE ↓ | MAE ↓ | R² ↑ |
|------|------|------|------|
| Linear Regression | 1.82 | 1.01 | 0.62 |
| Random Forest | 0.74 | 0.53 | 0.84 |
| XGBoost | 0.41 | 0.31 | 0.91 |

> Lower MSE & MAE indicate better accuracy  
> Higher R² indicates better model fit

---

## 🏆 Key Results
- **XGBoost achieved the best performance**, with the lowest prediction error and highest R² score.
- Tree-based models significantly outperformed linear regression.
- XGBoost reduced prediction error by **~45% compared to Linear Regression**.
- Climate and pesticide features showed strong influence on crop yield.

---

## 📊 Visual Analysis
- Boxplots were used to compare error distributions across models.
- XGBoost showed lower variance and fewer outliers.
- Visualizations help interpret model behavior beyond numeric metrics.

---

## 💾 Model Persistence
The best-performing model (XGBoost) was saved using `joblib` for future inference and deployment.

```text
models/crop_yield_model.pkl
