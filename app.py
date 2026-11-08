
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="CampusPulse Dashboard",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #080d1a, #111827);
    color: #f8fafc;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #26334d;
}

h1, h2, h3, p, label {
    color: #f8fafc !important;
}

.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #a5b4fc;
}

.subtitle {
    color: #94a3b8;
    font-size: 16px;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, #172554, #312e81);
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #4338ca;
    box-shadow: 0 5px 18px rgba(0,0,0,0.25);
}

[data-testid="stMetricLabel"] {
    color: #cbd5e1 !important;
}

[data-testid="stMetricValue"] {
    color: #c4b5fd !important;
    font-weight: bold;
}

[data-testid="stMetricDelta"] {
    color: #86efac !important;
}

.stButton button, .stDownloadButton button {
    background: linear-gradient(90deg, #4f46e5, #9333ea);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 8px 18px;
}

.stButton button:hover, .stDownloadButton button:hover {
    background: linear-gradient(90deg, #6366f1, #a855f7);
    color: white;
    border: none;
}

[data-testid="stDataFrame"] {
    border: 1px solid #334155;
    border-radius: 12px;
}

hr {
    border-color: #334155;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# LOAD DATA
# --------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("analysis_results.csv")

try:
    df = load_data()
except FileNotFoundError:
    st.error("analysis_results.csv not found. Keep it in the same folder as app.py.")
    st.stop()
except Exception as error:
    st.error(f"Unable to load dataset: {error}")
    st.stop()

required_columns = [
    "Study_Hours",
    "Attendance",
    "Final_Score",
    "Performance"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    st.error(f"Missing columns in dataset: {missing_columns}")
    st.stop()

# --------------------------------
# SIDEBAR
# --------------------------------

st.sidebar.markdown("## 🎓 CampusPulse")
st.sidebar.markdown("---")

st.sidebar.markdown("### Dashboard Navigation")
st.sidebar.info("Student Lifestyle & Academic Insights")

performance_options = ["All"] + sorted(
    df["Performance"].dropna().astype(str).unique().tolist()
)

selected_performance = st.sidebar.selectbox(
    "Filter by Performance",
    performance_options
)

if selected_performance == "All":
    filtered_df = df.copy()
else:
    filtered_df = df[
        df["Performance"].astype(str) == selected_performance
    ].copy()

st.sidebar.markdown("---")
st.sidebar.write(f"Total records: {len(filtered_df)}")
st.sidebar.caption("CampusPulse | Student Analytics")

# --------------------------------
# TITLE
# --------------------------------

st.markdown(
    '<div class="main-title">🎓 CampusPulse</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Student Lifestyle & Academic Insights Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown("---")

if filtered_df.empty:
    st.warning("No student records found for this filter.")
    st.stop()

# --------------------------------
# KPI CARDS
# --------------------------------

st.markdown("## 📊 Academic Overview")

total_students = len(filtered_df)
average_score = filtered_df["Final_Score"].mean()
average_attendance = filtered_df["Attendance"].mean()

if "Study_Hours" in filtered_df.columns:
    average_study_hours = filtered_df["Study_Hours"].mean()
else:
    average_study_hours = 0

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Students",
    f"{total_students}"
)

col2.metric(
    "Average Score",
    f"{average_score:.2f}"
)

col3.metric(
    "Average Attendance",
    f"{average_attendance:.2f}%"
)

col4.metric(
    "Average Study Hours",
    f"{average_study_hours:.2f}"
)

st.markdown("---")

# --------------------------------
# CHART STYLE
# --------------------------------

sns.set_theme(style="darkgrid")

def style_chart(fig, ax):
    fig.patch.set_facecolor("#111827")
    ax.set_facecolor("#1e293b")

    ax.tick_params(colors="#e2e8f0")
    ax.xaxis.label.set_color("#e2e8f0")
    ax.yaxis.label.set_color("#e2e8f0")
    ax.title.set_color("#c4b5fd")

    for spine in ax.spines.values():
        spine.set_color("#475569")

# --------------------------------
# CHART 1: PERFORMANCE DISTRIBUTION
# --------------------------------

st.markdown("## 📈 Student Performance Analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Performance Distribution")

    fig1, ax1 = plt.subplots(figsize=(7, 4))

    sns.countplot(
        data=filtered_df,
        x="Performance",
        color="#818cf8",
        ax=ax1
    )

    ax1.set_xlabel("Performance Grade")
    ax1.set_ylabel("Number of Students")
    ax1.set_title("Student Performance Distribution")

    style_chart(fig1, ax1)
    st.pyplot(fig1)
    plt.close(fig1)

# --------------------------------
# CHART 2: STUDY HOURS VS SCORE
# --------------------------------

with col2:
    st.markdown("### Study Hours vs Final Score")

    fig2, ax2 = plt.subplots(figsize=(7, 4))

    sns.scatterplot(
        data=filtered_df,
        x="Study_Hours",
        y="Final_Score",
        color="#a78bfa",
        s=65,
        ax=ax2
    )

    ax2.set_xlabel("Study Hours")
    ax2.set_ylabel("Final Score")
    ax2.set_title("Study Hours vs Academic Performance")

    style_chart(fig2, ax2)
    st.pyplot(fig2)
    plt.close(fig2)

# --------------------------------
# CHART 3: ATTENDANCE VS SCORE
# --------------------------------

col3, col4 = st.columns(2)

with col3:
    st.markdown("### Attendance vs Final Score")

    fig3, ax3 = plt.subplots(figsize=(7, 4))

    sns.regplot(
        data=filtered_df,
        x="Attendance",
        y="Final_Score",
        scatter_kws={"color": "#38bdf8", "alpha": 0.7},
        line_kws={"color": "#c084fc"},
        ax=ax3
    )

    ax3.set_xlabel("Attendance (%)")
    ax3.set_ylabel("Final Score")
    ax3.set_title("Attendance vs Academic Performance")

    style_chart(fig3, ax3)
    st.pyplot(fig3)
    plt.close(fig3)

# --------------------------------
# CHART 4: SCORE DISTRIBUTION
# --------------------------------

with col4:
    st.markdown("### Final Score Distribution")

    fig4, ax4 = plt.subplots(figsize=(7, 4))

    sns.histplot(
        data=filtered_df,
        x="Final_Score",
        bins=15,
        color="#818cf8",
        kde=True,
        ax=ax4
    )

    ax4.set_xlabel("Final Score")
    ax4.set_ylabel("Number of Students")
    ax4.set_title("Distribution of Final Scores")

    style_chart(fig4, ax4)
    st.pyplot(fig4)
    plt.close(fig4)

st.markdown("---")

# --------------------------------
# STUDENT RECORDS
# --------------------------------

st.markdown("## 👨‍🎓 Student Records")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# --------------------------------
# DOWNLOAD DATA
# --------------------------------

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Student Records",
    data=csv_data,
    file_name="campuspulse_student_records.csv",
    mime="text/csv"
)

# --------------------------------
# FOOTER
# --------------------------------

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#94a3b8;">
        <p>🎓 CampusPulse | Student Lifestyle & Academic Insights</p>
        <p>Built with Python, Pandas, Matplotlib, Seaborn and Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)
