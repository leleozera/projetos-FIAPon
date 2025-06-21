import streamlit as st
import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('../database/sensores.db')  # CERTO: volta uma pasta
df = pd.read_sql_query("SELECT * FROM leituras", conn)

st.title("Dashboard FarmTech Solutions")
st.write("Visualização de dados de sensores e status da irrigação")

# Mostrar tabela
st.subheader("Leituras Registradas")
st.dataframe(df)

# Gráficos
st.subheader("Gráfico de Umidade")
st.line_chart(df['umidade'])

st.subheader("Gráfico de pH")
st.line_chart(df['ph'])

# Estatísticas
st.subheader("Resumo Estatístico")
st.write(df.describe())

conn.close()
