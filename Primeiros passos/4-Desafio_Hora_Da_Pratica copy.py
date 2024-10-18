# Primeiro, vamos solucionar alguns problemas para aquecer e nos prepararmos para os projetos.

#1 Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
v1 = int(input("Digite um valor inteiro: "))
v2 = int(input("Digite outro valor inteiro: "))
array = []
for i in range(v1+1,v2,1):
    array.append(i)
print(f'Os valores entre {v1} e {v2} são: {array}')

#2 Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
a=4 
b=10
count=0
while (b>a):
    a= a * 1.03
    b= b * 1.015
    count+=1
print(f'Vai demora {count} dias para  a colônia da bactéria A ultrapassar ou igualar a colônia de uma bactéria B')


############################### Momento dos projetos ###############################

#3 Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária.
n = int(input("Digite um valor inteiro para visualizar sua tabuada: "))
print(f'Tabuada do {n}:')
for i in range(11):
    print(f'{n} x {i} = {n*i}')

#4 Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
n = int(input("Digite um valor inteiro para visualizar se é primo ou não: "))

array = []
for i in range(1,n+1,1):
    if(n % i == 0):   
        array.append(i)  # Se for divisível por esse valor ele adicona no array
if(len(array) > 2): # Como o número só primo pode ser divisível por 1 e por ele mesmo, logo, o tamanho do array tem que ser 2, caso não for, não será primo
    print("O valor não é primo")
else:
        print("O valor é primo")

#5 Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.
category_a = 0;category_b = 0;category_c = 0;category_d = 0
age = 0
print("----------------Distribuição de Idades de Pensionistas----------------")
print("Digite -1 para sair.")

while(age != -1):
    age = int(input("Digite a sua idade: "))
    if(age>-1 and age <= 25):
        category_a= category_a + 1
    elif(age > 25 and age <=50):
        category_b = category_b + 1
    elif(age>50 and age<=75):
        category_c = category_c + 1
    elif(age > 75 and age <=100):
        category_d = category_d + 1

print("\n----------------Distribuição de Idades de Pensionistas----------------")
print(f'{category_a} [0-25], {category_b} [26-50], {category_c} [51-75] e {category_d} [76-100]\n')

#6 Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:
#Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
vot =[]
vot_all =[1,1,1,1,2,3,2,3,4,4,5,5,5,5,6,6,2,1,2,3]
a=0;b=0;c=0;d=0;e=0;f=0
for i in range(len(vot_all)):
    if(vot_all[i] == 1):
        a = a +1
    elif(vot_all[i] == 2):
        b = b + 1
    elif(vot_all[i] == 3):
        c = c + 1
    elif(vot_all[i] == 4):
        d = d + 1
    elif(vot_all[i] == 5):
        e = e + 1
    elif(vot_all[i] == 6):
        f = f + 1

vot.extend([a,b,c,d,e,f])

print(f' Candidato 1 teve {vot[0]} votos.')
print(f' Candidato 2 teve {vot[1]} votos.')
print(f' Candidato 3 teve {vot[2]} votos.')
print(f' Candidato 4 teve {vot[3]} votos.')
print(f' Em Nulo teve {vot[4]} votos({vot[4]*100/20}%).')
print(f' Em branco teve {vot[5]} votos({vot[5]*100/20}%).')
