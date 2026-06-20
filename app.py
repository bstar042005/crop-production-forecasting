import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import google.generativeai as genai
from dotenv import load_dotenv
import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


# =====================================
# GEMINI CONFIG
# =====================================

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

gemini = genai.GenerativeModel(
    "gemini-2.5-flash"
)


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Crop Yield Forecasting",
    layout="wide"
)


# =====================================
# PDF REPORT FUNCTION
# =====================================

def generate_report(country, crop, year, prediction):

    filename = "crop_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Crop Yield Prediction Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            f"Country: {country}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Crop: {crop}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Year: {year}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Predicted Yield: {prediction:,.2f}",
            styles["Normal"]
        )
    )

    doc.build(elements)

    return filename


# =====================================
# LOAD MODEL
# =====================================

model = joblib.load(
    "models/best_crop_yield_model.pkl"
)


# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(
    "data/processed_crop_data.csv"
)

columns = df.columns.tolist()

if "Yield" in columns:
    columns.remove("Yield")


# =====================================
# COUNTRIES AND CROPS
# =====================================

countries = sorted([
    col.replace("Area_", "")
    for col in columns
    if col.startswith("Area_")
])

crops = sorted([
    col.replace("Item_", "")
    for col in columns
    if col.startswith("Item_")
])


# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("Crop Yield Forecasting")

st.sidebar.markdown("""
### About

Predict crop yield using:

- Rainfall Data
- Temperature Data
- Pesticide Usage
- Country Information
- Crop Type

---

### Features

Yield Prediction

AI Farming Assistant

Feature Importance Analysis

PDF Report Generation

---

### Model Information

**Model:** XGBoost Regressor

**R² Score:** 0.91

**Countries:** 100

**Crop Types:** 9
""")



# =====================================
# MAIN TITLE
# =====================================

st.title(
    "Crop Yield Forecasting"
)

st.info(
    "Predict crop yield using climate conditions, pesticide usage, country, and crop type."
)



# =====================================
# INPUTS
# =====================================

st.subheader(
    "Enter Input Parameters"
)

left, right = st.columns(2)

with left:

    year = st.number_input(
        "Year",
        min_value=1990,
        max_value=2050,
        value=2025
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        value=1000.0
    )

    temp = st.number_input(
        "Average Temperature (°C)",
        min_value=-20.0,
        value=25.0
    )

with right:

    pesticides = st.number_input(
        "Pesticides Usage",
        min_value=0.0,
        value=100.0
    )

    country = st.selectbox(
        "Country",
        countries
    )

    crop = st.selectbox(
        "Crop",
        crops
    )


# =====================================
# PREDICTION
# =====================================

if st.button("Predict Yield"):

    input_data = pd.DataFrame(
        np.zeros((1, len(columns))),
        columns=columns
    )

    input_data["Year"] = year
    input_data["Rainfall"] = rainfall
    input_data["Avg_Temp"] = temp
    input_data["Pesticides"] = pesticides

    area_col = f"Area_{country}"

    if area_col in input_data.columns:
        input_data[area_col] = 1

    crop_col = f"Item_{crop}"

    if crop_col in input_data.columns:
        input_data[crop_col] = 1

    prediction = model.predict(
        input_data
    )[0]

    st.session_state["prediction"] = prediction

    st.success(
        "Prediction Generated Successfully"
    )

    m1, m2 = st.columns(2)

    with m1:

        st.metric(
            "Predicted Yield",
            f"{prediction:,.2f}"
        )


    st.info(
        f"""
        Predicted Yield for **{crop}**
        in **{country}**
        during **{year}**
        is approximately **{prediction:,.2f}**.
        """
    )

    # PDF REPORT

    report_file = generate_report(
        country,
        crop,
        year,
        prediction
    )

    with open(report_file, "rb") as file:

        st.download_button(
            "Download Prediction Report",
            data=file,
            file_name="crop_report.pdf",
            mime="application/pdf"
        )

    # FEATURE IMPORTANCE

    st.subheader(
        "Feature Importance Analysis"
    )

    try:

        importance_df = pd.DataFrame({
            "Feature": columns,
            "Importance": model.feature_importances_
        })

        importance_df = (
            importance_df
            .sort_values(
                "Importance",
                ascending=False
            )
            .head(10)
        )

        fig = px.bar(
            importance_df,
            x="Importance",
            y="Feature",
            orientation="h",
            title="Top 10 Important Features"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    except Exception:

        st.warning(
            "Feature importance not available."
        )


# =====================================
# AI ASSISTANT
# =====================================

st.divider()

st.subheader("AI Farming Assistant")

user_question = st.text_input(
    "Ask a farming question"
)

if st.button("Ask AI"):

    prediction_value = st.session_state.get(
        "prediction",
        "Unknown"
    )

    prompt = f"""
    Crop: {crop}
    Country: {country}
    Predicted Yield: {prediction_value}

    Farmer Question:
    {user_question}

    Give practical farming advice.
    """

    try:

        response = gemini.generate_content(
            prompt
        )

        st.write(
            response.text
        )

    except Exception as e:

        st.error(
            f"Gemini Error: {e}"
        )