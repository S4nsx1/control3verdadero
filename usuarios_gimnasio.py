import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("users_data.csv")

st.write("""## Graficas de los usuarios que asisten al gimnasio""")
st.button("Generos(grafico)"):
  df_hombres = df[df["gender"] == "Male"]
  cantidad_hombres = len(df_hombres)

  df_mujeres = df[df["gender"] == "Female"]
  cantidad_mujeres = len(df_mujeres)

  df_nobinarios = df[df["gender"] == "Non-binary"]
  cantidad_nobinarios = len(df_nobinarios)

  fig,ax = plt.subplots()
  ax.bar(["Hombre","Mujer","No binario"], [cantidad_hombres,cantidad_mujeres,cantidad_nobinarios], color="blue")
  ax.set_xlabel("genero")
  ax.set_ylabel("Cantidad")
  ax.set_title("Generos usuarios registrados")
  st.pyplot(fig)
