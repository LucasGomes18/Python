"""
  Cap08 - Atividade 01
  Abrir um arquivo 

  Objetivos:
  Nesta atividade você vai ler um arquivo no formato CSV, verificar as opções de 
  enconding (codificação de caracteres) e separar os arquivo em uma lista para ler 
  as informações de cada coluna.

  Comandos utilizados:
  Biblioteca os, comando open, path, lista e for
"""
import os.path, datetime
from os import system, name
system('cls') if(name == 'nt') else system('clear')

arquivo = 'produtos.csv'
if (os.path.isfile(arquivo)):
    produtos = open(arquivo, 'r', encoding='utf-8' ) #utf-8 é pra funcionar as Ç e acentos// o r e de read pra ler o arquivo
    tamanho = os.path.getsize(arquivo) #pega o tamanho do arquivo
    dtModificacao = os.path.getmtime(arquivo)
    print('Tamanho do arquivo (bytes) :', tamanho)
    print('Data de Modificação :', datetime.datetime.fromtimestamp(dtModificacao))
    listadeProdutos = []
    for line in produtos:
      colunas = line.strip().split(';') #Isso vai tirar os espaçoes antes e depois dos nomes e separar cada dado usando como referencia o ponto e virgula
      #colunas do tipo int
      colunas[0]=int(colunas[0])
      colunas[2]=int(colunas[2])
      colunas[4]=int(colunas[4])
      colunas[5]=int(colunas[5])
      colunas[6]=int(colunas[6])
      colunas[7]=int(colunas[7])
      #colunas do tipo float
      colunas[8]=float(colunas[8])
      colunas[9]=float(colunas[9])
      listadeProdutos.append(colunas)
    produtos.close()
    for prod in listadeProdutos:
      print(prod)

    
else:
    print ('Aquivo invalido')