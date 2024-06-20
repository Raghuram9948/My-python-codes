import streamlit as st
import numpy as np
import pandas as pd





chart = pd.DataFrame(np.random.randn(20,3),columns=['line-1','line-2','line-3'])
st.header("1.visualization with randon ")
st.subheader('1.1 line chart')
st.line_chart(chart)

st.subheader('Area chart')
st.area_chart(chart)

st.subheader('bar chart')
st.bar_chart(chart)

st.header('2.visualization with dataframe')
st.subheader('loading dataframe')
link = 'https://raw.githubusercontent.com/AshishJangra27/Data-Analysis-with-Python-GFG/main/3.%20Data%20Preprocessing%20-%20Removing%20Null%20Value%20Rows/googleplaystore.csv'
fd = pd.read_csv(link)
st.dataframe(fd)

