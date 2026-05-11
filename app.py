
import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE CONFIGURATION

st.set_page_config(
    page_title="University Student Dashboard",
    layout="wide"
)

# TITLE

st.title("University Student Dashboard")

st.markdown(
    "Interactive dashboard for university student data analysis."
)

# FILE UPLOAD

uploaded_file = st.file_uploader(
    "Upload your CSV dataset",
    type=["csv"]
)

if uploaded_file is not None:

    # Read dataset
    df = pd.read_csv(uploaded_file)

    # DATA PREVIEW

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # METRICS

    total_applications = df["Applications"].sum()
    total_enrolled = df["Enrolled"].sum()
    avg_retention = df["Retention Rate (%)"].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Applications", f"{total_applications:,}")
    col2.metric("Total Enrolled", f"{total_enrolled:,}")
    col3.metric("Average Retention", f"{avg_retention:.2f}%")

    # APPLICATION TREND

    st.subheader("Applications Over Time")

    fig1 = px.line(
        df,
        x="Year",
        y="Applications",
        color="Term",
        markers=True
    )

    st.plotly_chart(fig1, use_container_width=True)

    # RETENTION RATE

    st.subheader("Retention Rate")

    fig2 = px.bar(
        df,
        x="Year",
        y="Retention Rate (%)",
        color="Term",
        barmode="group"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # FACULTY ENROLLMENT

    st.subheader("Faculty Enrollment")

    faculty_data = {
        "Engineering": df["Engineering Enrolled"].sum(),
        "Business": df["Business Enrolled"].sum(),
        "Arts": df["Arts Enrolled"].sum(),
        "Science": df["Science Enrolled"].sum()
    }

    faculty_df = pd.DataFrame(
        faculty_data.items(),
        columns=["Faculty", "Students"]
    )

    fig3 = px.pie(
        faculty_df,
        values="Students",
        names="Faculty"
    )

    st.plotly_chart(fig3, use_container_width=True)

else:
    st.warning("Please upload a CSV file to continue.")
