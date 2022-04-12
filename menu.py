import soma,subtracao,multiplicacao,divisao,this, tabuada, vetores

this.opcao = 0 #Criar a variavel global
num1 = 0
num2 = 0

def coletarNum1():
    print("Informe o 1° número: ")
    this.num1 = float(input())

def coletarNum2():
    print("Informe o 2° número: ")
    this.num2 = float(input())

def mostrarMenu():
    print("Escolha uma das Opções Abaixo!\n " +
          "\n1. Soma" +
          "\n2. Subtração" +
          "\n3. Multiplicação" +
          "\n4. Divisão" +
          "\n5. Tabuada" +
          "\n6. Vetor" +
          "\n7. Sair")
    this.opcao = int(input()) #Comando para coletar oq o usuario irá digitar

def operacao():
    #Mostrar o Menu em tela
    while this.opcao != 5:
        mostrarMenu()
        #Realizar as operções
        if this.opcao == 1: #Operação para somar(Opção 1)
            coletarNum1()
            coletarNum2()
            print(soma.somar(this.num1, this.num2))
        elif this.opcao == 2:#Opção para subtração(Opção 2)
            coletarNum1()
            coletarNum2()
            print(subtracao.subitrair(this.num1, this.num2))
        elif this.opcao == 3: #Opção para multiplicação(Opção 3)
            coletarNum1()
            coletarNum2()
            print(multiplicacao.multiplicar(this.num1, this.num2))
        elif this.opcao == 4: #Opção para Divisão(Opção 4)
            coletarNum1()
            coletarNum2()
            print(divisao.dividir(this.num1, this.num2))
        elif this.opcao == 5:
            coletarNum1()
            coletarNum2()
            print(tabuada.calculcarTabuada(int(this.num1), int(this.num2)))
        elif this.opcao == 6:
            vetores.mostrarVetor()
        elif this.opcao == 7:
            print("Obrigado!")
        else: print("Opção Escolhida Inválida, tente outro número!")
