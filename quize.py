import streamlit as st
import pandas as pd
import time
from streamlit_autorefresh import st_autorefresh
st.title("Quiz Show")

# Refresh every second
st_autorefresh(interval=1000, key="timer")

# Load questions and select random 10 only once
if "quiz" not in st.session_state:
    data = pd.read_csv("questions.csv")
    st.session_state.quiz = data.sample(10).reset_index(drop=True)

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

quiz = st.session_state.quiz

# Timer (10 minutes)
time_limit = 60

elapsed = int(time.time() - st.session_state.start_time)
remaining = time_limit - elapsed

if remaining <= 0:
    remaining = 0

mins = remaining // 60
secs = remaining % 60

st.subheader("⏰ Time Left")
st.write(str(mins) + " min " + str(secs) + " sec")

user_answers = []

for i in range(len(quiz)):

    st.write("Q", i + 1, ":", quiz["question"][i])

    ans = st.radio(
        "Select Answer",
        [
            quiz["option1"][i],
            quiz["option2"][i],
            quiz["option3"][i],
            quiz["option4"][i]
        ],
        key="q" + str(i)
    )

    user_answers.append(ans)
submit = st.button("Submit")
if submit or remaining == 0:
    score = 0
    for i in range(len(quiz)):
        if st.session_state["q" + str(i)] == quiz["answer"][i]:
            score = score + 1
    st.success("Your Score : " + str(score) + " / 10")
    if score >= 8:
        st.balloons()
    else:
        st.snow()

    st.stop()
