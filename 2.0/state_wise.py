import streamlit as st
import pandas as pd
import datetime

def state_wise():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
    df_all = df.loc[df["Date"]==df.Date[len(df)-1]]
    df_all = df_all.loc[df.State!="India"]
    df_all = df_all[["State", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True) 
    st.write(f"**Numbers in the Indian States as of `{datetime.datetime.strptime(df.Date[len(df)-1], '%Y-%m-%d').strftime('%d %B %Y')}`**")
    st.dataframe(df_all.set_index("State"))
    st.line_chart(df_all.set_index("State"))
