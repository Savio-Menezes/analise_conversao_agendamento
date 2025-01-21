# Relatório de Agendamentos 📊

Este é um aplicativo interativo desenvolvido com Streamlit para visualizar e analisar relatórios de agendamentos. Ele oferece diversas funcionalidades, como aplicação de filtros, exibição de métricas, gráficos analíticos e comparações de lucro entre diferentes tipos de clientes.

## Funcionalidades
- **Filtros personalizáveis**: Filtrar por tipo de serviço ou colaborador.
- **Métricas gerais**: Exibição de totais, valores e distribuição de serviços.
- **Análises gráficas**:
  - Distribuição por tipo de serviço.
  - Valor total por colaborador e por tipo de serviço.
  - Histograma de valores.
  - Média e desvio padrão dos valores.
  - Contagem de registros por colaborador.
- **Gráfico comparativo**: Lucro entre clientes agendados e passantes.

## Requisitos de Sistema
- Python 3.8 ou superior.
- Bibliotecas listadas abaixo.

## Instalação
1. Clone este repositório:
   ```bash
   git clone (url do projeto)
   cd seu-repositorio
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

3. Instale as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   ```

### Dependências
As seguintes bibliotecas são utilizadas:
- **pandas**: Para manipulação e análise de dados.
  ```bash
  pip install pandas
  ```
- **streamlit**: Para criar a interface interativa.
  ```bash
  pip install streamlit
  ```

## Como Executar
1. Certifique-se de que o arquivo CSV (relatorio_agendamento.csv) esteja no caminho especificado:
   ```
   C:\Users\savio.CVP\Documents\publico_alvo\data\relatorio_agendamento.csv
   ```

2. Execute o aplicativo Streamlit:
   ```bash
   streamlit run app.py
   ```

3. O aplicativo será iniciado e estará disponível no seu navegador padrão.

## Estrutura do Projeto
```
/
|-- app.py                  # Código principal do aplicativo
|-- requirements.txt        # Lista de dependências do projeto
|-- data/
    |-- relatorio_agendamento.csv  # Arquivo de dados (coloque aqui)
```

## Possíveis Erros e Soluções
- **Erro: "O arquivo não foi encontrado"**
  - Certifique-se de que o arquivo CSV está no local correto e nomeado como "relatorio_agendamento.csv".

- **Erro: "Erro ao exibir gráficos"**
  - Verifique se os dados no arquivo estão corretamente formatados e se as colunas esperadas estão presentes.

- **Erro: "DataFrame vazio"**
  - O arquivo pode estar vazio ou com problemas de codificação. Certifique-se de que o CSV contém dados válidos.

## Contribuição
Sinta-se à vontade para abrir problemas (*issues*) ou enviar solicitações de pull (*pull requests*) para melhorias.


