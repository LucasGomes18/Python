from os import system, name
system ('cls') if(name=='nt') else system('clear')

"""
  Cap04 - Atividade 01
  Tabuada

  Objetivos:
  Nesta atividade você vai montar uma Tabuada usando a estrutura de Loop do For e range.

  Comandos utilizados:
  Comandos for e range
"""

for seila in range(0,20,2):
    print(f'{seila:2} - Lucas')
    print('----------')
print('**************') 

print('***Tabuada Simples***')
n = int(input('Informe o multiplicadorc:'))
for i in range(1,11):
    print(f'{i} x {n} = {n*i}')
print('------------------------')