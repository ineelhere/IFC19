import streamlit as st
import pandas as pd
import plotly.express as px
import base64

def last24hrs():
    slider_ph = st.empty()
    st.write(f"**Numbers all over India per day since `30 January 2020`** ")
    
    df_daily = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
    df_daily["Date"] = pd.to_datetime(df_daily.Date)
    df_daily["Date"] = df_daily["Date"].dt.strftime('%d %B %Y')
    df_daily = df_daily.sort_index(ascending=False)
    df_india_daily = df_daily.loc[df_daily["State"]=="India"]
    df_india_daily = (df_india_daily[["Date", "Confirmed", "Recovered", "Deceased"]]).reset_index(drop=True)
    df_india_24hrs = df_india_daily.sort_index(ascending=False)
    df_india_24hrs = df_india_24hrs.set_index("Date").diff()
    df_india_24hrs = df_india_24hrs.iloc[::-1]
    total = len(df_india_24hrs)
    value = slider_ph.slider("Move the slider to list data for the last 'n' number of days", 1, total, 7, 1)


    st.dataframe(df_india_24hrs.head(value))
    csv = df_india_24hrs.iloc[::-1].reset_index().to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download the above as a CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
    st.markdown(href, unsafe_allow_html=True)

    df_long=pd.melt(df_india_24hrs.iloc[::-1].reset_index(), id_vars=['Date'], value_vars=["Confirmed", "Recovered", "Deceased"])
    fig = px.line(df_long, x='Date', y='value', color='variable')
    fig.update_layout(hovermode='x')
    st.plotly_chart(fig, use_container_width=True)

    
    st.write(f'**Numbers in the Indian states on `{df_daily.head(1).reset_index()["Date"][0]}`**')

    df_daily = df_daily.loc[df_daily.State!="India"]
    last_day = df_daily.Date.unique()[1]
    df_lastday = df_daily.loc[df_daily.Date == last_day].reset_index(drop=True)
    df_lastday = df_lastday.reset_index(drop=True)
    df_today = df_daily.loc[df_daily.Date == df_daily.head(1).reset_index()["Date"][0]].reset_index(drop=True)
    df_today = df_today.reset_index(drop=True)
    a = df_today[["Confirmed", "Recovered", "Deceased"]]
    b= df_lastday[["Confirmed", "Recovered", "Deceased"]]
    pd.to_numeric(a.all())
    pd.to_numeric(b.all())
    df_24 = a.subtract(b)
    df_24["State"] = df_lastday["State"]
    
    st.dataframe(df_24[["State", "Confirmed", "Recovered", "Deceased"]].set_index(["State"]))
    csv = df_24.reset_index(drop=True).to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download the above as a CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
    st.markdown(href, unsafe_allow_html=True)

    df_c = df_24[["State", "Confirmed"]].sort_values(by="Confirmed", ascending=False)
    fig = px.pie(df_c, values='Confirmed', names='State', title=f'Confirmed COVID19 Cases in Indian States on {df_today.head(1).reset_index()["Date"][0]}')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(hovermode='x')
    st.plotly_chart(fig, use_container_width=True)

    df_c = df_24[["State", "Recovered"]].sort_values(by="Recovered", ascending=False)
    fig = px.pie(df_c, values='Recovered', names='State', title=f'Recovered COVID19 Cases in Indian States on {df_today.head(1).reset_index()["Date"][0]}')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(hovermode='x')
    st.plotly_chart(fig, use_container_width=True)

    df_c = df_24[["State", "Deceased"]].sort_values(by="Deceased", ascending=False)
    fig = px.pie(df_c, values='Deceased', names='State', title=f'Loss of life due to COVID19 in Indian States on {df_today.head(1).reset_index()["Date"][0]}')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(hovermode='x')
    st.plotly_chart(fig, use_container_width=True)