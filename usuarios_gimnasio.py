import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("users_data.csv")

st.write("""Graficas de los usuarios que asisten al gimnasio""")
