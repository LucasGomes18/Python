import os
os.system('cls')

nomeCompleto = input('Informe seu nome completo:')

#Função len retorna a quantidade de caracteres de uma variavel
print('1. Quantidade de caracteres:', len(nomeCompleto))

# upper transforma um texto em maiusculo
print('.2 Nome em maiusculo:', nomeCompleto.upper())

# lower transforma um texto em minusculo
print('.3 Nome em minusculo:', nomeCompleto.lower())

# capitalize deixa a primeira letra em maiusculo
print('.4 Nome com a primeira letra em maiusculo:', nomeCompleto.capitalize())

# separar o primeiro nome
espaco = nomeCompleto.find(' ')
# se usar print(espaco) ele ira exibir o numero do caracter que esta o primeiro espaço, no caso de lucas agrbiel figueredo gomes seria o 5, pois ele vem contando como 0,1,2,3...

print('5. somente o primeiro nome:' , nomeCompleto[0:espaco])

#alocar primeiro nome na variavel nome e depois so o sobrenome, daqui ate a linha 33
nome = nomeCompleto[0:espaco]

    """_summary_
    logo a baixo eu criei a variavel sobrenome,jogando dentro dela o a nomeCompleto e buscando na nomeCompleto o primeiro espaço +1 que ue tinha ja localizado e com o len definindo
    para ir desse ponto do espaço +1 adiante assim so pulando o primeiro nome que ta antes do pimeiro espaço
    """
sobrenome = nomeCompleto [espaco+1:len(nomeCompleto)]
print('somente primeiro nome', nome)
print('somente o segundo nome', sobrenome)

#metodo replace para tirar todos os espaços em branco
print('6. Nome sem espaços', nomeCompleto.replace(' ','') )

#metodo isalpha para verificar se tem somente letras
somenteLetras = nomeCompleto.replace(' ','')#primeiro tiro os espaços
print('.7 tem Somente letras', somenteLetras.isalpha())

#metodo para verificar se tem numeros ou letras
print('.8 É alphanumerico? tem letras ou numeros:' , somenteLetras.isalnum())

#metodo split cria uma lista usando o espaço em branco como quebra
#exemplo ['lucas', 'gabriel']
print('9. quebra os texto a cada espaço em branco', nomeCompleto.split(" "))

#metodo center para centralizar o texto em 80 colunas usando o *
print('10. Centralizar o nome entre*: ')
print(nomeCompleto.center (80,'*'))


