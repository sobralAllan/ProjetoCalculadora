vetor = []

def preencherVetor():
    for i in range(101):
        vetor.append(i+1) #append = adicionar elementos dentro do vetor
def mostrarVetor():
    preencherVetor()
    for i in range(101):
        print(vetor[i])