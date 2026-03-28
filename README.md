# Teste Power BI

## Descrição do Case

Este projeto representa um teste de entrevista para a posição de Consultor em Power BI na ACT. O objetivo é demonstrar a habilidade de transformar dados brutos de uma planilha Excel (`dados_ACT.xlsx`) em um modelo de dados estruturado, seguindo as melhores práticas de modelagem dimensional para Business Intelligence (BI).

O arquivo `src/estrutura_dados.py` contém o código Python (utilizando a biblioteca Pandas) que processa os dados originais e os separa em tabelas dimensão e uma tabela fato, criando um esquema estrela (star schema) adequado para análises em ferramentas como Power BI.

O projeto inclui também um dashboard interativo desenvolvido no Power BI (`Case_ACT.pbix`), baseado nos dados processados, e uma apresentação explicativa (`Case para vaga de Consultor Power BI-v03.pptx`).

## Estrutura dos Dados

Os dados originais da planilha `data/dados_ACT.xlsx` contêm informações sobre vendas, incluindo datas, locais, produtos, canais, indicadores e cenários. Esses dados foram normalizados e separados da seguinte forma:

### Tabelas Dimensão (em `dimensions/`)
- **Dim_Tempo.csv**: Contém informações temporais (data de referência, ano, mês, nome do mês).
- **Dim_Local.csv**: Contém informações geográficas (UF, cidade, DDD).
- **Dim_Produto.csv**: Contém detalhes dos produtos (produto, plano, tecnologia, segmento).
- **Dim_Canal.csv**: Contém os canais de venda.
- **Dim_Indicador.csv**: Contém indicadores de nível 1 e 2.
- **Dim_Cenario.csv**: Contém origem e cenário dos dados.

### Tabela Fato (em `facts/`)
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

1. **Executar o Script de Processamento**:
   - Certifique-se de ter Python e Pandas instalados.
   - Execute `python src/estrutura_dados.py` para gerar os arquivos CSV a partir de `data/dados_ACT.xlsx`.

2. **Importar no Power BI**:
   - Abra o arquivo `Case_ACT.pbix` no Power BI Desktop.
   - Ou, crie um novo arquivo e importe os CSVs das pastas `dimensions/` e `facts/`.
   - Crie relacionamentos entre a tabela fato e as dimensões usando as chaves ID.

3. **Visualizar a Apresentação**:
   - Abra `Case para vaga de Consultor Power BI-v03.pptx` para entender o case e os requisitos.

## Dependências

- Python 3.x
- Pandas: `pip install pandas`
- Arquivo `data/dados_ACT.xlsx` (dados originais)

## Estrutura do Projeto

```
/
├── data/                          # Dados brutos
│   └── dados_ACT.xlsx
├── dimensions/                    # Tabelas dimensão
│   ├── Dim_Canal.csv
│   ├── Dim_Cenario.csv
│   ├── Dim_Indicador.csv
│   ├── Dim_Local.csv
│   ├── Dim_Produto.csv
│   └── Dim_Tempo.csv
├── facts/                         # Tabela fato
│   └── Fato_Vendas.csv
├── src/                           # Código fonte
│   └── estrutura_dados.py
├── Img/                           # Imagens (se utilizadas)
├── Case_ACT.pbix                  # Dashboard Power BI
├── Case para vaga de Consultor Power BI-v03.pptx  # Apresentação
├── README.md                      # Este arquivo
├── .gitignore                     # Arquivos ignorados pelo Git
└── .venv/                         # Ambiente virtual (ignorado)
```