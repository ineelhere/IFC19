import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from all_india import *
from state_wise import *
from info import *
from last24hrs import *
from vaccination import *

st.sidebar.subheader("About the webapp")
st.sidebar.success("** RECOGNITION:  \n\nThis webapp has been included in one of the Weekly Roundups on Streamlit community forum under the Geography and Society section: [https://discuss.streamlit.io/t/weekly-roundup-streamlit-books-seogres-metrics-dashboards-and-more/16468](https://discuss.streamlit.io/t/weekly-roundup-streamlit-books-seogres-metrics-dashboards-and-more/16468)**")
st.sidebar.markdown("""
* [API Source](https://data.covid19india.org/)
* [Source Codes](https://github.com/ineelhere/IFC19/tree/master/2.0)
* [Feedback](https://docs.google.com/forms/d/e/1FAIpQLSeLCG7pvEx7JlSXMTtO2vpSDt6XVuUyR4VwM5rxfZgxV0Z2Vg/viewform)
### 👋👋 IFC19 webapp version 2.0 is here! | August 2021 
ICF19 no longer uses the Django framework. It now runs on Streamlit - an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.
- [The old website](https://indraneel.pythonanywhere.com/) is now deprecated and redirects users to visit this new version.
- The Streamlit hosted app is available [here](https://share.streamlit.io/ineelhere/ifc19/2.0/ifc19_app.py)

#### New features in this release
* More visualizations - interactive and downloadable
* Download all the data in csv format as desired
* COVID19 Vaccination data for India is added
* Truly open-source and reproducible, no secrets! [Click here](https://github.com/ineelhere/IFC19/tree/master/2.0)

___
### 👉👉 IFC19 webapp version 1.0 | May 2020 
*`currently deprecated`*  \n
With a background in Biotechnology and Bioinformatics, I wanted to expand my knowledge and skillsets in data science programming and web development. While I was self-learning my way out, I was inspired by the several COVID19 dashboards that were coming up from several sources worldwide. So, I thought of creating a similar website myself as a part of the learning process and here is the result!
The data is being pulled from the crowdsourced API provided by the covid19india.org. The relevant data is then cleaned up and processed using python. The results are then presented on the website using Django framework.
So, long story short — I have created a website that displays real-time data and statistics along with other information regarding the COVID19 situation in India. Please visit the website and [provide your feedback](https://docs.google.com/forms/d/e/1FAIpQLSeLCG7pvEx7JlSXMTtO2vpSDt6XVuUyR4VwM5rxfZgxV0Z2Vg/viewform) on the same.

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
st.sidebar.markdown(html_text, unsafe_allow_html=True)

st.sidebar.info("**This project is fully a personal endeavor. It has not been done under any sort of external influence or funding or sponsorship.**")

st.markdown("""# IFC19 - India ![](https://img.icons8.com/fluency/50/000000/india-map.png) Fights COVID19 """)

st.markdown("""
*webapp version 2.0* | *best viewed on `desktop mode` if accessed from mobile devices*
""")

IST = pytz.timezone('Asia/Kolkata') 
datetime_ist = datetime.datetime.now(IST)
st.write(f'**⌛️ Data Fetched from source on : {datetime_ist.strftime("`%d %B %Y` at `%H:%M:%S` hours")} IST**')
df_daily = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
df_daily["Date"] = pd.to_datetime(df_daily.Date)
df_daily["Date"] = df_daily["Date"].dt.strftime('%d %B %Y')
df_daily = df_daily.sort_index(ascending=False)
df_india_daily = df_daily.loc[df_daily["State"]=="India"]

df_india_24hrs = (df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]]).reset_index(drop=True).sort_index(ascending=False)
df_india_24hrs = df_india_24hrs.set_index("Date").diff()
df_india_24hrs = df_india_24hrs.iloc[::-1]

st.warning(f'**Confirmed** cases till {df_india_daily[["Date"]].reset_index(drop=True)["Date"][0]} in India: **{df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Confirmed"][0]}**  \n**Confirmed** cases in the past 24 hours in India: **{int(df_india_24hrs.reset_index().head(1)["Confirmed"][0])}**')
st.info(f'Currently **Active** cases in India: **{df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Confirmed"][0]-df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Recovered"][0]-df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Deceased"][0]-df_india_daily.head(1).reset_index()["Other"][0]}**')
st.success(f'**Recoveries** till {df_india_daily[["Date"]].reset_index(drop=True)["Date"][0]} in India: **{df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Recovered"][0]}**  \n**Recoveries** in the past 24 hours in India: **{int(df_india_24hrs.reset_index().head(1)["Recovered"][0])}**')
st.error(f'**Loss** of life till {df_india_daily[["Date"]].reset_index(drop=True)["Date"][0]} in India: **{df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True)["Deceased"][0]}**  \n**Loss** of life in the past 24 hours in India: **{int(df_india_24hrs.reset_index().head(1)["Deceased"][0])}**')

st.subheader("**Please make a selection below**")
mode = st.radio("", ["Show cumulative stats till date since outbreak", "Show stats for cases per day", "Show stats on COVID19 vaccination in India"])
if mode == "Show cumulative stats till date since outbreak":
    all_india()
    state_wise()
if mode ==  "Show stats for cases per day" :
    last24hrs()
if mode == "Show stats on COVID19 vaccination in India":
    vaccination()

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
st.write("*[Collaborations](https://github.com/ineelhere/IFC19/tree/master/2.0) are welcome *")
st.write("**[Please click here  to share your thoughts on this webapp!](https://docs.google.com/forms/d/e/1FAIpQLSeLCG7pvEx7JlSXMTtO2vpSDt6XVuUyR4VwM5rxfZgxV0Z2Vg/viewform)**")
response = st.checkbox("List the Data Sources (Websites)")
if response:
    resources()
st.info("** Take care and stay safe.**")
