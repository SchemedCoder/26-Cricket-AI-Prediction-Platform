import os
import subprocess
import joblib
import pandas as pd

# ==========================================
# AUTO-TRAIN MODELS IF MISSING
# ==========================================

winner_model_path = "ml/winner_model.pkl"
score_model_path = "ml/score_model.pkl"

if (
    not os.path.exists(winner_model_path)
    or not os.path.exists(score_model_path)
):
    print("Model artifacts not found. Training models...")
    subprocess.run(["python", "ml/train_model.py"])


# ==========================================
# LOAD TRAINED MODELS
# ==========================================

winner_model = joblib.load(winner_model_path)
score_model = joblib.load(score_model_path)


# ==========================================
# SAMPLE MATCH INPUT
# ==========================================

sample = pd.DataFrame([{
    "team1_encoded": 3,
    "team2_encoded": 2,
    "venue_encoded": 1,
    "team1_bat_first": 1
}])


# ==========================================
# PREDICTIONS
# ==========================================

winner_prediction = winner_model.predict(sample)[0]
score_prediction = score_model.predict(sample)[0]

predicted_winner = "Team1" if winner_prediction == 1 else "Team2"

print("Predicted Winner:", predicted_winner)
print("Predicted First Innings Score:", round(score_prediction))
