# Product Price Predictor

A small Streamlit demo based on the supplied 24-row dataset.

## Run locally
1. Install Python.
2. Open a terminal in this folder.
3. Install dependencies:
   `pip install -r requirements.txt`
4. (Optional, if you change products.csv) retrain the model:
   `python train_model.py`
5. Start the app:
   `streamlit run app.py`

## Deploy online
1. Upload all files in this folder to a GitHub repository.
2. Open https://share.streamlit.io/
3. Choose the repository and set the main file path to `app.py`.
4. Deploy.

## Important limitation
The demo predicts price using Month only, so it estimates a month-level average. It does not learn individual product-specific prices. The dataset is tiny and is for learning/demo purposes, not real-world pricing.
