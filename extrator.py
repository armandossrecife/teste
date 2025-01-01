import json
import pandas as pd

COMPRAS_JSON = "compras_por_fornecedor_2024.json"

def extract_fornecedores(file):
    """Extrai os valores de @Fornecedor de um JSON e os adiciona a uma lista.
    file: Arquivo JSON
    Returns:
        list: Uma lista contendo os valores de @Fornecedor.
    """
    fornecedores = []
    try:
      with open(file, 'r') as f:
        data = json.load(f)
      for item in data: 
        fornecedor = item['fornecedor']
        fornecedores.append(fornecedor)
    except Exception as ex:
        print(f"Erro: {str(ex)}")
    return fornecedores

# Função para extrair os dados de cada nota e item
def extrai_dados_compras_por_fornecedor(filename):
    # Carregando o JSON
    with open(filename, 'r') as f:
        data = json.load(f)

    result = []
    for fornecedor in data:
        for nota in fornecedor['notas']:
            for item in nota['itens']:
                row = {
                    'codigo_fornecedor': fornecedor['fornecedor']['codigo'],
                    'nome_fornecedor': fornecedor['fornecedor']['nome'],
                    'numero_nota': nota['numero'],
                    'data_lancamento': nota['data_lancamento'],
                    'data_emissao': nota['data_emissao'],
                    'data_vencimento': nota['data_vencimento'],
                    'codigo_item': item['codigo'],
                    'descricao': item['descricao'],
                    'quantidade': item['quantidade'],
                    'valor_unitario': item['valor_unitario'],
                    'ipi': item['ipi'],
                    'total_item': item['total_item']
                }
                result.append(row)
    return result

def extrai_dados_detalhes_notas_por_fornecedor(filename):
    # Carregando o JSON
    with open(filename, 'r') as f:
        data = json.load(f)

    result = []
    for fornecedor in data:
        for nota in fornecedor['notas']:
          row = { 
              'codigo_fornecedor': fornecedor['fornecedor']['codigo'],
                    'nome_fornecedor': fornecedor['fornecedor']['nome'],
                    'numero_nota': nota['numero'],
                    'data_lancamento': nota['data_lancamento'],
                    'data_emissao': nota['data_emissao'],
                    'data_vencimento': nota['data_vencimento'],
                    'despesas_adicionais': nota['detalhes']['Despesas adicionais'],
                    'seguro': nota['detalhes']['Seguro'],
                    'desconto': nota['detalhes']['Desconto'],
                    'valor_deducao': nota['detalhes']['Valor deduções'],
                    'frete': nota['detalhes']['Frete'],
                    'impostos': nota['detalhes']['Impostos'],
                    'acrescimo': nota['detalhes']['Acréscimo'],
                    'total_itens': nota['detalhes']['Total itens'],
                    'valor_total_nota': nota['detalhes']['Valor total da nota']
              }
          result.append(row)
    return result

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
