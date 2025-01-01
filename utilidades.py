import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def convert_valor_total_to_float(valor_total_str):
  """
  Converts a string representing a value with dots and commas
  (e.g., '1.202.016,73') to a float.

  Args:
    valor_total_str: The string representing the value.

  Returns:
    The converted float value.
  """
  try:
    # Replace dots with empty strings to remove the thousands separator
    valor_total_str = valor_total_str.replace('.', '')
    # Replace comma with dot for the decimal separator
    valor_total_str = valor_total_str.replace(',', '.')
    return float(valor_total_str)
  except ValueError:
    print(f"Error: Could not convert '{valor_total_str}' to float.")
    return None

def extract_user_info(user_str):
    """
    Extracts user ID and name from a string in the format "0399 - FRANCISCO DAS".
    Args:
        user_str: The string containing user ID and name.
    Returns:
        tuple: A tuple containing (user_id, user_name).
    """
    try:
        user_id, user_name = user_str.split(" - ")
        return user_id, user_name
    except ValueError:
        return None, None

def add_user_to_movimentacoes(df_users, df_movimentacoes):
	# Merge df_movimentacoes with df_users to add 'usuarioId' to df_movimentacoes
	# First, extract just the user_id from the original user column
    df_movimentacoes['temp_usuarioId'] = df_movimentacoes['usuarioId'].apply(lambda x: extract_user_info(x)[0] if extract_user_info(x) else None)
	#Merge the dataframes using the temporary user_id
    df_movimentacoes = pd.merge(df_movimentacoes, df_users, left_on='temp_usuarioId', right_on='usuarioId', how='left', suffixes=('', '_y'))
	#Drop the temporary user id
    df_movimentacoes.drop('temp_usuarioId', axis=1, inplace=True)
	# Drop any redundant columns added by the merge operation (if any)
    df_movimentacoes.drop(columns=[col for col in df_movimentacoes.columns if col.endswith('_y')], inplace=True)
    return df_movimentacoes

def add_fabricanteid_to_movimentacoes(df_fabricantes, df_movimentacoes):
    # Create a mapping from 'FabricanteDescricao' to 'id' from df_fabricantes
    fabricante_mapping = df_fabricantes['FabricanteDescricao'].to_dict()
    fabricante_id_mapping = {v: k for k, v in fabricante_mapping.items()}

	# Add 'fabricanteId' to df_movimentacoes based on 'FabricanteDescricao'
    df_movimentacoes['fabricanteId'] = df_movimentacoes['FabricanteDescricao'].map(fabricante_id_mapping)
    return df_movimentacoes

def carrega_resumo_relatorio_movimentacoes(dados):
    # Acessando a lista de dicionários
    dados_resumo = dados['dadosResumo']
    return dados_resumo

def converte_dados_resumo_para_dataframe(dados_resumo):
    # Criando um DataFrame do Pandas para facilitar a manipulação
    df = pd.DataFrame(dados_resumo)
    df['ValorTotalReal'] = df['ValorTotal']
    # Convertendo 'ValorTotal' para um tipo numérico (float)
    df['ValorTotal'] = df['ValorTotal'].apply(convert_valor_total_to_float)

    # Ordenando o DataFrame por 'ValorTotal' em ordem ascendente
    df = df.sort_values(by='ValorTotal', ascending=False)
    return df

def cria_grafico_barras_movimentacoes(df):
    # Criando o gráfico de barras
    plt.figure(figsize=(16, 6))
    bars = plt.barh(df['Agrupamento'], df['ValorTotal'])

    # Adicionando os valores nas barras
    for bar in bars:
        yval = bar.get_y() + bar.get_height() / 2
        plt.text(bar.get_width() + 5, yval, round(bar.get_width(), 2))

    plt.xlabel('Agrupamento')
    plt.ylabel('Valor Total')
    plt.title('Movimentações 2024 - Valor Total por Agrupamento')
    plt.xticks(rotation=45)
    plt.show()

def cria_df_centro_custo(df):
    # Ordenando o DataFrame por 'ValorTotal' em ordem ascendente
    df_centro_custo = df.sort_values(by='CentroCusto')
    return df_centro_custo

def cria_df_administrativo(df):
    df_administrativo = df[df['CentroCusto'] == 'ADMINISTRATIVO']
    return df_administrativo

def cria_df_area_tecnica_cto(df):
    df_area_tecnica_cto = df[df['CentroCusto'] == 'AREA TECNICA CTO']
    return df_area_tecnica_cto

def cria_df_coleta_unimed_primavera(df):
    df_coleta_unimed_primavera = df[df['CentroCusto'] == 'POSTO DE COLETA HOSPITAL HTI']
    return df_coleta_unimed_primavera

def cria_df_coleta_hospital_hti(df):
    df_coleta_hospital_hti = df[df['CentroCusto'] == 'POSTO DE COLETA HOSP. UNIMED PRIMAVERA']
    return df_coleta_hospital_hti

