import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "products.csv"
MODEL_PATH = BASE_DIR / "model.pkl"

st.set_page_config(page_title="Product Price Predictor", page_icon="🛒", layout="wide")
st.title("🛒 Product Price Predictor")
st.write("Choose a month to estimate the average product price from the sample dataset.")

df = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH)

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

selected_month = st.selectbox("Select month", months)

if st.button("Predict price", type="primary"):
    predicted_price = float(model.predict(pd.DataFrame({"Month": [selected_month]}))[0])
    discounted_price = predicted_price * 0.90

    col1, col2 = st.columns(2)
    col1.metric("Predicted price", f"₹{predicted_price:,.2f}")
    col2.metric("Price after 10% discount", f"₹{discounted_price:,.2f}")

    st.caption(
        "Demo only: this model estimates a month-level average from just 24 sample rows. "
        "It does not predict the price of a specific product and should not be used for real pricing."
    )

st.subheader("Dataset")
st.dataframe(df, use_container_width=True)

st.subheader("Summary by month")
summary = df.groupby("Month", as_index=False)["price"].mean()
summary = summary.rename(columns={"price": "Average price"})
st.dataframe(summary, use_container_width=True)
