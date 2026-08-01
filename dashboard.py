import os
import json
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

LOG_FILE = "logs/events.json"

st.set_page_config(
    page_title="AI Surveillance Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Refresh every second
st_autorefresh(interval=1000, key="dashboard_refresh")

st.title("🛡️ AI Surveillance Dashboard")

# Optional manual refresh button
if st.button("🔄 Refresh Dashboard"):
    st.rerun()

st.success("🟢 AI Engine Status : ONLINE")

st.divider()

# ----------------------------
# Load Events
# ----------------------------

events = []

if os.path.exists(LOG_FILE):
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            events = json.load(file)
    except Exception:
        events = []

# ----------------------------
# Dashboard
# ----------------------------

if len(events) == 0:

    st.info("No suspicious events detected yet.")

else:

    latest = events[-1]

    clip_name = os.path.basename(latest["clip"])

    total_events = len(events)

    avg_fusion = round(
        sum(e["fusion"] for e in events) / total_events,
        2
    )

    max_audio = max(e["audio"] for e in events)

    col1, col2, col3 = st.columns(3)

    # ----------------------------
    # Column 1
    # ----------------------------

    with col1:

        st.metric(
            "👤 People",
            latest["people"]
        )

        st.metric(
            "🔊 Audio",
            f"{latest['audio']:.2f}"
        )

        st.progress(min(float(latest["audio"]), 1.0))

        st.caption(
            f"Audio Level : {latest['audio']:.2f}"
        )

    # ----------------------------
    # Column 2
    # ----------------------------

    with col2:

        st.metric(
            "🧠 Fusion Score",
            f"{latest['fusion']:.2f}"
        )

        fusion = float(latest["fusion"])

        st.progress(min(fusion, 1.0))

        st.caption(f"Fusion Score : {fusion:.2f}")

        if fusion >= 0.75:
            st.caption("Threshold Reached → Recording & Logging Triggered")

        elif fusion >= 0.50:
            st.caption("Potential Activity → Monitoring")

        else:
            st.caption("Normal Activity")

        # ----------------------------
        # Risk Level
        # ----------------------------

        fusion = float(latest["fusion"])

        if fusion >= 0.75:
            st.error("🔴 HIGH RISK")
            st.caption("AI Decision: Suspicious activity detected.")

        elif fusion >= 0.50:
            st.warning("🟡 MEDIUM RISK")
            st.caption("AI Decision: Monitor the situation.")

        else:
            st.success("🟢 LOW RISK")
            st.caption("AI Decision: Environment appears normal.")

    # ----------------------------
    # Column 3
    # ----------------------------

    with col3:

        st.metric(
            "📹 Latest Clip",
            clip_name
        )

        st.metric(
            "🕒 Time",
            latest["time"]
        )

    st.divider()

    # ----------------------------
    # Statistics
    # ----------------------------

    s1, s2, s3 = st.columns(3)

    s1.metric(
        "📊 Total Events",
        total_events
    )

    s2.metric(
        "📈 Avg Fusion",
        f"{avg_fusion:.2f}"
    )

    s3.metric(
        "🎤 Max Audio",
        f"{max_audio:.2f}"
    )

    st.divider()

    # ----------------------------
    # Event History
    # ----------------------------

    st.subheader("📜 Event History")

    df = pd.DataFrame(events[::-1][:10])

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

st.divider()

st.caption(
    "AI Surveillance System Prototype | "
    "Built using Python • OpenCV • YOLOv8 • Kalman Filter • Streamlit"
)