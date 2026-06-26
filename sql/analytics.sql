-- ==========================================
-- TOP WINNING TEAMS
-- ==========================================

SELECT
    winner,
    COUNT(*) AS wins
FROM bronze_matches
GROUP BY winner
ORDER BY wins DESC;


-- ==========================================
-- AVG FIRST INNINGS SCORE BY VENUE
-- ==========================================

SELECT
    v.venue_name,
    AVG(m.first_innings_score) AS avg_score
FROM bronze_matches m
JOIN bronze_venues v
ON m.venue_id = v.venue_id
GROUP BY v.venue_name
ORDER BY avg_score DESC;


-- ==========================================
-- TOP BATSMEN
-- ==========================================

SELECT
    player_name,
    batting_avg,
    strike_rate
FROM bronze_players
ORDER BY batting_avg DESC
LIMIT 5;
