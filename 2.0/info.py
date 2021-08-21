import streamlit as st

def resources():
    html_text = """
    <a class="twitter-timeline" href="https://twitter.com/CovidIndiaSeva?ref_src=twsrc%5Etfw">Tweets by CovidIndiaSeva</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    """
    st.markdown(html_text, unsafe_allow_html=True)
