import pandas as pd
import streamlit as st
import os

# Configuração inicial do Streamlit
st.set_page_config(
    page_title="Relatório de Agendamentos 📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Função para carregar os dados
@st.cache_data
def load_data():
    file_path = os.path.join(os.getcwd(), "data", "relatorio_agendamento.csv")
    if not os.path.exists(file_path):
        st.error(f"O arquivo '{file_path}' não foi encontrado.")
        return pd.DataFrame()
    return pd.read_csv(file_path, encoding='utf-8', sep=',')

# Carregar os dados
data = load_data()

# Limpar espaços extras nos nomes das colunas
data.columns = data.columns.str.strip()

# Verifica se os dados foram carregados corretamente
if data.empty:
    st.warning("Nenhum dado foi carregado. Verifique o arquivo e tente novamente.")
else:
    # Título e layout principal
    st.title("📊 Relatório de Agendamentos")
    st.markdown("---")

    # Configuração de filtros na barra lateral
    st.sidebar.header("Filtros")
    tipos_servicos = data["Tipo de Servio"].unique()
    servico_selecionado = st.sidebar.multiselect(
        "Filtrar por Tipo de Serviço",
        options=tipos_servicos,
        default=tipos_servicos,
    )

    colaboradores = data["Colaborador"].unique()
    colaborador_selecionado = st.sidebar.multiselect(
        "Filtrar por Colaborador",
        options=colaboradores,
        default=colaboradores,
    )

    # Filtra os dados com base nas seleções
    dados_filtrados = data[
        (data["Tipo de Servio"].isin(servico_selecionado)) &
        (data["Colaborador"].isin(colaborador_selecionado))
    ]

    # Divisão em métricas principais
    st.header("Visão Geral")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📋 Total de Serviços", len(dados_filtrados))
    with col2:
        valor_total = dados_filtrados["Valor da OS"].sum()
        st.metric("💰 Valor Total", f"R$ {valor_total:,.2f}")
    with col3:
        passantes = dados_filtrados["Passante"].value_counts().get("Sim", 0)
        st.metric("👥 Clientes Passantes", passantes)
    with col4:
        agendados = dados_filtrados["Agendado"].value_counts().get("Sim", 0)
        st.metric("📅 Clientes Agendados", agendados)

    st.markdown("---")

    # Gráficos em abas com espaçamento e diferentes visualizações
    st.header("Análises Visuais")
    tab1, tab2, tab3 = st.tabs(["📈 Distribuições", "📊 Gráficos Financeiros", "📋 Detalhes por Colaborador"])

    # Aba 1: Gráficos de distribuição
    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Distribuição por Tipo de Serviço")
            servico_chart = dados_filtrados["Tipo de Servio"].value_counts().reset_index()
            servico_chart.columns = ["Tipo de Serviço", "Quantidade"]
            st.bar_chart(servico_chart.set_index("Tipo de Serviço"), use_container_width=True)

        with col2:
            st.subheader("Histograma de Valores de OS")
            valor_histograma = dados_filtrados["Valor da OS"].value_counts().sort_index()
            st.bar_chart(valor_histograma, use_container_width=True)

    # Aba 2: Gráficos financeiros
    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Valor Total por Colaborador")
            colaborador_chart = dados_filtrados.groupby("Colaborador")["Valor da OS"].sum().reset_index()
            colaborador_chart.columns = ["Colaborador", "Valor Total"]
            st.line_chart(colaborador_chart.set_index("Colaborador"), use_container_width=True)

        with col2:
            st.subheader("Valor Total por Tipo de Serviço")
            valor_servico = dados_filtrados.groupby("Tipo de Servio")["Valor da OS"].sum().reset_index()
            valor_servico.columns = ["Tipo de Serviço", "Valor Total"]
            st.bar_chart(valor_servico.set_index("Tipo de Serviço"), use_container_width=True)

    # Aba 3: Detalhes por colaborador
    with tab3:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Agendamentos por Colaborador")
            colaborador_count = dados_filtrados["Colaborador"].value_counts().reset_index()
            colaborador_count.columns = ["Colaborador", "Contagem"]
            st.area_chart(colaborador_count.set_index("Colaborador"), use_container_width=True)

        with col2:
            st.subheader("Comparativo de Lucro: Agendados x Passantes")
            lucro_por_tipo = dados_filtrados.groupby("Passante")["Valor da OS"].sum().reset_index()
            lucro_por_tipo.columns = ["Tipo de Cliente", "Lucro Total"]
            lucro_por_tipo["Tipo de Cliente"] = lucro_por_tipo["Tipo de Cliente"].replace(
                {"Sim": "Agendados", "Não": "Passantes"}
            )
            st.bar_chart(lucro_por_tipo.set_index("Tipo de Cliente"), use_container_width=True)
