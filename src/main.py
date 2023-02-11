import streamlit as st

st.set_page_config(page_title="YouTube Downloader")
st.title("Youtube Downloader")
st.write("Paste YouTube URL in the text box below")
st.write("Select MP3 or MP4 output format")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    URL = st.text_input("YouTube URL", placeholder="Paste YouTube URL here")

with col2:
    file_format = st.radio("File Type:", ("MP3", "MP4"))


