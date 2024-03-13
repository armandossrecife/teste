import sys
import datetime
import os

my_so = sys.platform
versao_python = sys.version
data_hoje_local = datetime.datetime.today()

if my_so.startswith("linux") or my_so.startswith("darwin"):
    os.system("clear")
else:
    os.system("cls")

print(f"Data: {data_hoje_local}")

nome = input("Digite seu nome: ")

print(f"Olá {nome}, bem vindo ao Python!")
print(f"Este programa foi feito em Python na versão: {versao_python}")
print(f"Sistema Operacional: {my_so}")