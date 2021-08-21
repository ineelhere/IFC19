import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from all_india import *
from state_wise import *
from info import *
from last24hrs import *

st.sidebar.subheader("Look out here for more COVID related information")
st.sidebar.markdown("""
* [API Source](https://data.covid19india.org/)
* [Source Codes](https://github.com/ineelhere/IFC19/tree/master/2.0)
* [Feedback](https://docs.google.com/forms/d/e/1FAIpQLSeLCG7pvEx7JlSXMTtO2vpSDt6XVuUyR4VwM5rxfZgxV0Z2Vg/viewform)

""")

# st.markdown("")
st.markdown("""# India ![](https://img.icons8.com/fluency/50/000000/india-map.png) Fights COVID19 (IFC19)""")

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

df_india_24hrs = (df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]]).reset_index(drop=True).sort_index(ascending=False)
df_india_24hrs = df_india_24hrs.set_index("Date").diff()
df_india_24hrs = df_india_24hrs.iloc[::-1]

st.warning(f'**Confirmed** cases till {df_india_daily[["Date"]].reset_index(drop=True)["Date"][0]} in India: **{df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Confirmed"][0]}**  \n**Confirmed** cases in the past 24 hours in India: **{df_india_24hrs.reset_index().head(1)["Confirmed"][0]}**')
st.info(f'Currently **Active** cases **{df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Confirmed"][0]-df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Recovered"][0]-df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Deceased"][0]-df_india_daily.head(1).reset_index()["Other"][0]}**')
st.success(f'**Recoveries** till {df_india_daily[["Date"]].reset_index(drop=True)["Date"][0]} in India: **{df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Recovered"][0]}**  \n**Recoveries** in the past 24 hours in India: **{df_india_24hrs.reset_index().head(1)["Recovered"][0]}**')
st.error(f'**Loss** of life till {df_india_daily[["Date"]].reset_index(drop=True)["Date"][0]} in India: **{df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Deceased"][0]}**  \n**Loss** of life in the past 24 hours in India: **{df_india_24hrs.reset_index().head(1)["Deceased"][0]}**')

mode = st.radio("", ["Show cumulative stats till date since outbreak", "Show stats for cases per day"])
if mode == "Show cumulative stats till date since outbreak":
    all_india()
    state_wise()
else:
    last24hrs()

response = st.button("List the Data Sources (Websites)")
if response:
    resources()

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
st.write("**[Let me know your thoughts on this webapp!](https://docs.google.com/forms/d/e/1FAIpQLSeLCG7pvEx7JlSXMTtO2vpSDt6XVuUyR4VwM5rxfZgxV0Z2Vg/viewform)**")
st.info("** 👨‍💻 App development under progress. New features coming soon!**")