def cria_df_unidade_jockey(df):
    df_unidade_jockey = df[df['CentroCusto'] == 'UNIDADE JOCKEY']
    return df_unidade_jockey

def cria_df_unidade_matriz(df):
    df_unidade_matriz = df[df['CentroCusto'] == 'UNIDADE MATRIZ']
    return df_unidade_matriz

def cria_df_indefinido(df):
    df_indefinido = df[df['CentroCusto'] == 'Indefinido']
    return df_indefinido

def cria_treemap_movimentacoes(df):
    # Criando o treemap
    fig = px.treemap(df, path=['CentroCusto', 'Agrupamento'], values='ValorTotal',
                  color='CentroCusto', hover_data=['ValorTotalReal'])
    fig.show()

def cria_df_itens(df_movimentacoes):
    df_itens = df_movimentacoes[['itemId', 'itemDescricao']]
    df_itens.drop_duplicates(inplace=True)
    return df_itens

def cria_df_itens_movimentacoes(df_movimentacoes):
    colunas_uteis = ["itemId","itemDescricao","tipo","tipoItem", "data","especificacao","loteQuantidade","LoteId", "LoteValidade","precoMedio","valorTotal"]
    df_itens_movimentacoes = df_movimentacoes[colunas_uteis]
    return df_itens_movimentacoes

def cria_df_movimentacoes_entradas(df_movimentacoes_organizado):
    consulta_entradas = "tipo=='E'"
    df_movimentacoes_entradas = df_movimentacoes_organizado.query(consulta_entradas)
    return df_movimentacoes_entradas

def cria_df_movimentacoes_entradas_compra(df_movimentacoes_organizado):
    consulta_entrada_compra = "tipo=='E' and especificacao=='Ordem de compra'"
    df_movimentacoes_entradas_compra = df_movimentacoes_organizado.query(consulta_entrada_compra)
    return df_movimentacoes_entradas_compra

def cria_df_quantidades_movimentacoes_entradas_compra(data):
    df_quantidades_movimentacoes_entradas_compra = pd.DataFrame(data)
    return df_quantidades_movimentacoes_entradas_compra

# Percentual de tipo_de_itens_em_movimentacoes_de_compra
def cria_grafico_tipo_de_itens_em_movimentacoes_de_compra(df_quantidades_movimentacoes_entradas_compra):
    # prompt: crie um gráfico pie para representar o percentual das quantidades de df_quantidades_movimentacoes_entradas_compra
    # Create the pie chart using plotly
    fig = px.pie(df_quantidades_movimentacoes_entradas_compra, values='quantidade', names='tipo_item', title='Percentual de Tipos de Itens em Movimentações de Compra')
    fig.show()

def cria_grafico_movimentacoes_valor_total_por_mes(df_movimentacoes_entradas_compra):
    # prompt: Baseado na data do dataframe df_movimentacoes_entradas_compra, como fazer um gráfico de compras mensais para mostrar valorTotal  
    # por mês para os meses de janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro de 2024?
    # Filter data for 2024
    df_2024 = df_movimentacoes_entradas_compra[df_movimentacoes_entradas_compra['data'].dt.year == 2024]

    # Group by month and sum 'valorTotal'
    monthly_purchases = df_2024.groupby(df_2024['data'].dt.month)['valorTotal'].sum()

    # Create a list of month names
    month_names = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    # Select months from January to November
    selected_months = monthly_purchases.loc[1:11]

    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(month_names[:11], selected_months.values)
    plt.xlabel('Mês')
    plt.ylabel('Valor Total de Compras')
    plt.title('Compras Mensais - 2024 (Janeiro a Novembro)')
    plt.grid(True)
    plt.show()

def cria_df_movimentacoes_consumo(df_movimentacoes_organizado):
    consulta_consumo = "tipo=='S'"
    df_movimentacoes_consumo = df_movimentacoes_organizado.query(consulta_consumo)
    return df_movimentacoes_consumo

def cria_df_lotes(df_movimentacoes):
    df_lotes = df_movimentacoes[['LoteId',	'LoteValidade']]
    df_lotes.drop_duplicates(inplace=True)
    return df_lotes

def cria_df_fabricantes(df_movimentacoes):
    colunas_fabricantes = ['fabricanteId', 'FabricanteDescricao']
    df_fabricantes = df_movimentacoes[colunas_fabricantes]
    df_fabricantes.drop_duplicates(inplace=True)
    return df_fabricantes

def cria_df_users(df_movimentacoes):
    s_users = df_movimentacoes['usuarioId']
    # Apply the function to each element in the series
    user_info_list = s_users.apply(extract_user_info).tolist()
    user_info_list = list(set(user_info_list))
    df_users = pd.DataFrame(user_info_list, columns=['usuarioId', 'nome'])
    return df_users    
