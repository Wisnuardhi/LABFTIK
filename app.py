import streamlit as st
import requests

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🎗️",
    layout="wide"
)

# CSS Custom
st.markdown("""
<style>
.main {
    padding: 2rem;
}
.stButton>button {
    width: 100%;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}
.result-box {
    padding:20px;
    border-radius:10px;
    background-color:#f0f2f6;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🎗️ Breast Cancer Prediction System")
st.markdown("Prediksi kanker payudara menggunakan model **Support Vector Machine (SVM)**")

# Sidebar
with st.sidebar:
    st.header("Informasi")
    st.write("""
    Aplikasi ini digunakan untuk memprediksi
    kemungkinan kanker payudara berdasarkan
    30 fitur input.
    """)

# Layout 2 Kolom
col1, col2 = st.columns([2,1])

inputs = []

with col1:
    st.subheader("Input Features")

    for i in range(30):
        value = st.number_input(
            f"Feature {i+1}",
            value=0.0,
            format="%.4f"
        )
        inputs.append(value)

    predict = st.button("🔍 Predict")

with col2:
    st.subheader("Prediction Result")

    if predict:
        with st.spinner("Processing..."):

            response = requests.post(
                "https://labftik.vercel.app/predict",
                json={"features": inputs}
            )

            hasil = response.json()

            prediction = hasil["prediction"]
            probability = hasil["probability"]

            st.success(f"Prediction: {prediction}")

            st.metric(
                label="Probability",
                value=f"{probability:.2%}"
            )

            st.progress(float(probability))

            st.info(
                f"Tingkat keyakinan model sebesar "
                f"{probability:.2%}"
            )
