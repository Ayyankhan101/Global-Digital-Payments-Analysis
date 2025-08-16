# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#-------------- CONFIG -----------------
st.set_page_config(page_title="Global Digital Payments Dashboard",
                   layout="wide", initial_sidebar_state="expanded")


# ----------------- LOAD DATA ---------------
@st.cache_data
def load_data():
    df = pd.read_csv("Used a mobile phone or the internet to pay bills in world.csv")
    df = df[df["OBS_STATUS"] == "A"].copy()
    df["TIME_PERIOD"] = df["TIME_PERIOD"].astype(int)
    df["OBS_VALUE"] = pd.to_numeric(df["OBS_VALUE"], errors="coerce")
    return df

df = load_data()



# ----------------- SIDEBAR -----------------
st.sidebar.header("🔎 Filters")

# Year
year = st.sidebar.selectbox("Year", sorted(df["TIME_PERIOD"].unique(), reverse=True))

# Country (multiselect)
countries = sorted(df["AREA_LABEL"].unique())
selected_countries = st.sidebar.multiselect("Countries", countries, default=["United States", "India", "Brazil"])

# Sex
sex_options = ["Total"] + [s for s in df["SEX_LABEL"].unique() if s != "Total"]
sex = st.sidebar.selectbox("Sex", sex_options)

# Age
age_options = ["15 years old and over"] + [a for a in df["AGE_LABEL"].unique() if a != "15 years old and over"]
age = st.sidebar.selectbox("Age", age_options)

# Income
income_options = ["Total"] + [i for i in df["COMP_BREAKDOWN_1_LABEL"].unique() if "Income" in str(i)]
income = st.sidebar.selectbox("Income Level", income_options)

# Education
edu_options = ["Total"] + [e for e in df["COMP_BREAKDOWN_3_LABEL"].unique() if "Education" in str(e)]
education = st.sidebar.selectbox("Education", edu_options)





# ----------------- FILTER DATA -------------
filtered = df[
    (df["TIME_PERIOD"] == year) &
    (df["AREA_LABEL"].isin(selected_countries)) &
    (df["SEX_LABEL"] == sex) &
    (df["AGE_LABEL"] == age) &
    (df["COMP_BREAKDOWN_1_LABEL"] == income) &
    (df["COMP_BREAKDOWN_3_LABEL"] == education)
].copy()

# Handle empty
if filtered.empty:
    st.error("No data for the selected combination.")
    st.stop()




# ----------------- KPI ROW -----------------
kpi1, kpi2 = st.columns(2)
with kpi1:
    st.metric("Countries Selected", len(selected_countries))
with kpi2:
    st.metric("Avg Adoption %", f"{filtered['OBS_VALUE'].mean():.1f}")




# ----------------- CHART ROW ---------------
# Bar chart – Top 10 with unique colors
top = filtered.sort_values("OBS_VALUE", ascending=False).head(10)
fig_bar = px.bar(
    top,
    x="OBS_VALUE",
    y="AREA_LABEL",
    orientation="h",
    text="OBS_VALUE",
    title=f"Top 10 – Digital Payment Adoption ({year})",
    color="AREA_LABEL",          # one color per bar
    color_discrete_sequence=px.colors.sequential.Reds_r  # optional palette
)
fig_bar.update_traces(texttemplate="%{x:.1f}%", textposition="outside")
st.plotly_chart(fig_bar, use_container_width=True)




# Choropleth map – Global heatmap
map_df = filtered[filtered["OBS_VALUE"].notnull()]
fig_map = px.choropleth(
    map_df, locations="AREA_LABEL", locationmode="country names",
    color="OBS_VALUE", hover_name="AREA_LABEL",
    color_continuous_scale="Viridis",
    title=f"Global Adoption Heatmap ({year})"
)
fig_map.update_geos(showcoastlines=True, coastlinecolor="Black")
st.plotly_chart(fig_map, use_container_width=True)





# ----------------- TREND LINE --------------
st.subheader("📈 2017 → 2021 Trend (Total Adults)")

trend = df[
    (df["AREA_LABEL"].isin(selected_countries)) &
    (df["SEX_LABEL"] == "Total") &
    (df["COMP_BREAKDOWN_1_LABEL"] == "Total") &
    (df["AGE_LABEL"] == "15 years old and over")
].pivot_table(index="TIME_PERIOD", columns="AREA_LABEL", values="OBS_VALUE")

fig_line = px.line(trend, markers=True,
                   title="Digital Payment Adoption Over Time")
fig_line.update_layout(legend_title_text="Country")
st.plotly_chart(fig_line, use_container_width=True)

# ----------------- RAW DATA ----------------
with st.expander("📋 View Raw Data"):
    st.dataframe(filtered[["AREA_LABEL", "OBS_VALUE"]].reset_index(drop=True))