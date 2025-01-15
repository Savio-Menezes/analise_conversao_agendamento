import pandas as pd
import streamlit as st

# Função para carregar os dados do CSV
@st.cache_data
def load_data():
    try:
        # Tenta carregar o arquivo com codificação UTF-8 e vírgula como separador
        return pd.read_csv('data/publico.csv', encoding='utf-8', sep=',')
    except UnicodeDecodeError:
        # Alternativa para arquivos com codificação Latin-1/ANSI
        return pd.read_csv('data/publico.csv', encoding='latin-1', sep=',')
    except pd.errors.ParserError:
        # Ajusta para arquivos com ponto-e-vírgula
        return pd.read_csv('data/publico.csv', encoding='utf-8', sep=';')

# Carregar os dados
data = load_data()

# Configurar o layout do Streamlit
st.title("Análise de Público-Alvo 📊")
st.subheader("Visualização de Dados Demográficos e Comportamentais")

# Filtros na barra lateral
st.sidebar.header("Filtros")
idade_min, idade_max = int(data["Idade"].min()), int(data["Idade"].max())
idade_selecionada = st.sidebar.slider("Filtrar por Idade", idade_min, idade_max, (idade_min, idade_max))

generos = data["Gênero"].unique()
generos_selecionados = st.sidebar.multiselect("Filtrar por Gênero", generos, default=generos)

localizacoes = data["Localização"].unique()
localizacoes_selecionadas = st.sidebar.multiselect("Filtrar por Localização", localizacoes, default=localizacoes)

# Aplicar filtros nos dados
dados_filtrados = data[
    (data["Idade"] >= idade_selecionada[0]) & (data["Idade"] <= idade_selecionada[1]) &
    (data["Gênero"].isin(generos_selecionados)) &
    (data["Localização"].isin(localizacoes_selecionadas))
]

# Mostrar os dados na interface
st.write("### Dados Filtrados:")
st.dataframe(dados_filtrados)

# Visualizações interativas
st.write("### Distribuição de Idades")
st.bar_chart(dados_filtrados["Idade"].value_counts())

st.write("### Distribuição por Gênero")
gender_distribution = dados_filtrados["Gênero"].value_counts()
st.bar_chart(gender_distribution)

st.write("### Interesses por Canal")
st.bar_chart(dados_filtrados.groupby("Canal")["Métrica"].sum())
