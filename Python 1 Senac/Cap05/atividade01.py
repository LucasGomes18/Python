"""
python = 'Lista' ou 'Tupla'
            0       1         2         3        4
Nomes = ['José', 'Maria', 'Joaquim', 'Joana', 'João']
print(nomes[2])
print(nomes[1])

"""    

"""
  Cap05 - Atividade 01
  Número por Extenso
  Objetivos:
  Nesta atividade você vai escrever um número por extenso, para isto usará uma tupla. 
  A tupla é um array que contem dados que não pode ser alterados.
  Comandos utilizados:
  Tupla, operadores / e %
"""
from os import system, name
system('cls') if(name == 'nt') else system('clear')

# tupla é criada com () e não pode ter seus dados alterados
# lista é criada com [] e pode ter seus dados alterados

unidades = ('zero', 'um', 'doi', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
dezenas = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove')
rasos = ('', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setemta', 'noventa')

numero = int(input('Informe um número entre 0 e 99 para ser convertido para texto: '))

if numero <10:
    numTexto = unidades[numero]
    print (numTexto)
elif numero <20:
    numTexto = dezenas[numero-10]
    print (numTexto)

elif numero <100:
    u = numero % 10
    d = int(numero / 10)
    if u == 0:
         numTexto = f'{rasos[d]}'
    else:
        numTexto = f'{rasos[d]} e {unidades[u]}'
    print (numTexto)
    
else:
    numTexto = f'O valor {numero} é invalido'
    print (numTexto)