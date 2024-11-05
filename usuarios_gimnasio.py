import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv("users_data.csv")

st.write("""## Graficas de los usuarios que asisten al gimnasio""")

df_hombres = df[df["gender"] == "male"]
cantidad_hombres = len(df_hombres)

df_mujeres = df[df["gender"] == "female"]
cantidad_mujeres = len(df_mujeres)

df_nobinarios = df[df["gender"] == "Non-binary"]
cantidad_nobinarios = len(df_nobinarios)

fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].bar(["Hombre","Mujer","No binario"], [cantidad_hombres,cantidad_mujeres,cantidad_nobinarios], color=blue)
ax[0].set_xlabel("genero")
ax[0].set_ylabel("Cantidad")
ax[0].set_tittle("Generos usuarios registrados")

st.pyplot(fig)
