import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from all_india import *
from state_wise import *

st.sidebar.subheader("Look out here for more COVID related information")
st.sidebar.markdown("""
* Data Source - https://data.covid19india.org/
* Source Codes - https://github.com/ineelhere/IFC19/tree/master/2.0
* Feedback - https://docs.google.com/forms/d/e/1FAIpQLSeLCG7pvEx7JlSXMTtO2vpSDt6XVuUyR4VwM5rxfZgxV0Z2Vg/viewform

""")

# st.markdown("")
st.title("India Fights COVID19 (IFC19)")

st.markdown("""
webapp version 2.0 | 💻 development under progress 💻
""")

IST = pytz.timezone('Asia/Kolkata') 
datetime_ist = datetime.datetime.now(IST)
st.write(f'**⌛️ Data Fetched on : {datetime_ist.strftime("`%d %B %Y` at `%H:%M:%S` hours")} IST**')
df_daily = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
df_daily["Date"] = pd.to_datetime(df_daily.Date)
df_daily["Date"] = df_daily["Date"].dt.strftime('%d %B %Y')
df_daily = df_daily.sort_index(ascending=False)
df_india_daily = df_daily.loc[df_daily["State"]=="India"]

st.warning(f'Confirmed cases till {df_india_daily[["Date"]].reset_index(drop=True)["Date"][0]} in India: **{df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Confirmed"][0]}**')
st.success(f'Recoveries till {df_india_daily[["Date"]].reset_index(drop=True)["Date"][0]} in India: **{df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Recovered"][0]}**')
st.error(f'Loss of life till {df_india_daily[["Date"]].reset_index(drop=True)["Date"][0]} in India: **{df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Deceased"][0]}**')

all_india()
state_wise()

st.markdown("""
___
**© [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/) | 2021 **


[🌟✨ Collaborations are welcome ✨🌟](https://github.com/ineelhere/IFC19)
""")
