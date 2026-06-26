import pandas as pd


# ==========================================
# LOAD MATCHES
# ==========================================

matches = pd.read_csv("data/matches.csv")


# ==========================================
# FEATURE ENGINEERING
# ==========================================

matches["team1_bat_first"] = (
    matches["bat_first"] == matches["team1"]
).astype(int)

matches["team1_won"] = (
    matches["winner"] == matches["team1"]
).astype(int)

matches["high_scoring_match"] = (
    matches["first_innings_score"] >= 180
).astype(int)


# ==========================================
# SAVE FEATURES
# ==========================================

matches.to_csv(
    "data/match_features.csv",
    index=False
)

print(matches.head())
print("Match features generated.")
