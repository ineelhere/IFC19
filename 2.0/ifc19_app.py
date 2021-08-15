import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from state_wise import *

st.sidebar.subheader("Look out here for more COVID related information")
# st.markdown("![](https://komarev.com/ghpvc/?username=ineelhere&label=VISITOR+COUNTS)")
st.title("India Fights COVID19 (IFC19)")

st.markdown("""
webapp version 2.0 | 💻 development under progress 💻
""")

df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
IST = pytz.timezone('Asia/Kolkata') 
datetime_ist = datetime.now(IST)
st.write(f'**🔄 Data is up-to-date as of: `{df.loc[df.State=="Total"]["Last_Updated_Time"][0]}` IST  \n⌛️ Current time: `{datetime_ist.strftime("%d/%m/%Y %H:%M:%S %Z")}` IST**')

state_wise()

st.markdown("""
___
**© [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/) | 2021 **


[🌟✨ Collaborations are welcome ✨🌟](https://github.com/ineelhere/IFC19)
""")
