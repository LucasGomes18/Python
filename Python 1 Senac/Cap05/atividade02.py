"""
  Cap05 - Atividade 02
  Jogo: Papel, pedra e Tesoura

  Objetivos:
  Nesta atividade você vai criar um jogo usando tupla e tupla multi-dimensional.

  Comandos utilizados:
  Tupla, Tupla Multi-Dimensional, biblioteca random e randint
"""

from os import system, name

# biblioteca random
import random

opcao = 's'
while opcao.upper()=='S':

    system('cls') if(name == 'nt') else system('clear')

    opcoes = ('pedra', 'papel', 'tesoura')
    print('Escolha a sua jogada: ')
    for i, elemento in enumerate(opcoes):
        print(f'{i+1} - {elemento}')
    jogador=int(input())-1
    cpu = random.randint(0,2)
    
    JM = ('Jogador wins')
    CM = ('Cpu wins')
    EM = ('Empate')
    
    resultado = (
                    #0    1   2
                    (EM, JM, CM),#0
                    (CM, EM, JM),#1
                    (JM, CM, EM),#2
    )
    
    print(f'voce escolheu {opcoes[jogador]}')
    print(f'a cpu escolheu {opcoes[cpu]}')
    print(resultado[cpu][jogador])
    
    opcao = input('Digite S para continuar ou qualquer tecla para parar')