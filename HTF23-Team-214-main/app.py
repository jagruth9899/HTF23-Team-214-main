import streamlit as st
import pandas as pd
import time
ts=time.time()
from streamlit_autorefresh import st_autorefresh

count=st_autorefresh(interval=2000,limit=100,key="fizzbuzzcounter")

df=pd.read_csv("C:/Users/gangareddy/Downloads/face-recogniton-attendance-system-main/08-10-23")
st.dataframe(df.style.highlight_max(axis=0))