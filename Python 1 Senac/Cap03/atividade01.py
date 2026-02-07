"""
Cap03 - Atividade 01
vericar numero Par e Impar

Objetivos:
Nesta atividade Voce vai usar uma estrutura de decisao (if/else) para verificar se um numero e par ou impar

Comandos utilizados:
If, operador % (retorna o resto da divisao entre operados)

"""

import os
os.system('cls')

numero = int(input('Informe um numero inteiro: '))
resto = int(numero % 2)
if resto == 0:
    print (f'O numero {numero} é: Par')
else:
    print (f'O numero {numero} é: Impar')
print()
print('----------')
print('**********')
print ('final do algoritimo')