import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import base64

def state_wise():
    df = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
    df_all = df.loc[df["Date"]==df.Date[len(df)-1]]
    df_all = df_all.loc[df.State!="India"]
    df_all = df_all[["State", "Confirmed", "Recovered", "Deceased"]].reset_index(drop=True) 
    st.write(f"**Numbers (cumulative) in the Indian States as of `{datetime.datetime.strptime(df.Date[len(df)-1], '%Y-%m-%d').strftime('%d %B %Y')}`**")
    st.dataframe(df_all.set_index("State"))
    
    csv = df_all.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download the above as a CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
    st.markdown(href, unsafe_allow_html=True)
    
    df_c = df_all[["State", "Confirmed"]].sort_values(by="Confirmed", ascending=False)
    fig = px.pie(df_c, values='Confirmed', names='State', title=f"Total Confirmed COVID19 Cases in Indian States till {datetime.datetime.strptime(df.Date[len(df)-1], '%Y-%m-%d').strftime('%d %B %Y')}")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(hovermode='x')
    st.plotly_chart(fig, use_container_width=True)

    df_c = df_all[["State", "Recovered"]].sort_values(by="Recovered", ascending=False)
    fig = px.pie(df_c, values='Recovered', names='State', title=f"Total Recovered COVID19 Cases in Indian States till {datetime.datetime.strptime(df.Date[len(df)-1], '%Y-%m-%d').strftime('%d %B %Y')}")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(hovermode='x')
    st.plotly_chart(fig, use_container_width=True)

    df_c = df_all[["State", "Deceased"]].sort_values(by="Deceased", ascending=False)
    fig = px.pie(df_c, values='Deceased', names='State', title=f"Total Loss of life due to COVID19 in Indian States till {datetime.datetime.strptime(df.Date[len(df)-1], '%Y-%m-%d').strftime('%d %B %Y')}")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(hovermode='x')
    st.plotly_chart(fig, use_container_width=True)





    # df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
    # st.write(f"**State wise data - Total Numbers till Date since outbreak**")
    # df_temp = df[df.State!="Total"][["State", "Confirmed", "Recovered", "Deaths",	"Active"]]
    # df_temp = df_temp.set_index("State")
    # st.dataframe(df_temp)
    # st.bar_chart(df_temp)