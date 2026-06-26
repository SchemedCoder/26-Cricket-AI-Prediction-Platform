import joblib
import pandas as pd


winner_model = joblib.load("ml/winner_model.pkl")
score_model = joblib.load("ml/score_model.pkl")


# Example prediction
sample = pd.DataFrame([{
    "team1_encoded": 3,
    "team2_encoded": 2,
    "venue_encoded": 1,
    "team1_bat_first": 1
}])


winner = winner_model.predict(sample)[0]
score = score_model.predict(sample)[0]

if winner == 1:
    predicted_winner = "Team1"
else:
    predicted_winner = "Team2"

print("Predicted Winner:", predicted_winner)
print("Predicted First Innings Score:", round(score))
