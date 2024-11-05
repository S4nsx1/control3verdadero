import streamlit as st
import pandas as pd 


df = pd.read_csv("users_data.csv")

st.write("Graficas de los usuarios que asisten al gimnasio")
