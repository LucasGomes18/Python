from os import system
def limparTela():
    system('cls||clear')

from  import soma, sub, mult, div #se quiser pode ser apenas: from calculadora import *, o '*' importa tudo do arquivo

while (True):
    
    limparTela()
    
    try:
        n1=float(input('Informe o 1º valor :'))
        n2=float(input('Informe o 2º valor :'))
    
    except ValueError:
        print('Opção inválida. informe somente numeros')
        input()
        continue #retorna para o inicio do loop
    
    print('\n Escolha a operação aritmética :')
    print(f'''
          1 - Somar
          2 - Subtrair
          3 - Multiplicar
          4 - Dividir
          ''')
    
    while True:
        operador = input('Digite a opção :')
        if operador in ['1', '2', '3', '4']:
            operador = int(operador)
            break
        
        else:
            print('Opção invalida! Escolha um número entre 1 e 4.')
    if operador==1:
            soma(n1,n2)
    if operador==2:
            sub(n1,n2)
    if operador==3:
            mult(n1,n2)
    if operador==4:
            div(n1,n2)
            
    opcao = input('Digite qualquer tecla para continuar ou X para encerrar :')
    if opcao.upper()=='X':
        break