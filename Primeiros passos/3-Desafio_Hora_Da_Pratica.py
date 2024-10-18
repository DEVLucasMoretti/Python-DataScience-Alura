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

#9 Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
n = float(input("Digite um valor: "))

print("O valor é um número inteiro!") if n == int(n) else print("O valor é um número decimal!")





########################################  Momento dos projetos  ########################################



#10 Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
def operecao_a_ser_realizada(n1,n2,op):
    if(op =='+'):
        return num1 + num2
    elif(op =='-'):
            return  num1 - num2
    elif(op =='/'):
        return  num1 / num2
    elif(op =='*'):
        return  num1 * num2
    else:
        print("Opereção Inválida")

def impar_ou_par(num):
    num_str = str(num)
    verify_num= num_str.split('.')
    list_num = []
    list_num.append(int(verify_num[0]))
    list_num.append(int(verify_num[1]))
    if(list_num[1] == 0):
        list_num_int = list(map(int,str(list_num[0])))
        for i in range(0,10,2):
            if (list_num_int[-1] == i): #Verificamos se o último algarismo é par
                return "par"
        for i in range(1,10,2):
            if (list_num_int[-1]== i): #Verificamos se o último algarismo é ímpar
                return "ímpar"
    else:
        list_num_float = list(map(int,str(list_num[1])))
        print(list_num_float)
        for i in range(0,10,2):
            if (list_num_float[-1] == i): #Verificamos se o último algarismo é par
                return "par"
        for i in range(1,10,2):
            if (list_num_float[-1]== i): #Verificamos se o último algarismo é ímpar
                return "ímpar"

def inteiro_ou_decimal(num):
    if num == int(num):
        return "inteiro"
    else:
        return "decimal"

def positivo_ou_negativo(num):
    if num > 0:
     return "positivo"
    else: 
        return"negativo"

num1 = float(input("Digite um valor: "))
num2 = float(input("Digite outro valor: "))
print("(+) Para soma\n(-) Para subtração\n(/) Para divisão\n(*) Para multiplicação")
op = input("Digite qual operação deseja fazer: ")

result = (operecao_a_ser_realizada(num1,num2,op))
print(f'O resultado da operação é {result}.\nO número é {impar_ou_par(result)},{positivo_ou_negativo(result)} e {inteiro_ou_decimal(result)}.')





#11 Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes.

def forma_triangulo(a,b,c): # Verifica se é possível formar um triângulo
    if(a+b>c and a+c>b and b+c>a):
        return True
    else:
       return False
def forma_equilatero(a,b,c): # Verifica se triângulo é Equilatero
    if(a==b and a==c and b==c):
        return True
def forma_isosceles(a,b,c): # Verifica se triângulo é Isósceles
    if(a==b)or(a==c) or(b==c):
        return True
def forma_escaleno(a,b,c): # Verifica se triângulo é Escaleno
    if(a!=b and a!=c and b!=c):
        return True

a = int(input("Digite o 1º valor inteiro do lado do triângulo: "))
b = int(input("Digite o 2º valor inteiro do lado do triângulo: "))
c = int(input("Digite o 3º valor inteiro do lado do triângulo: "))

if(forma_triangulo(a,b,c) == True): # Se for possível forma um triângulo, ele verifica o tipo dele.
    if forma_equilatero(a,b,c) == True:
        print("O triângulo é Equilátero")
    elif forma_escaleno(a,b,c) == True:
        print("O triângulo é Escaleno")
    elif forma_isosceles(a,b,c) == True:
        print("O triângulo é Isósceles")
else:
    print("Os valores informados não formam nenhum triângulo")





#12 Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:
#O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
#O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
def discount_etanol(liters):
    if(liters <= 15):
        return 1.7 * liters * 0.98
    else:
        return 1.7 * liters * 0.96    
def discount_diesel(liters):
    if(liters <= 15):
        return 2 * liters * 0.97
    else:
        return 2 * liters * 0.95

l = float(input("Quantos litros foram vendidos: "))
comb = input("Qual o tipo de combustível (E - etanol e D - diesel): ").upper()

if( comb == "E"):
    print(f"O valor a ser pago em {l} litros de etanol é R${l*discount_etanol(l):,.2f}")
elif( comb == "D"):
    print(f"O valor a ser pago em {l} litros de disel é R${l*discount_diesel(l):,.2f}")
else:
    "Valor de combustível inválido! "

