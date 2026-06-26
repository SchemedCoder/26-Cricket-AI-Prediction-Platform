import pandas as pd


# ==========================================
# LOAD PLAYER DATA
# ==========================================

players = pd.read_csv("data/players.csv")


# ==========================================
# PLAYER FEATURES
# ==========================================

players["batting_strength"] = (
    players["batting_avg"] * players["strike_rate"]
)

players["bowling_strength"] = (
    players["bowling_avg"].replace(0, 999)
)

players["all_rounder_score"] = (
    players["batting_avg"] +
    players["strike_rate"] / 10 +
    players["economy"].replace(0, 10)
)


# ==========================================
# SAVE FEATURES
# ==========================================

players.to_csv(
    "data/player_features.csv",
    index=False
)

print(players.head())
print("Player features generated.")
