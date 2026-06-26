import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor


# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("data/match_features.csv")

# ==========================================
# FEATURE ENGINEERING FOR MODEL
# ==========================================

# Convert categorical columns into numeric
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
# MODEL 1: WINNER CLASSIFICATION
# ==========================================

y_class = df["team1_won"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_class,
    test_size=0.2,
    random_state=42
)

winner_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

winner_model.fit(X_train, y_train)

joblib.dump(
    winner_model,
    "ml/winner_model.pkl"
)

# ==========================================
# MODEL 2: SCORE REGRESSION
# ==========================================

y_reg = df["first_innings_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_reg,
    test_size=0.2,
    random_state=42
)

score_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

score_model.fit(X_train, y_train)

joblib.dump(
    score_model,
    "ml/score_model.pkl"
)

print("Models trained successfully.")
