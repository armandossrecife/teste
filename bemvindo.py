import sys
import datetime

versao_python = sys.version
data_hoje_local = datetime.datetime.today()

nome = input("Digite seu nome: ")
print(f"Data: {data_hoje_local}")
print(f"Olá {nome}, bem vindo ao Python!")
print(f"Este programa foi feito em Python na versão: {versao_python}")