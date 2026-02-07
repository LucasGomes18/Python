"""
  Cap03 - Atividade Extra
  Calcular IMC

  Objetivos:
  Nesta atividade você vai calcular o IMC a partir de um peso e uma 
  altura, usará a comando if para mostrar o resultado do calculo do IMC.
    Ex: IMC = 70 kg / (1,60 m x 1,60 m) = 70 kg / 2,56 m² = 27,3 
        IMC <18,5kg/m2 - baixo peso
        IMC >18,5 até 24,9kg/m2 - eutrofia (peso adequado)
        IMC ≥25 até 29,9kg/m2 - sobrepeso
        IMC >30,0kg/m2 até 34,9kg/m2 - obesidade grau 1
        IMC >35kg/m2 até 39,9kg/m2 - obesidade grau 2
        IMC > 40kg/m2 - obesidade extrema
  Comandos utilizados:
  Variáveis, if / elif / else
"""

from os import system, name
system ('cls') if(name=='nt') else system('clear')

peso = float(input('Informe seu peso : '))
altura = float(input('informe sua altura : '))

imc = peso/(altura*altura)

if imc < 18.5:
    print ('baixo peso')
    
elif imc > 18.5 and imc <= 24.9:
    print ('eutrofia (peso adequado)')
    
elif imc >= 25 and imc <= 29.9:
    print ('sobrepeso')
    
elif imc >= 30 and imc <= 34.9:
    print ('obesidade grau 1')
    
elif imc >= 35 and imc <= 39.9:
    print ('obesidade grau 2')
    
elif imc > 40:
    print ('obesidade extrema')
    
print(f'seu imc é {imc:.2f}')
pesomin = ((altura*altura)*18.5)
pesomax = ((altura*altura)*24.9)
print (f'Seu peso ideal deve ser entre : {pesomin:.2f} e {pesomax:.2f}')