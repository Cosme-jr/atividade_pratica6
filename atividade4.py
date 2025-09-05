"""
4 - 

Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
"""
import requests
import json

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    dados = resposta.json()
    if 'error' in dados:
        return None
    return dados[f'{moeda}BRL']

moeda = input("Informe o código da moeda (ex: USD, EUR, GBP): ")
cotacao = consultar_cotacao(moeda)
if cotacao:
    print("Valor atual:", cotacao['ask'])
    print("Valor máximo:", cotacao['high'])
    print("Valor mínimo:", cotacao['low'])
    print("Data da última atualização:", cotacao['create_date'])
else:
    print("Moeda não encontrada.")
