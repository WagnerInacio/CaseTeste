import pandas as pd

df = pd.read_excel('d:/05 - PROJETOS/Teste Entrevista ACT Power BI/dados_ACT.xlsx')

df['DT_REF_MES'] = pd.to_datetime(df['DT_REF_MES'], origin='1899-12-30', unit='D')

dim_tempo = df[['DT_REF_MES']].drop_duplicates().reset_index(drop=True)
dim_tempo['ID_Tempo'] = dim_tempo.index + 1
dim_tempo['Ano'] = dim_tempo['DT_REF_MES'].dt.year
dim_tempo['Mes'] = dim_tempo['DT_REF_MES'].dt.month
dim_tempo['Mes_Nome'] = dim_tempo['DT_REF_MES'].dt.strftime('%B')
dim_tempo = dim_tempo[['ID_Tempo', 'DT_REF_MES', 'Ano', 'Mes', 'Mes_Nome']]

dim_local = df[['UF', 'CIDADE', 'DDD']].drop_duplicates().reset_index(drop=True)
dim_local['ID_Local'] = dim_local.index + 1
dim_local = dim_local[['ID_Local', 'UF', 'CIDADE', 'DDD']]

dim_produto = df[['PRODUTO', 'PLANO', 'TECNOLOGIA', 'SEGMENTO']].drop_duplicates().reset_index(drop=True)
dim_produto['ID_Produto'] = dim_produto.index + 1
dim_produto = dim_produto[['ID_Produto', 'PRODUTO', 'PLANO', 'TECNOLOGIA', 'SEGMENTO']]

dim_canal = df[['CANAL']].drop_duplicates().reset_index(drop=True)
dim_canal['ID_Canal'] = dim_canal.index + 1
dim_canal = dim_canal[['ID_Canal', 'CANAL']]

dim_indicador = df[['INDICADOR_N1', 'INDICADOR_N2']].drop_duplicates().reset_index(drop=True)
dim_indicador['ID_Indicador'] = dim_indicador.index + 1
dim_indicador = dim_indicador[['ID_Indicador', 'INDICADOR_N1', 'INDICADOR_N2']]

dim_cenario = df[['ORIGEM', 'CENARIO']].drop_duplicates().reset_index(drop=True)
dim_cenario['ID_Cenario'] = dim_cenario.index + 1
dim_cenario = dim_cenario[['ID_Cenario', 'ORIGEM', 'CENARIO']]

fato = df.copy()
fato = fato.merge(dim_tempo[['ID_Tempo', 'DT_REF_MES']], on='DT_REF_MES', how='left')
fato = fato.merge(dim_local[['ID_Local', 'UF', 'CIDADE', 'DDD']], on=['UF', 'CIDADE', 'DDD'], how='left')
fato = fato.merge(dim_produto[['ID_Produto', 'PRODUTO', 'PLANO', 'TECNOLOGIA', 'SEGMENTO']], on=['PRODUTO', 'PLANO', 'TECNOLOGIA', 'SEGMENTO'], how='left')
fato = fato.merge(dim_canal[['ID_Canal', 'CANAL']], on='CANAL', how='left')
fato = fato.merge(dim_indicador[['ID_Indicador', 'INDICADOR_N1', 'INDICADOR_N2']], on=['INDICADOR_N1', 'INDICADOR_N2'], how='left')
fato = fato.merge(dim_cenario[['ID_Cenario', 'ORIGEM', 'CENARIO']], on=['ORIGEM', 'CENARIO'], how='left')
fato = fato[['ID_Tempo', 'ID_Local', 'ID_Produto', 'ID_Canal', 'ID_Indicador', 'ID_Cenario', 'valor']]

dim_tempo.to_csv('d:/05 - PROJETOS/Teste Entrevista ACT Power BI/Dim_Tempo.csv', index=False)
dim_local.to_csv('d:/05 - PROJETOS/Teste Entrevista ACT Power BI/Dim_Local.csv', index=False)
dim_produto.to_csv('d:/05 - PROJETOS/Teste Entrevista ACT Power BI/Dim_Produto.csv', index=False)
dim_canal.to_csv('d:/05 - PROJETOS/Teste Entrevista ACT Power BI/Dim_Canal.csv', index=False)
dim_indicador.to_csv('d:/05 - PROJETOS/Teste Entrevista ACT Power BI/Dim_Indicador.csv', index=False)
dim_cenario.to_csv('d:/05 - PROJETOS/Teste Entrevista ACT Power BI/Dim_Cenario.csv', index=False)
fato.to_csv('d:/05 - PROJETOS/Teste Entrevista ACT Power BI/Fato_Vendas.csv', index=False)

print('Estrutura criada com sucesso!')
print('Arquivos salvos:')
print('- Dim_Tempo.csv')
print('- Dim_Local.csv')
print('- Dim_Produto.csv')
print('- Dim_Canal.csv')
print('- Dim_Indicador.csv')
print('- Dim_Cenario.csv')
print('- Fato_Vendas.csv')