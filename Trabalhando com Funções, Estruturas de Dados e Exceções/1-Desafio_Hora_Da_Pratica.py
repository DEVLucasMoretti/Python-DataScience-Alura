import random
import math
#1  Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.
max_people = int(input("Informe a quantidade de participantes: "))
winner = random.randint(0,max_people)

print(f'O ganhador foi o de número --> [{winner}]')

#2 Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
count=1 
name = input('Qual o seu nome?\nR: ') 

while(count!=0):
    token = random.randint(1000,9998)
    if(token % 2 ==0):
        count=0
        print('\n\n')
        print(f'_________________  {name} o seu token gerado é [{token}]  _________________')
        print('\n\n')

#3 Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:
frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

len_frutas = len(frutas) # verificamos o tamanho lista 

salada_de_frutas_surpresa = [] #criamos a lista da salada de frutas surpresa
while(len(salada_de_frutas_surpresa) < 3): #enquanto a lista de salada de frutas surpresa for < 3, vai adicionar elementos nela, queros 3 frutas apenas , por isso essa condição
    i = random.randint(0,len_frutas-1) # vai sortear da lista original frutas uma delas, coloquei o -1 porque vai retornar tamnho 12 mas não existe index 12, por isso o -1, variando de index 0 a 11
    if (salada_de_frutas_surpresa.__contains__(frutas[i]) == False): #Para não haver reptição na lista, se não tiver a fruta já , na minha lista nova, vai adiconar
        salada_de_frutas_surpresa.append(frutas[i])

print(f' A salada de fruta surpresa tem os ingredientes: {salada_de_frutas_surpresa}')

#4 Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte:
#No final, informe quais números possuem raízes inteiras e seus respectivos valores.
numeros = [2, 8, 15, 23, 91, 112, 256]

for i in range(len(numeros)):
    raiz = math.sqrt(numeros[i])
    if(raiz == int(raiz)):
        print(f'O número {numeros[i]} possui raíz inteira e seu respectivos valor é {raiz:.0f}.')

# 5 Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.
print("o preço do metro quadrado da grama é de R$ 25,00.")
r = float(input('Digite o raio da área circular do jardim:  '))

a = math.pi * r**2
price = a*25
print(f'Por uma área de {a:,.2f} m² de jardim, você pagará R${price:,.2f} .')