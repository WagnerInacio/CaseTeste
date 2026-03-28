# Teste Entrevista ACT Power BI

## Descrição do Case

Este projeto representa um teste de entrevista para a posição de desenvolvedor em Power BI na ACT. O objetivo é demonstrar a habilidade de transformar dados brutos de uma planilha Excel (`dados_ACT.xlsx`) em um modelo de dados estruturado, seguindo as melhores práticas de modelagem dimensional para Business Intelligence (BI).

O arquivo `estrutura_dados.py` contém o código Python (utilizando a biblioteca Pandas) que processa os dados originais e os separa em tabelas dimensão e uma tabela fato, criando um esquema estrela (star schema) adequado para análises em ferramentas como Power BI.

## Estrutura dos Dados

Os dados originais da planilha `dados_ACT.xlsx` contêm informações sobre vendas, incluindo datas, locais, produtos, canais, indicadores e cenários. Esses dados foram normalizados e separados da seguinte forma:

### Tabelas Dimensão
- **Dim_Tempo.csv**: Contém informações temporais (data de referência, ano, mês, nome do mês).
- **Dim_Local.csv**: Contém informações geográficas (UF, cidade, DDD).
- **Dim_Produto.csv**: Contém detalhes dos produtos (produto, plano, tecnologia, segmento).
- **Dim_Canal.csv**: Contém os canais de venda.
- **Dim_Indicador.csv**: Contém indicadores de nível 1 e 2.
- **Dim_Cenario.csv**: Contém origem e cenário dos dados.

### Tabela Fato
- **Fato_Vendas.csv**: Contém as vendas medidas (valor), com chaves estrangeiras para as dimensões.

## Por que Separar em Tabelas Dimensão e Fato?

A separação dos dados em tabelas dimensão e fato é uma prática fundamental em data warehousing e BI, conhecida como modelagem dimensional. Aqui estão as principais razões:

### 1. **Facilita Análises e Relatórios**
   - As dimensões fornecem contexto descritivo para os fatos, permitindo filtros, agrupamentos e drill-downs intuitivos.
   - Por exemplo, é possível analisar vendas por tempo (ano/mês), local (UF/cidade), produto, etc., de forma flexível.

### 2. **Reduz Redundância de Dados**
   - Informações descritivas são armazenadas uma vez nas dimensões, evitando repetição.
   - Isso economiza espaço de armazenamento e facilita a manutenção.

### 3. **Melhora Performance de Consultas**
   - Consultas analíticas são mais rápidas, pois envolvem junções simples entre fato e dimensões.
   - Ferramentas de BI como Power BI otimizam consultas em esquemas estrela.

### 4. **Suporte a Agregações e Métricas**
   - A tabela fato contém apenas medidas numéricas (como valor de vendas), permitindo cálculos como somas, médias, etc.
   - Dimensões suportam hierarquias (ex.: tempo com ano > mês > dia).

### 5. **Manutenibilidade e Escalabilidade**
   - Mudanças em descrições (ex.: nome de um produto) afetam apenas a dimensão correspondente.
   - Fácil adição de novas dimensões ou medidas sem impactar a estrutura existente.

### 6. **Compatibilidade com Ferramentas de BI**
   - Power BI e outras ferramentas são otimizadas para modelos dimensionais.
   - Permite criação de relacionamentos automáticos e visualizações eficientes.

## Como Usar

1. **Executar o Script**: Rode `estrutura_dados.py` para gerar os arquivos CSV a partir de `dados_ACT.xlsx`.
2. **Importar no Power BI**: Carregue os arquivos CSV no Power BI e crie relacionamentos entre a tabela fato e as dimensões usando as chaves ID.
3. **Criar Visualizações**: Use as dimensões para filtros e a fato para medidas em dashboards e relatórios.

## Dependências

- Python 3.x
- Pandas: `pip install pandas`
- Arquivo `dados_ACT.xlsx` na raiz do projeto

## Estrutura do Projeto

```
/
├── dados_ACT.xlsx          # Dados originais
├── estrutura_dados.py      # Script de processamento
├── Dim_Tempo.csv           # Dimensão Tempo
├── Dim_Local.csv           # Dimensão Local
├── Dim_Produto.csv         # Dimensão Produto
├── Dim_Canal.csv           # Dimensão Canal
├── Dim_Indicador.csv       # Dimensão Indicador
├── Dim_Cenario.csv         # Dimensão Cenário
├── Fato_Vendas.csv         # Tabela Fato
└── README.md               # Este arquivo
```