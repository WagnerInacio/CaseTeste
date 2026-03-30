import pandas as pd

df = pd.read_excel('data/dados_ACT.xlsx')
df['DT_REF_MES'] = pd.to_datetime(df['DT_REF_MES'], origin='1899-12-30', unit='D')

def create_dim(df, cols, id_col):
    dim = df[cols].drop_duplicates().reset_index(drop=True)
    dim[id_col] = dim.index + 1
    return dim[[id_col] + cols]

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

fato = df.copy()
fato = fato.merge(dim_tempo[['ID_Tempo', 'DT_REF_MES']], on='DT_REF_MES', how='left')
fato = fato.merge(dim_local[['ID_Local', 'UF', 'CIDADE', 'DDD']], on=['UF', 'CIDADE', 'DDD'], how='left')
fato = fato.merge(dim_produto[['ID_Produto', 'PRODUTO', 'PLANO', 'TECNOLOGIA', 'SEGMENTO']], on=['PRODUTO', 'PLANO', 'TECNOLOGIA', 'SEGMENTO'], how='left')
fato = fato.merge(dim_canal[['ID_Canal', 'CANAL']], on='CANAL', how='left')
fato = fato.merge(dim_indicador[['ID_Indicador', 'INDICADOR_N1', 'INDICADOR_N2']], on=['INDICADOR_N1', 'INDICADOR_N2'], how='left')
fato = fato.merge(dim_cenario[['ID_Cenario', 'ORIGEM', 'CENARIO']], on=['ORIGEM', 'CENARIO'], how='left')
fato = fato[['ID_Tempo', 'ID_Local', 'ID_Produto', 'ID_Canal', 'ID_Indicador', 'ID_Cenario', 'valor']]

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
