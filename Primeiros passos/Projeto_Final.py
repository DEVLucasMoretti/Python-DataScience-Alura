
votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811 }
max_votos = votos['Design 1']
sum_votos= 0

for design,valor in votos.items():
    sum_votos = sum_votos + valor
    if(valor > max_votos):
        max_votos = valor
        design_win = design

print(f'O design vencedor é o {design_win} com {((max_votos*100)/sum_votos):,.2f}% dos votos.')







#for produto, valor in sells.items():