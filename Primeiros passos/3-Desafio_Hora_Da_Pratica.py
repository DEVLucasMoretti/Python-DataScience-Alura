# Vamos praticar o uso de estruturas condicionais como o if, else e elif a partir de algumas atividades. 

#1 Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))

print(f'Maior valor é {a}') if a > b else print(f'Maior valor é {b}') #If Ternário

#2 Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
p= float(input("Informe o percentual de crescimento de produção de uma empresa: "))
print(f'porcentagem negativa') if p>0 else print(f'porcentagem negativa')

#3 Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
letter = input("Digite uma letra: ").upper()
print(f'A letra {letter} é uma Vogal') if (letter == "A" or letter =="E" or letter =="I" or letter =="O" or letter =="U") else print(f'A letra {letter} é uma Consoante')

#4 Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
v1 = float(input(f'Informe o valor médio do carro no 1º ano: '))
v2 = float(input(f'Informe o valor médio do carro no 2º ano: '))
v3 = float(input(f'Informe o valor médio do carro no 3º ano: '))

max_value = v1
#Verifica o maior valor
if(v2 > max_value): 
    max_value = v2
if (v3 > max_value):
    max_value = v3
#Verifica o menor valor
min_value= v1
if(v2 < min_value):
    min_value = v2
if(v3 < min_value):
    min_value = v3

print(f'O maior o valor médio do carro é R${max_value:,.2f} e o menor R${min_value:,.2f}')

#5 Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
v1 = float(input(f'Informe o valor do 1º produto: '))
v2 = float(input(f'Informe o valor do 1º produto: '))
v3 = float(input(f'Informe o valor do 1º produto: '))

min_value= v1
if(v2 < min_value):
    min_value = v2
if(v3 < min_value):
    min_value = v3

print(f'O produto mais barato é do preço de R${min_value:,.2f}')

#6 Escreva um programa que leia três números e os exiba em ordem decrescente
def bubble_sort_desc(numbers): #método de ordenação
    n = len(numbers)
    for i in range(n):
        trade = False
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:  # decrescente
                # Troca os elementos
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                trade = True
        # Se não houve troca, a lista está ordenada
        if not trade:
            break

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

numbers = [n1, n2, n3]

# Chamar a função de ordenação
bubble_sort_desc(numbers)

print(numbers)

#7 Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
per = input("Digite o turno que você estuda(manhã, tarde ou noite): ").lower()

if per == 'manhã':
    print('Bom Dia!')
elif per == 'tarde':
    print('Boa Tarde!')
elif per == 'noite':
    print('Boa Noite!')
else:
    print('Valor Inválido!')

#8 Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo
def separa_algarismos(numero):
    return list(map(int,str(numero))) #converte o valor para inteiro e converter cada algorismo para um índice na lista
    #Ex: "2003"
    #retorna uma lista [2,0,0,3]
def verificar_impar_ou_par(numeros_lista):
    tamanho = len(numeros_lista) #Verifica tamanho da lista para verficar quantos índices tem
    for i in range(0,10,2):  # Verificamos se o útlimo algarismo da lista é 0,2,4,6,8  = PAR
        if(numeros_lista[tamanho-1]== i):
            print("O Número é Par")
    for i in range(1,10,2):  # Verificamos se o útlimo algarismo da lista é 1,3,5,7,9  = ÍMPAR
        if(numeros_lista[tamanho-1]== i):
            print("O Número é Impar")

n = input("Digite um número inteiro para verificar de o número é Ímpar ou Par: ")
numeros_lista = separa_algarismos(n) 
verificar_impar_ou_par(numeros_lista)
#Fiz sem colocar as variáveis em inglês para um melhor entendimento do código ^-^



