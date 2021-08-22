import streamlit as st
import pandas as pd
import plotly.express as px

def vaccination():
    df_vac = pd.read_csv("http://api.covid19india.org/csv/latest/cowin_vaccine_data_statewise.csv")
    df_vac = df_vac.loc[df_vac.State == "India"]
    df_vac = df_vac.dropna(subset=["Total Doses Administered"])
    df_vac = df_vac.iloc[::-1].reset_index(drop=True)
    df_vac["Updated On"] = pd.to_datetime(df_vac["Updated On"]).dt.strftime('%d %B %Y')
    df_vac = df_vac.drop(columns=['State', 'AEFI', '18-44 Years (Doses Administered)', '45-60 Years (Doses Administered)', '60+ Years (Doses Administered)','18-44 Years (Individuals Vaccinated)','45-60 Years (Individuals Vaccinated)','60+ Years (Individuals Vaccinated)', 'Male (Individuals Vaccinated)','Female (Individuals Vaccinated)','Transgender (Individuals Vaccinated)'])    
    
    slider_ph = st.empty()
    st.write(f"**Latest data available on COVID19 vaccination in India** ")
    value = slider_ph.slider("Move the slider to list data for the last 'n' number of days", 1, len(df_vac), 7, 1)
    st.dataframe(df_vac.head(value).set_index(["Updated On"]))

    df_long=pd.melt(df_vac.iloc[::-1].reset_index(), id_vars=['Updated On'], value_vars=['Total Doses Administered', 'Sessions', 'First Dose Administered', 'Second Dose Administered'])
    fig = px.line(df_long, x='Updated On', y='value', color='variable')
    fig.update_layout(hovermode='x')
    st.plotly_chart(fig, use_container_width=True)

    df_long=pd.melt(df_vac.iloc[::-1].reset_index(), id_vars=['Updated On'], value_vars=['Covaxin (Doses Administered)', 'CoviShield (Doses Administered)', 'Sputnik V (Doses Administered)'])
    fig = px.line(df_long, x='Updated On', y='value', color='variable')
    fig.update_layout(hovermode='x')
    st.plotly_chart(fig, use_container_width=True)
