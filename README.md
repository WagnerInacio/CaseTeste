# Teste Power BI

## Descrição do Case

Este projeto representa um teste de entrevista para a posição de Consultor em Power BI na ACT. O objetivo é demonstrar a habilidade de transformar dados brutos de uma planilha Excel em um modelo de dados estruturado, seguindo as melhores práticas de modelagem dimensional para Business Intelligence (BI).

O código Python abaixo (originalmente em `src/estrutura_dados.py`) utiliza a biblioteca Pandas para processar os dados originais e separá-los em tabelas dimensão e fato, criando um esquema estrela (star schema) adequado para análises em ferramentas como Power BI.

```python
import pandas as pd

# Carregar dados
df = pd.read_excel('data/dados_ACT.xlsx')
df['DT_REF_MES'] = pd.to_datetime(df['DT_REF_MES'], origin='1899-12-30', unit='D')

# Função para criar dimensão
def create_dim(df, cols, id_col):
    dim = df[cols].drop_duplicates().reset_index(drop=True)
    dim[id_col] = dim.index + 1
    return dim[[id_col] + cols]

# Criar dimensões
dim_tempo = create_dim(df, ['DT_REF_MES'], 'ID_Tempo')
dim_tempo['Ano'] = dim_tempo['DT_REF_MES'].dt.year
dim_tempo['Mes'] = dim_tempo['DT_REF_MES'].dt.month
dim_tempo['Mes_Nome'] = dim_tempo['DT_REF_MES'].dt.strftime('%B')
dim_tempo = dim_tempo[['ID_Tempo', 'DT_REF_MES', 'Ano', 'Mes', 'Mes_Nome']]

dim_local = create_dim(df, ['UF', 'CIDADE', 'DDD'], 'ID_Local')
dim_produto = create_dim(df, ['PRODUTO', 'PLANO', 'TECNOLOGIA', 'SEGMENTO'], 'ID_Produto')
dim_canal = create_dim(df, ['CANAL'], 'ID_Canal')
dim_indicador = create_dim(df, ['INDICADOR_N1', 'INDICADOR_N2'], 'ID_Indicador')
dim_cenario = create_dim(df, ['ORIGEM', 'CENARIO'], 'ID_Cenario')

# Criar fato
fato = df.copy()
fato = fato.merge(dim_tempo[['ID_Tempo', 'DT_REF_MES']], on='DT_REF_MES', how='left')
fato = fato.merge(dim_local[['ID_Local', 'UF', 'CIDADE', 'DDD']], on=['UF', 'CIDADE', 'DDD'], how='left')
fato = fato.merge(dim_produto[['ID_Produto', 'PRODUTO', 'PLANO', 'TECNOLOGIA', 'SEGMENTO']], on=['PRODUTO', 'PLANO', 'TECNOLOGIA', 'SEGMENTO'], how='left')
fato = fato.merge(dim_canal[['ID_Canal', 'CANAL']], on='CANAL', how='left')
fato = fato.merge(dim_indicador[['ID_Indicador', 'INDICADOR_N1', 'INDICADOR_N2']], on=['INDICADOR_N1', 'INDICADOR_N2'], how='left')
fato = fato.merge(dim_cenario[['ID_Cenario', 'ORIGEM', 'CENARIO']], on=['ORIGEM', 'CENARIO'], how='left')
fato = fato[['ID_Tempo', 'ID_Local', 'ID_Produto', 'ID_Canal', 'ID_Indicador', 'ID_Cenario', 'valor']]

# Salvar CSVs
dims = {
    'Dim_Tempo.csv': dim_tempo,
    'Dim_Local.csv': dim_local,
    'Dim_Produto.csv': dim_produto,
    'Dim_Canal.csv': dim_canal,
    'Dim_Indicador.csv': dim_indicador,
    'Dim_Cenario.csv': dim_cenario
}
for file, data in dims.items():
    data.to_csv(f'dimensions/{file}', index=False)
fato.to_csv('facts/Fato_Vendas.csv', index=False)

print('Estrutura criada com sucesso!')
```

O projeto inclui também um dashboard interativo desenvolvido no Power BI (`Case_ACT.pbix`), baseado nos dados processados conforme o código acima.

## Estrutura dos Dados

Os dados originais de uma planilha Excel contêm informações sobre vendas, incluindo datas, locais, produtos, canais, indicadores e cenários. Esses dados foram normalizados e separados em tabelas dimensão e fato, conforme o código Python acima, criando um esquema estrela. No arquivo `Case_ACT.pbix`, essas estruturas são implementadas da seguinte forma:

### Tabelas Dimensão
- **Dim_Tempo**: Contém informações temporais (data de referência, ano, mês, nome do mês).
- **Dim_Local**: Contém informações geográficas (UF, cidade, DDD).
- **Dim_Produto**: Contém detalhes dos produtos (produto, plano, tecnologia, segmento).
- **Dim_Canal**: Contém os canais de venda.
- **Dim_Indicador**: Contém indicadores de nível 1 e 2.
- **Dim_Cenario**: Contém origem e cenário dos dados.

### Tabela Fato
- **Fato_Vendas**: Contém as vendas medidas (valor), com chaves estrangeiras para as dimensões.

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

## Estrutura do Projeto

Este README descreve o projeto completo. Os arquivos enviados são:

- `README.md`: Este arquivo com descrição e código.
- `Case_ACT.pbix`: Dashboard Power BI com o modelo de dados e visualizações.

O projeto original inclui:
```
/
├── data/                          # Dados brutos (não incluído)
│   └── dados_ACT.xlsx
├── dimensions/                    # Tabelas dimensão (processadas no .pbix)
│   ├── Dim_Canal.csv
│   ├── Dim_Cenario.csv
│   ├── Dim_Indicador.csv
│   ├── Dim_Local.csv
│   ├── Dim_Produto.csv
│   └── Dim_Tempo.csv
├── facts/                         # Tabela fato (processada no .pbix)
│   └── Fato_Vendas.csv
├── src/                           # Código fonte (incluído acima)
│   └── estrutura_dados.py
├── Img/                           # Imagens (se utilizadas)
├── Case_ACT.pbix                  # Dashboard Power BI (enviado)
├── README.md                      # Este arquivo
└── .venv/                         # Ambiente virtual (ignorado)
```