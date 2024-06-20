import streamlit as st
import pandas as pd


st.header("Uploading csv file")
file = st.file_uploader("upload your file",type= 'csv')

if file is not None:
    fd = pd.read_csv(file)
    st.table(fd.head())

st.header("uploading video")
aud = st.file_uploader("Select Audio",)
st.video(aud)
st.header("upload image")
img = st.file_uploader("upload img")
if img is not None:
    st.image(img)

st.title("Uploading Audio")
Ad = st.file_uploader("upload audio")

st.audio(Ad)







