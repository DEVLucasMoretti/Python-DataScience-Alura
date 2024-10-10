#Vamos praticar o uso da função (print) com algumas atividades.

#1 mprima a frase Escola de Dados da Alura!.
print("Escola de Dados da Alura!\n")

#2 Imprima seu nome e seu sobrenome
print("Nome: Lucas\nSobrenome: Moretti\n")

#3 mprima o seu primeiro nome letra a letra. Por exemplo, meu nome é Mirla, então eu obtenho a seguinte saída:
name = "LUCAS\n"

for i in range(6):
    print((name[i]))

#4 Imprima o dia do seu nascimento em formato dia mês ano. Lembrando que os valores de dia e ano não podem estar entre aspas. Supondo uma data de aniversário.
dia = 28
mes = "Fevereiro"
ano = 2003

print(dia, mes, ano,'\n')

#5 mprima, em um único print, o atual ano que você está fazendo esse curso. O valor do ano deve ser um dado numérico e a saída do print deve ser a seguinte: Ano atual: [ano]
ano = 2024
print(f'Ano Atual: {ano}\n')
