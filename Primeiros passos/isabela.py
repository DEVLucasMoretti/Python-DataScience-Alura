

lista = [1,2,3,4,5]
soma = 0
tamanho = len(lista)

for i in range(tamanho):
    if(lista[i] % 2 == 0):
        soma = lista[i] + soma

print(soma)
