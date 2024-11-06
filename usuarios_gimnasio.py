import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("users_data.csv")

st.write(""" 
#          Gimnasio Akira
## Graficas de los usuarios que asisten al gimnasio""")
if st.button("Generos(grafico)"):
  df_hombres = df[df["gender"] == "Male"]
  cantidad_hombres = len(df_hombres)

  df_mujeres = df[df["gender"] == "Female"]
  cantidad_mujeres = len(df_mujeres)

  df_nobinarios = df[df["gender"] == "Non-binary"]
  cantidad_nobinarios = len(df_nobinarios)

  fig,ax = plt.subplots(figsize=(10,3))
  ax.bar(["Hombre","Mujer","No binario"], [cantidad_hombres,cantidad_mujeres,cantidad_nobinarios], color="blue")
  ax.set_xlabel("genero")
  ax.set_ylabel("Cantidad")
  ax.set_title("Generos usuarios registrados")
  st.pyplot(fig)

if st.button("Localidad(grafico)"):
  df_denver = df[df["user_location"] == "Denver"]
  cantidad_denver = len(df_denver)
  df_Orlando = df[df["user_location"] == "Orlando"]
  cantidad_Orlando = len(df_Orlando)
  df_Austin = df[df["user_location"] == "Austin"]
  cantidad_Austin = len(df_Austin)
  df_Seattle = df[df["user_location"] == "Seattle"]
  cantidad_Seattle = len(df_Seattle)
  df_Atlanta = df[df["user_location"] == "Atlanta"]
  cantidad_Atlanta = len(df_Atlanta)
  df_Detroit = df[df["user_location"] == "Detroit"]
  cantidad_Detroit = len(df_Detroit)
  df_Miami = df[df["user_location"] == "Miami"]
  cantidad_Miami = len(df_Miami)
  df_San_Francisco = df[df["user_location"] == "San Francisco"]
  cantidad_San_Francisco = len(df_San_Francisco)
  df_Boston = df[df["user_location"] == "Boston"]
  cantidad_Boston = len(df_Boston)
  df_Las_Vegas = df[df["user_location"] == "Las Vegas"]
  cantidad_Las_Vegas = len(df_Las_Vegas)

  fig,ax = plt.subplots(figsize=(10,3))
  ax.bar(["Denver","Orlando","Austin","Seattle","Atlanta","Detroit","Miami","San Francisco","Boston","Las Vegas"], [cantidad_denver, cantidad_Orlando, cantidad_Austin,cantidad_Seattle,cantidad_Atlanta, cantidad_Detroit, cantidad_Miami,cantidad_San_Francisco,cantidad_Boston,cantidad_Las_Vegas ], color="red")
  ax.set_xlabel("Localidad")
  ax.set_ylabel("Lugareños")
  ax.set_title("Localidad usuarios registrados")
  st.pyplot(fig)

if st.button("Calidad Suscripciones(grafico)"):
  df_Basic = df[df["subscription_plan"] == "Basic"]
  cantidad_Basic = len(df_Basic)
  df_Pro = df[df["subscription_plan"] == "Pro"]
  cantidad_Pro = len(df_Pro)
  df_Student = df[df["subscription_plan"] == "Student"]
  cantidad_Student = len(df_Student)
  
  fig,ax = plt.subplots(figsize=(10,3))
  ax.bar(["Basic","Pro","Student"],[cantidad_Basic,cantidad_Pro, cantidad_Student], color="lilac")
  ax.set_xlabel("Suscripciones")
  ax.set_ylabel("Usuarios")
  ax.set_title("Suscripciones usuarios registrados")
  st.pyplot(fig)
  
  
