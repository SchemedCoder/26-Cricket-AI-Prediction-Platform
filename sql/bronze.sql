-- ==========================================
-- BRONZE LAYER (RAW DATA)
-- ==========================================

CREATE TABLE bronze_matches (
    match_id VARCHAR(20),
    season INT,
    team1 VARCHAR(20),
    team2 VARCHAR(20),
    venue_id VARCHAR(20),
    toss_winner VARCHAR(20),
    bat_first VARCHAR(20),
    winner VARCHAR(20),
    first_innings_score INT
);

CREATE TABLE bronze_players (
    player_id VARCHAR(20),
    player_name VARCHAR(100),
    team VARCHAR(20),
    role VARCHAR(50),
    batting_avg FLOAT,
    strike_rate FLOAT,
    bowling_avg FLOAT,
    economy FLOAT
);

CREATE TABLE bronze_deliveries (
    match_id VARCHAR(20),
    inning INT,
    over_number INT,
    ball_number INT,
    batting_team VARCHAR(20),
    bowler VARCHAR(100),
    batsman VARCHAR(100),
    runs INT,
    wicket INT
);

CREATE TABLE bronze_venues (
    venue_id VARCHAR(20),
    venue_name VARCHAR(100),
    city VARCHAR(50),
    avg_first_innings_score FLOAT,
    pacers_help INT,
    spinners_help INT
);
