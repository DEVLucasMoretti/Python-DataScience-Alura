
import random

#5 Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.
#O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.
#Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).
#Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.
dia = int(input('Digite a quantidade de dias que irá viajar: '))
cidade = input('Digite a cidade desejada para a viagem (Salvador, Fortaleza, Natal ou Aracaju): ').capitalize()
autonomia_km_l = 14
diaria_hotel = 150
distancia_de_Recefife_km = [850,800,300,550]
cidades = ['Salvador', 'Fortaleza', 'Natal','Aracaju']
gasto_passeio_alimentacao= [200,400,250,300]

if (cidade == "Salvador"):
 index_cidade_escolhida = 0
elif (cidade == "Fortaleza"):
 index_cidade_escolhida = 1
elif (cidade == "Natal"):
 index_cidade_escolhida = 2
elif (cidade == "Aracaju"):
 index_cidade_escolhida = 3

def gasto_hotel(dia):
    return dia * diaria_hotel

def gasto_gasolina(lista_km,index):
  return (lista_km[index]/14) * 5

def gasto_passeio(lista_passeio,dia,index):
  return dia * lista_passeio[index]

gasto_total = gasto_hotel(dia) + gasto_gasolina(distancia_de_Recefife_km,index_cidade_escolhida) + gasto_passeio(gasto_passeio_alimentacao,dia,index_cidade_escolhida)

print(f'Com base nos gastos definidos, uma viagem de {dia} dias para {cidade} saindo de Recife custaria {gasto_total:,.2f} reais')

