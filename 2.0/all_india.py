import streamlit as st
import pandas as pd
import numpy as np


def all_india():
    df_daily = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
    df_daily["Date"] = pd.to_datetime(df_daily.Date)
    df_daily["Date"] = df_daily["Date"].dt.strftime('%d %B %Y')
    df_daily = df_daily.sort_index(ascending=False)
    df_india_daily = df_daily.loc[df_daily["State"]=="India"]
    total = len(df_india_daily)
    slider_ph = st.empty()
    st.write(f"**Numbers all over India since `30 January 2020`** ")
    value = slider_ph.slider("Move the slider to list data for the last 'n' number of days", 1, total, 7, 1)
    st.dataframe((df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].head(value)).set_index(["Date"]))
    
