# Análise de Público-Alvo 📊

Este é um projeto desenvolvido com **Streamlit** e **Pandas** para a análise de dados demográficos e comportamentais de um público-alvo. O objetivo é fornecer uma visualização interativa dos dados através de filtros personalizados e gráficos.

## Requisitos

Antes de começar a usar o projeto, é necessário ter o seguinte instalado:

- Python 3.7 ou superior
- Pip para instalação de pacotes Python
- **Streamlit**: Biblioteca para criar aplicações interativas
- **Pandas**: Biblioteca para manipulação de dados
- (Opcional) Um arquivo CSV com os dados a serem analisados

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

No Windows:

bash
Copiar código
venv\Scripts\activate
No macOS/Linux:

bash
Copiar código
source venv/bin/activate
Instale as dependências:

Instale as bibliotecas necessárias com o comando:

bash
Copiar código
pip install -r requirements.txt
Ou, caso o arquivo requirements.txt não esteja presente, você pode instalar diretamente:

bash
Copiar código
pip install streamlit pandas
Prepare os dados
O projeto exige um arquivo CSV com dados demográficos e comportamentais para análise. O arquivo CSV deve estar na pasta data/ e ser chamado publico.csv.

Caso o arquivo não esteja presente, você pode gerar um arquivo com as colunas esperadas, como:

Idade: Idade do público
Gênero: Gênero do público (exemplo: "Masculino", "Feminino")
Localização: Localização geográfica do público
Canal: Canal de interesse ou de aquisição
Métrica: Métrica associada ao interesse no canal
Como Rodar o Projeto
Após a instalação, siga os passos abaixo para rodar o aplicativo:

Rodando o Streamlit
Execute o seguinte comando para rodar a aplicação:

bash
Copiar código
streamlit run app.py
O Streamlit irá abrir uma janela no seu navegador com a interface gráfica onde você pode interagir com os dados.

Filtro de Dados
Na interface, você pode aplicar filtros por:

Idade: Selecione um intervalo de idades.
Gênero: Filtre por gênero (Masculino, Feminino, etc.).
Localização: Selecione a(s) localização(ões) de interesse.
Esses filtros são aplicados diretamente aos dados e atualizam a visualização em tempo real.

Visualizações
O aplicativo exibe três tipos de gráficos interativos:

Distribuição de Idades: Gráfico de barras mostrando a distribuição das idades no conjunto de dados filtrado.
Distribuição por Gênero: Gráfico de barras mostrando a quantidade de indivíduos por gênero.
Interesses por Canal: Gráfico de barras mostrando o total de "Métricas" por canal.
Personalizações
Se você quiser personalizar a visualização ou os filtros, você pode modificar as seguintes partes do código:

Filtros
Você pode adicionar ou remover filtros na barra lateral. A lógica de filtros está na seção:

python
Copiar código
idade_selecionada = st.sidebar.slider("Filtrar por Idade", idade_min, idade_max, (idade_min, idade_max))
generos_selecionados = st.sidebar.multiselect("Filtrar por Gênero", generos, default=generos)
localizacoes_selecionadas = st.sidebar.multiselect("Filtrar por Localização", localizacoes, default=localizacoes)
Gráficos
Você pode modificar a forma de visualização, como tipo de gráfico ou as colunas exibidas.

Exemplo de Uso
Suponha que o arquivo CSV tenha a seguinte estrutura:

Idade	Gênero	Localização	Canal	Métrica
25	Masculino	São Paulo	Online	150
30	Feminino	Rio de Janeiro	TV	200
22	Masculino	São Paulo	Online	120
40	Feminino	Belo Horizonte	Rádio	80
Após aplicar filtros (por exemplo, idades entre 20 e 40 anos, gênero feminino e localizações "São Paulo" e "Rio de Janeiro"), o aplicativo exibirá os gráficos com base nesses dados filtrados.

Contribuições
Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou correções de bugs, fique à vontade para abrir uma issue ou enviar um pull request.
