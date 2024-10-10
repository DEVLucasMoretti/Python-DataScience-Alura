# Vamos praticar o uso de vários tipos de variáveis e da função input a partir de algumas atividades. Solucione os problemas propostos em código.


####################  Calculadora com operadores  ####################

#1 Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.
name = input("Digite o seu nome: ")
print(f'Olá, {name}.\n')

#2 Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
name = input("Digite o seu nome: ")
year = input("Digite a sua idade: ")
print(f'Olá, {name}, você tem {year} anos.\n')

#3 Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
name = input("Digite o seu nome: ")
year = input("Digite a sua idade: ")
height = input("Digite a sua altura:")
print(f'Olá, {name}, você tem {year} anos e mede {height} metros.\n')

#4 Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
print(f'A soma de {a} + {b} = {a+b}')

#5 Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))
print(f'A soma de {a} + {b} + {c} = {a+b+c}')

#6 Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
print(f'A soma de {a} - {b} = {a-b}')

#7 Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
a = int(input("Digite um numerador: "))
b = int(input("Digite um denominador(não pode ser zero): "))
print(f'A Divisão de {a} por {b} é {a/b}')

#8 Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
a = int(input("Digite um operador: "))
b = int(input("Digite uma potência): "))
print(f'A exponenciação entre esses dois valores é {a**b}')

#9 Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
a = int(input("Digite um numerador: "))
b = int(input("Digite um denominador(não pode ser zero): "))
print(f'A Divisão inteira de {a} por {b} é {a//b}')

#10 Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0
a = int(input("Digite um numerador: "))
b = int(input("Digite um denominador(não pode ser zero): "))
print(f'O resto da divisão de {a} por {b} é {a % b}')

#11 Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
a = int(input("Digite uma nota: "))
b = int(input("Digite uma nota: "))
c= int(input("Digite uma nota: "))
avg = (a+b+c)/3
print(f'A média das notas é {avg}')

#12 Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
sum=0
weight=0
numbers= [5,12,20,15] 
for i in range(4):
    weight = weight + (i+1)
    print(weight)
    sum= sum + numbers[i]*(i+1)
    
print(f'A média ponderada é {sum/weight}')


####################  Editando textos  ####################

#1 Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
frase = 'Python'
print(frase)

#2 Crie um código que solicite uma frase e depois imprima a frase na tela.
frase = input('Escreva uma frase: ')
print(frase)

#3 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
frase = input('Escreva uma frase:')
print(frase.upper())

#4 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
frase = input('Escreva uma frase:')
print(frase.lower())

#5 Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
frase = " Frase vai ficar sem espaços no Início e Final          "
print(frase.strip())

#6 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
frase = input('Escreva uma frase: ')
print(frase.strip())

#7 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
frase = input('Escreva uma frase: ')
print(frase.strip().lower())

#8 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
frase = input('Escreva uma frase: ')
print(frase.replace('e','f'))

#9 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”
frase = input('Escreva uma frase: ')
print(frase.replace('a','@'))

#10 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
frase = input('Escreva uma frase: ')
print(frase.replace('s','$'))