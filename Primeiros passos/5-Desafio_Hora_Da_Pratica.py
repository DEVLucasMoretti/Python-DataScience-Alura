#  Vamos praticar o uso de estruturas de dados, como as listas e os dicionários, a partir de algumas atividades.

#1 Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len().
expenses = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

print(sum(expenses[:])/len(expenses)) #expenses[:] vai pegar todos os valores da lista e com a função SUM, vai somar todos esses elementos.

#2 Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
expenses = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
s = 0; c = 0
for price in expenses:
    if(price > 3000):
        s = s + price
        c = c + 1
print(f'Foram feitas {c} compras acima de R$3.000 e a porcentagem em relação ao valor total é {(s*100)/sum(expenses[:]):,.2f}%')

# 3 Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
import random
l = []
for i in range(5):
    l.append(random.randint(0,100))
print(l)

# 4 Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
import random
l = []
for i in range(5):
    l.append(random.randint(0,100))

print(f'Lista  informada: {l}')
l.reverse()
print(f'Lista invertida: {l}')

#5 Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
n = int(input("Digite um valor inteiro: "))
primos = []

for num in range(2, n + 1):  # Começa de 2, já que 1 não é primo
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primos.append(num)

print(f"Números primos entre 1 e {n}: {primos}")

########################### Momento dos projetos ###########################

#6 Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).
list_bac = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

for i in range(1,len(list_bac)):
    percent = 100 * (list_bac[i] - list_bac[i-1]) / (list_bac[i])

    print(f'Dia {i} o percentual de aumento foi de {percent}')

#7 Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.
ids= [1,43,55,34,88,77,24,34,67,79] 
p = 0; im=0

for i in range(10):
    if(ids[i] % 2 == 0):
        p = p + 1
    else:
        im = im + 1
print(f'A quantidade de números par é {p} e de números ímpares é de {im}')

#8 Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.
gabarito = ['D','A','C','B','A','D','C','C','A','B']
nota = 0
for i in range(10):
    n = input(f'Digite a resposta da questão {i+1}: ').upper()
    if(n == gabarito[i]):
        nota = nota + 1
        
print(f'A sua nota foi {nota}')

#9 Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
temp = [22,12,33,44,42,35,30,30,20,22,32,33]
mes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
temp_media = sum(temp[:])/len(temp)

for i in range(len(temp)):
    if(temp[i]> temp_media):
        print(f'({temp[i]}°C) - {mes[i]}')

#10 Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário: Escreva um código que calcule o total de vendas e o produto mais vendido.
soma = 0
sells = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
max = sells['Produto A'] #Coloquei o valor do Produto A como maximo para comparar com os demais valores e ver qual é o maior deles
max_vendas = 0
produto_mais_vendido = ""

for produto, valor in sells.items():
    soma += valor  # Soma todos os valores
    if (valor > max_vendas):
        max_vendas = valor
        produto_mais_vendido = produto  # Armazena o nome do produto mais vendido

print(f'A soma das vendas é de R${soma} e o produto mais vendido é {produto_mais_vendido} com {max_vendas} vendas.')

# 11 Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo: Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.
votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811 }
max_votos = votos['Design 1']
sum_votos= 0

for design,valor in votos.items():
    sum_votos = sum_votos + valor
    if(valor > max_votos):
        max_votos = valor
        design_win = design

print(f'O design vencedor é o {design_win} com {((max_votos*100)/sum_votos):,.2f}% dos votos.')