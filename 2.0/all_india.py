import streamlit as st
import pandas as pd
import base64


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
    csv = (df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].head(value)).to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download the above as a CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
    st.markdown(href, unsafe_allow_html=True)
