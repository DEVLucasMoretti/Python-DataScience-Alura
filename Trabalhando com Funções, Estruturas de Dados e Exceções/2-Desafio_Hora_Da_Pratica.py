import random
#1 Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.
#Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:
#"Nota da manobra: [media]"

points_skate = []

for i in range(5):
    points_skate.append(random.randint(5,10))   # Notas variadas dos jurados

def avg_points(points_skate):
    max_point = 0
    min_point = 11
    for value in points_skate:  #Verificamos qual o menor e maior valor
        if(value > max_point):
            max_point = value
        if(value < min_point):
            min_point = value

    points_skate.remove(max_point) #removemos o maior valor
    points_skate.remove(min_point) #removemos o menor valor

    return (points_skate[0] + points_skate[1] + points_skate[2])/3 #cáculo da média

media = avg_points(points_skate) # media recebe o cálculo da média das notas

print(f"Nota da manobra: {media:,.2f}")

#2 Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:
#maior nota, menor nota ,média , situação (Aprovado(a) ou Reprovado(a))
#Para testar o comportamento da função, os dados podem ser exibidos em um texto: 
grade=[]
for i in range(4):
    grade.append(random.randint(0,10))

def performance(grade):
    max_point = 0
    min_point = 11
    for value in grade:  #Verificamos qual o menor e maior valor
        if(value > max_point):
            max_point = value
        if(value < min_point):
            min_point = value
    avg = ((grade[0] + grade[1] + grade[2]+ grade[3])/4)

    status = "Aprovado(a)" if avg >=6 else "Reprovado(a)" #If ternário
    return f"O(a) estudante obteve uma média de {avg}, com a sua maior nota de {max_point} pontos e a menor nota de {min_point} pontos e foi {status}"

print(performance(grade))

#3 Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]
nome_completo = []
# Usando zip para combinar os nomes e sobrenomes
for nome, sobrenome in zip(nomes, sobrenomes):
    # Concatenando nome e sobrenome e formatando
    nome_completo.append(f"{nome.title()} {sobrenome.title()}")

print(nome_completo)

#4 Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.
#Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.
#Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.
#Para teste, utilize as seguintes listas de gols marcados e sofridos:

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

#vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.
def calcula_pontos(lista1,lista2):
    soma = 0
    for i in range(5):
        if lista1[i] > lista2[i]:
            soma = soma + 3
        elif lista1[i] == lista2[i]:
            soma = soma + 1
    print(f'A pontuação do time foi de {soma} pontos e seu aproveitamento foi de {soma*100/30:,.2f}%')

calcula_pontos(gols_marcados,gols_sofridos)