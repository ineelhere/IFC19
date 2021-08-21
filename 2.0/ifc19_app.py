import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from all_india import *
from state_wise import *
from info import *

st.sidebar.subheader("Look out here for more COVID related information")
st.sidebar.markdown("""
* Data Source - https://data.covid19india.org/
* Source Codes - https://github.com/ineelhere/IFC19/tree/master/2.0
* Feedback - https://docs.google.com/forms/d/e/1FAIpQLSeLCG7pvEx7JlSXMTtO2vpSDt6XVuUyR4VwM5rxfZgxV0Z2Vg/viewform

""")
response = st.sidebar.button("Resources")
if response:
    resources()


# st.markdown("")
st.title("India Fights COVID19 (IFC19)")

st.markdown("""
*webapp version 2.0* | *best viewed on `desktop mode` if accessed from mobile devices*
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

mode = st.radio("", ["Show cumulative stats till date since outbreak", "Show stats for last 24 hours as per the data available"])
if mode == "Show cumulative stats till date since outbreak":
    all_india()
    state_wise()
else:
    st.write("**Coming soon!**")

st.markdown("""
___
**© [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/) | 2021 **
""")

html_text = """
<a href="https://www.linkedin.com/in/indraneelchakraborty/" target="_blank"><img src="https://static-exp1.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" alt="Linkedin" width="22" height="22"> </a>
                <a href="https://sites.google.com/view/indraneelchakraborty" target="_blank"><img width="22" height="22" src="https://lh3.googleusercontent.com/mjVS_Izc6fGAvuaT0v--gb2so5mZvAbI5EUMUB41cWB7tpy81trBCR8rIlj8NoKgPzDWGN-Hs97NlW0T9W57YJ5z9A8QQWwXUYa_Zg=h120" alt="Google Sites"> </a>
                <a href="https://twitter.com/ineelhere" target="_blank"> <img src="https://abs.twimg.com/favicons/twitter.ico" alt="Twitter" width="22" height="22"> </a>
                <a href="https://www.youtube.com/channel/UCbIMzl7rOj0FkamVf_aBM8w" target="_blank"> <img src="https://www.youtube.com/s/desktop/28b67e7f/img/favicon_48.png" alt="YouTube" width="22" height="22"> </a>
                <a href="https://github.com/ineelhere" target="_blank"><img width="22" height="22" src="https://github.com/fluidicon.png" alt="Github"> </a>

"""
st.markdown(html_text, unsafe_allow_html=True)
st.write("[🌟✨ Collaborations are welcome ✨🌟](https://github.com/ineelhere/IFC19)")
st.info("** 👨‍💻 App development under progress. New features coming soon!**")

