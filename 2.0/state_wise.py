import streamlit as st
import pandas as pd
import numpy as np

def state_wise():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
    st.write(f"**State wise data - Total Numbers till Date since outbreak**")
    df_temp = df[df.State!="Total"][["State", "Confirmed", "Recovered", "Deaths",	"Active"]]
    df_temp = df_temp.set_index("State")
    st.dataframe(df_temp)
    st.bar_chart(df_temp)
