# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título
st.title("🌾 Dashboard do Sistema de Irrigação - FarmTech Solutions")

# Carregar os dados (substitua pelo caminho correto do seu arquivo ou conexão com o BD)
df = pd.read_csv("dados_sensores.csv")

# Exibir dados brutos
if st.checkbox("Mostrar dados brutos"):
    st.write(df)

# Gráfico de umidade
st.subheader("💧 Nível de Umidade do Solo")
fig_umidade, ax_umidade = plt.subplots()
sns.lineplot(data=df, x="data_hora", y="umidade", ax=ax_umidade)
plt.xticks(rotation=45)
st.pyplot(fig_umidade)

# Gráfico de pH
st.subheader("🧪 Nível de pH do Solo")
fig_ph, ax_ph = plt.subplots()
sns.lineplot(data=df, x="data_hora", y="ph", ax=ax_ph, color="purple")
plt.xticks(rotation=45)
st.pyplot(fig_ph)

# Gráfico de fósforo e potássio
st.subheader("🌱 Níveis de Nutrientes (P e K)")
fig_nutrientes, ax_nutrientes = plt.subplots()
sns.lineplot(data=df, x="data_hora", y="fosforo", ax=ax_nutrientes, label="Fósforo (P)", color="green")
sns.lineplot(data=df, x="data_hora", y="potassio", ax=ax_nutrientes, label="Potássio (K)", color="orange")
plt.legend()
plt.xticks(rotation=45)
st.pyplot(fig_nutrientes)

# Estado do relé (bomba de irrigação)
st.subheader("🚿 Ativação da Irrigação")
st.line_chart(df[["data_hora", "estado_rele"]].set_index("data_hora"))
