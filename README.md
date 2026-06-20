# Smart Crop Yield Forecasting Dashboard

An AI-powered crop yield prediction platform that helps estimate agricultural production using climate conditions, pesticide usage, crop type, and geographical data. The project combines Machine Learning, Explainable AI, and Generative AI to provide intelligent farming insights through an interactive web dashboard.

---

## Live Demo

🔗 **Live Application:** [https://crop-appuction-forecasting-7e7edbus735vzhckmwqtsd.streamlit.app/]

---

## Project Overview

Accurate crop yield prediction is essential for:

* Agricultural planning
* Food supply management
* Resource optimization
* Policy decision-making
* Sustainable farming practices

Traditional statistical approaches often struggle with complex, non-linear relationships between environmental factors and crop production. This project leverages machine learning models to improve prediction accuracy and provide actionable insights for farmers and agricultural stakeholders.

---

## Features

### Crop Yield Prediction

Predict crop yield based on:

* Year
* Rainfall
* Average Temperature
* Pesticide Usage
* Country
* Crop Type

### Feature Importance Analysis

Visualize the most influential factors affecting crop yield using XGBoost feature importance.

### AI Farming Assistant

Powered by Google Gemini AI.

Users can ask farming-related questions such as:

* Why is my yield low?
* How can I improve wheat production?
* What farming practices should I follow?

### PDF Report Generation

Generate and download prediction reports containing:

* Selected Country
* Crop Type
* Input Parameters
* Predicted Yield

### Interactive Dashboard

Built using Streamlit for an intuitive and user-friendly experience.

---

## System Architecture

Data Collection
↓
Data Preprocessing
↓
Feature Engineering
↓
Model Training
↓
XGBoost Model Selection
↓
Streamlit Dashboard
↓
Yield Prediction
↓
AI Recommendations & PDF Reports

---

## Dataset Information

The dataset includes:

* Annual Rainfall (mm)
* Average Temperature (°C)
* Pesticide Usage (tonnes)
* Crop Yield
* Country Information
* Crop Information

Data was cleaned, merged, and transformed using feature engineering and one-hot encoding techniques.

---

## Machine Learning Models Evaluated

### Linear Regression

Baseline regression model.

### Random Forest Regressor

Ensemble tree-based learning model.

### XGBoost Regressor

Gradient boosting model selected as the final deployment model.

---

## Model Performance

| Model             | MSE           | MAE      | R² Score |
| ----------------- | ------------- | -------- | -------- |
| Linear Regression | 1847708880.21 | 30010.20 | 0.749    |
| Random Forest     | 86606223.19   | 3345.52  | 0.988    |
| XGBoost           | 625723648.00  | 14873.79 | 0.915    |

### Selected Model

 **XGBoost Regressor**

Reasons:

* Highest predictive performance
* Strong handling of non-linear relationships
* Robust feature importance analysis
* Suitable for deployment

---

## Tech Stack

### Machine Learning

* Python
* Scikit-learn
* XGBoost
* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib

### Web Application

* Streamlit

### AI Assistant

* Google Gemini API

### Reporting

* ReportLab

### Version Control

* Git
* GitHub

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/crop-production-forecasting.git

cd crop-production-forecasting
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create `.env`

```env
GEMINI_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

---

## Project Structure

```text
crop-production-forecasting/
│
├── data/
│   ├── processed_crop_data.csv
│   ├── rainfall.csv
│   ├── pesticides.csv
│   ├── temp.csv
│   └── yield.csv
│
├── models/
│   └── best_crop_yield_model.pkl
│
├── notebooks/
│   └── data_preprocessing.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

## Author

**Bhavya Vaish**

##  Support

If you found this project useful, consider giving it a star ⭐ on GitHub.
