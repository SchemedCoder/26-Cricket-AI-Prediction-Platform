import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_error


df = pd.read_csv("data/match_features.csv")

df["team1_encoded"] = df["team1"].astype("category").cat.codes
df["team2_encoded"] = df["team2"].astype("category").cat.codes
df["venue_encoded"] = df["venue_id"].astype("category").cat.codes

features = [
    "team1_encoded",
    "team2_encoded",
    "venue_encoded",
    "team1_bat_first"
]

X = df[features]

# ==========================================
# CLASSIFICATION METRICS
# ==========================================

winner_model = joblib.load("ml/winner_model.pkl")

y_class = df["team1_won"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_class,
    test_size=0.2,
    random_state=42
)

pred = winner_model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("Winner Prediction Accuracy:", accuracy)

# ==========================================
# REGRESSION METRICS
# ==========================================

score_model = joblib.load("ml/score_model.pkl")

y_reg = df["first_innings_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_reg,
    test_size=0.2,
    random_state=42
)

pred = score_model.predict(X_test)

mae = mean_absolute_error(y_test, pred)

print("Score Prediction MAE:", mae)
