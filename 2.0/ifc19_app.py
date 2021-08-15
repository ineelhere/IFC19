import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

st.sidebar.subheader("Look out here for more COVID related information")
# st.markdown("![](https://komarev.com/ghpvc/?username=ineelhere&label=VISITOR+COUNTS)")
st.title("India Fights COVID19 (IFC19)")
st.markdown("""
webapp version 2.0 | **Currently under development**
![](https://miro.medium.com/max/1400/1*CsJ05WEGfunYMLGfsT2sXA.gif)
""")
df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")


IST = pytz.timezone('Asia/Kolkata') 
datetime_ist = datetime.now(IST)
st.write(f'**🔄 Data was last updated on: `{df.loc[df.State=="Total"]["Last_Updated_Time"][0]}` IST  \n🕖 Current time: `{datetime_ist.strftime("%d/%m/%Y %H:%M:%S %Z")}` IST**')

st.write(f"State wise data")
st.write(df)
st.markdown("""
___
**© [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/) | 2021**
""")
