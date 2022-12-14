import streamlit as st
from components.youtube_downloader.ytb import ytbfunc

page_names_to_funcs = {
    "Youtube-Downloader" : ytbfunc
}

demo_name = st.sidebar.selectbox(
    "Youtube-downloader", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()