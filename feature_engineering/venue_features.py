import pandas as pd


# ==========================================
# LOAD VENUE DATA
# ==========================================

venues = pd.read_csv("data/venues.csv")


# ==========================================
# VENUE FEATURES
# ==========================================

venues["pitch_type"] = venues.apply(
    lambda row: "PACE"
    if row["pacers_help"] > row["spinners_help"]
    else "SPIN",
    axis=1
)

venues["high_scoring_ground"] = (
    venues["avg_first_innings_score"] >= 180
).astype(int)


# ==========================================
# SAVE FEATURES
# ==========================================

venues.to_csv(
    "data/venue_features.csv",
    index=False
)

print(venues.head())
print("Venue features generated.")
