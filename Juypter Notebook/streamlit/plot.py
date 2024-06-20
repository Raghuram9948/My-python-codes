
import numpy as np
import pandas as pd
import altair as at
import streamlit as st
import matplotlib as plt


st.title("AAAA")
fd = st.file_uploader("choose your audio")
st.audio(fd)
