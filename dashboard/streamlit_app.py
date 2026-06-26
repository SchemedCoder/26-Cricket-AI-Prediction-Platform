import os
import subprocess
import joblib
import pandas as pd
import streamlit as st


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Cricket AI Prediction Platform",
    layout="wide"
)

st.title("🏏 Cricket AI Prediction Platform")
st.write("Predict match winner and first innings score using ML")


# ==========================================
# LOAD MODELS
# ==========================================

winner_model_path = "ml/winner_model.pkl"
score_model_path = "ml/score_model.pkl"

if (
    not os.path.exists(winner_model_path)
    or not os.path.exists(score_model_path)
):
    st.warning("Models missing. Training models...")
    subprocess.run(["python", "ml/train_model.py"])

winner_model = joblib.load(winner_model_path)
score_model = joblib.load(score_model_path)


# ==========================================
# INPUTS
# ==========================================

teams = ["MI", "CSK", "RCB", "KKR", "RR", "PBKS", "SRH", "DC"]
venues = ["V001", "V002", "V003", "V004"]

team1 = st.selectbox("Select Team 1", teams)
team2 = st.selectbox("Select Team 2", teams)
venue = st.selectbox("Select Venue", venues)
bat_first = st.radio("Who bats first?", [team1, team2])


# ==========================================
# SIMPLE ENCODING
# ==========================================

team_mapping = {
    "MI": 0,
    "CSK": 1,
    "RCB": 2,
    "KKR": 3,
    "RR": 4,
    "PBKS": 5,
    "SRH": 6,
    "DC": 7
}

venue_mapping = {
    "V001": 0,
    "V002": 1,
    "V003": 2,
    "V004": 3
}


# ==========================================
# PREDICTION BUTTON
# ==========================================

if st.button("Predict Match"):

    sample = pd.DataFrame([{
        "team1_encoded": team_mapping[team1],
        "team2_encoded": team_mapping[team2],
        "venue_encoded": venue_mapping[venue],
        "team1_bat_first": 1 if bat_first == team1 else 0
    }])

    winner_prediction = winner_model.predict(sample)[0]
    score_prediction = score_model.predict(sample)[0]

    predicted_winner = team1 if winner_prediction == 1 else team2

    probabilities = winner_model.predict_proba(sample)[0]
    team1_prob = round(probabilities[1] * 100, 2)
    team2_prob = round(probabilities[0] * 100, 2)

    st.success(f"Predicted Winner: {predicted_winner}")
    st.metric("Predicted First Innings Score", round(score_prediction))

    st.subheader("Win Probability")
    st.write(f"{team1}: {team1_prob}%")
    st.progress(team1_prob / 100)

    st.write(f"{team2}: {team2_prob}%")
    st.progress(team2_prob / 100)
