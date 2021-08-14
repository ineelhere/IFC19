import streamlit as st
import pandas as pd

st.sidebar.subheader("Look out here for more COVID relates information")
# st.markdown("![](https://komarev.com/ghpvc/?username=ineelhere&label=VISITOR+COUNTS)")
st.title("India Fights COVID19 (IFC19)")
st.markdown("""
webapp version 2.0 | development under progress
![](https://miro.medium.com/max/1400/1*CsJ05WEGfunYMLGfsT2sXA.gif)
""")
df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
st.write(f"State wise data")
st.write(df)

st.markdown("""
___
**© [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/) | 2021**
""")
