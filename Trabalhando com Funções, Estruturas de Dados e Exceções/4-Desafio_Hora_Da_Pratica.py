#5 Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste. Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.
gabarito = ['D', 'A', 'B', 'C', 'A']

# Gabarito da prova
gabarito = ['D', 'A', 'B', 'C', 'A']

# Listas de respostas dos estudantes
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], 
                  ['C', 'A', 'A', 'C', 'A'], 
                  ['D', 'B', 'A', 'C', 'A']]

testes_com_ex = [['D', 'A', 'B', 'C', 'A'], 
                  ['C', 'A', 'A', 'E', 'A'], 
                  ['D', 'B', 'A', 'C', 'A']]

# Função para calcular as notas
def calcular_notas(testes):
    notas = []
    for resposta in testes:
        # Verificar se todas as alternativas são válidas
        for alternativa in resposta:
            if alternativa not in ['A', 'B', 'C', 'D']:
                raise ValueError(f"A alternativa {alternativa} não é uma opção de alternativa válida")
        
        # Calcular a nota
        nota = sum(1 for i in range(len(gabarito)) if resposta[i] == gabarito[i])
        notas.append(nota)
    
    return notas

# Testando sem exceção
try:
    notas_sem_ex = calcular_notas(testes_sem_ex)
    print("Notas sem exceção:", notas_sem_ex)
except ValueError as e:
    print(e)

# Testando com exceção
try:
    notas_com_ex = calcular_notas(testes_com_ex)
    print("Notas com exceção:", notas_com_ex)
except ValueError as e:
    print(e)
