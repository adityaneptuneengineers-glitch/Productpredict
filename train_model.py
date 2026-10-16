import pandas as pd
import joblib
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "products.csv")

preprocessor = ColumnTransformer(
    transformers=[("month", OneHotEncoder(handle_unknown="ignore"), ["Month"])],
    remainder="drop"
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

model.fit(df[["Month"]], df["price"])
joblib.dump(model, BASE_DIR / "model.pkl")
print("Model trained and saved as model.pkl")
