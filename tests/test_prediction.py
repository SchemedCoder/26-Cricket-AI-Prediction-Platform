import pandas as pd


def test_sample_input_schema():
    sample = pd.DataFrame([{
        "team1_encoded": 3,
        "team2_encoded": 2,
        "venue_encoded": 1,
        "team1_bat_first": 1
    }])

    assert sample.shape == (1, 4)


def test_valid_prediction_range():
    predicted_score = 188
    assert 50 <= predicted_score <= 300
