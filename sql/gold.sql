-- ==========================================
-- GOLD LAYER (PREDICTIONS)
-- ==========================================

CREATE TABLE gold_match_predictions (
    prediction_id INT,
    team1 VARCHAR(20),
    team2 VARCHAR(20),
    predicted_winner VARCHAR(20),
    predicted_score INT,
    win_probability FLOAT,
    prediction_timestamp TIMESTAMP
);

CREATE TABLE gold_player_predictions (
    prediction_id INT,
    player_name VARCHAR(100),
    predicted_runs FLOAT,
    predicted_wickets FLOAT,
    confidence_score FLOAT,
    prediction_timestamp TIMESTAMP
);
