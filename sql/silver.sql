-- ==========================================
-- SILVER LAYER (CLEANED + FEATURED)
-- ==========================================

CREATE TABLE silver_match_features AS
SELECT
    match_id,
    season,
    team1,
    team2,
    venue_id,
    toss_winner,
    bat_first,
    winner,
    first_innings_score,
    CASE
        WHEN bat_first = team1 THEN 1
        ELSE 0
    END AS team1_bat_first,
    CASE
        WHEN winner = team1 THEN 1
        ELSE 0
    END AS team1_won
FROM bronze_matches;


CREATE TABLE silver_player_features AS
SELECT
    player_id,
    player_name,
    team,
    role,
    batting_avg,
    strike_rate,
    bowling_avg,
    economy,
    batting_avg * strike_rate AS batting_strength
FROM bronze_players;
