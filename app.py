
import streamlit as st
import pandas as pd
import time
from datetime import datetime
import random

st.set_page_config(layout="wide", page_title="Battle of the Sexes Shootout")

# Sample team data
teams = [
    {"medal": "🥇", "name": "The Allen Wrench", "abbr": "MIN", "yards": 380},
    {"medal": "🥈", "name": "Big Penix Energy", "abbr": "GB", "yards": 355},
    {"medal": "🥉", "name": "Yeah I Suck at Fantasy", "abbr": "BAL", "yards": 322},
    {"medal": "", "name": "Roy The Rocket", "abbr": "LAC", "yards": 300},
    {"medal": "", "name": "Buddy Boyz Dexter", "abbr": "SF", "yards": 289},
    {"medal": "", "name": "Dusted RBs Retirement", "abbr": "TB", "yards": 275}
]

# Big plays
big_plays = [
    {"timestamp": "12:03", "team": "BAL", "play": "22 yd catch"},
    {"timestamp": "12:01", "team": "LAC", "play": "27 yd run"},
    {"timestamp": "11:59", "team": "MIN", "play": "32 yd pass"}
]

# Trash talk
trash_talk = [
    "Big Penix Energy: You’re lucky this week.",
    "Allen Wrench: Watch your back Sunday."
]

# Title
st.markdown("<h1 style='text-align: center; color: white;'>🏆 Battle of the Sexes Shootout</h1>", unsafe_allow_html=True)

# Layout
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.markdown("### 💬 Trash Talk")
    for line in trash_talk:
        st.markdown(f"- {line}")
    st.text_input("Send a jab...", "")

with col3:
    st.markdown("### 🚀 Big Plays")
    for play in big_plays:
        st.markdown(f"**{play['timestamp']} - {play['team']}**: {play['play']}")

with col2:
    st.markdown("### Live Yardage Leaderboard")
    for team in sorted(teams, key=lambda x: -x["yards"]):
        bar = st.progress(min(team["yards"], 400) / 400)
        st.markdown(f"{team['medal']} **{team['name']} ({team['abbr']})** – {team['yards']} yards")

# Auto-refresh simulation
time.sleep(30)
