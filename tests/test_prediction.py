import joblib
import pandas as pd


def test_prediction_output():

    winner_model = joblib.load("ml/winner_model.pkl")
    score_model = joblib.load("ml/score_model.pkl")

    sample = pd.DataFrame([{
        "team1_encoded": 3,
        "team2_encoded": 2,
        "venue_encoded": 1,
        "team1_bat_first": 1
    }])

    winner = winner_model.predict(sample)[0]
    score = score_model.predict(sample)[0]

    assert winner in [0, 1]
    assert score > 0
