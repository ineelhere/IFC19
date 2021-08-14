import streamlit as st
import pandas as pd
st.markdown("![](https://komarev.com/ghpvc/?username=ineelhere&color=blue)")
st.title("India Fights COVID19 (IFC19)")
st.markdown("""
webapp version 2.0 | development under progress

![](https://miro.medium.com/max/1400/1*CsJ05WEGfunYMLGfsT2sXA.gif)
""")
df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
st.write(f"State wise data")
st.write(df)

st.markdown("""
<hr>

**© Indraneel Chakraborty | 2021**
""")
