import time

def InsertionSort(entrada):

    # percorre todos os elementos
    f = len(entrada)
    for index in range(1, f):
        valorAtual = entrada[index]
        posicaoAtual = index

        #Enquanto a posicao atual for maior que 0 e o valor do array nessa posicao for maior que o valor atual, o loop vai continuar
        while posicaoAtual > 0 and entrada[posicaoAtual - 1] > valorAtual:
            #o vetor 'entrada' vai receber o valor predecedor do atual
            entrada[posicaoAtual] = entrada[posicaoAtual -1]
            #posicao atual vai decrementando até chegar em 0(ou até o valor do array ser maior que o valor atual)
            posicaoAtual = posicaoAtual - 1
       #o valor atual é inserido na posicao atual do array         
        entrada[posicaoAtual] = valorAtual

print("=====================================================================\n")
print("               ELEMENTOS EM ORDEM ALEATORIA!!!!!!\n")        
#=====================================================================
#pega a entrada com 10 numeros!!        
entrada1 = []
valores = open("entrada10.txt", "r")

for linha in valores:
    entrada1.append(int(linha))

valores.close()
ini = time.time()
InsertionSort(entrada1)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada1)
print("\n->> InsertionSort 10 valores:")
print("\n  ->tempo: ", t)

#=====================================================================
#pega a entrada com 1000 numeros!!        
entrada2 = []
valores = open("entrada1000.txt", "r")

for linha in valores:
    entrada2.append(int(linha))
valores.close()
ini = time.time()
InsertionSort(entrada2)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada2)
print("\n->> InsertionSort 1000 valores:")
print("\n  ->tempo: ", t)

#=====================================================================
#pega a entrada com 10000 numeros!!        
entrada3 = []
valores = open("entrada10000.txt", "r")

for linha in valores:
    entrada3.append(int(linha))
valores.close()
ini = time.time()
InsertionSort(entrada3)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada3)
print("\n->> InsertionSort 10000 valores:")
print("\n  ->tempo: ", t)

#=====================================================================
#pega a entrada com 100000 numeros!!        
entrada4 = []
valores = open("entrada100000.txt", "r")

for linha in valores:
    entrada4.append(int(linha))
valores.close()
ini = time.time()
InsertionSort(entrada4)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada4)
print("\n->> InsertionSort 100000 valores:")
print("\n  ->tempo: ", t)
'''
#=======================================================================
#pega a entrada com 1000000 numeros!!        
entrada5 = []
valores = open("entrada1000000.txt", "r")

for linha in valores:
    entrada5.append(int(linha))
valores.close()
ini = time.time()
InsertionSort(entrada5)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada5)
print("\n->> InsertionSort 1000000 valores:")
print("\n  ->tempo: ", t)

'''
#Todos os array já foram ordenados nos codigos acima, logo não precisarei fazer alterações nos mesmos

print("=====================================================================\n")
print("               ELEMENTOS EM ORDEM CRESCENTE!!!!!!\n")


ini = time.time()
InsertionSort(entrada1)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada1)
print("\n->> InsertionSort 10 valores:")
print("\n  ->tempo: ", t)


ini = time.time()
InsertionSort(entrada2)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada2)
print("\n->> InsertionSort 1000 valores:")
print("\n  ->tempo: ", t)


ini = time.time()
InsertionSort(entrada3)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada3)
print("\n->> InsertionSort 10000 valores:")
print("\n  ->tempo: ", t)

ini = time.time()
InsertionSort(entrada4)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada4)
print("\n->> InsertionSort 100000 valores:")
print("\n  ->tempo: ", t)

'''
ini = time.time()
InsertionSort(entrada5)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada5)
print("\n->> InsertionSort 1000000 valores:")
print("\n  ->tempo: ", t)
'''
print("=====================================================================\n")
print("               ELEMENTOS EM ORDEM DECRESCENTE!!!!!!\n")

#invertendo a ordem da lista
entrada1.reverse()
#print(entrada1)
entrada2.reverse()
#print(entrada2)
entrada3.reverse()
#print(entrada3)
entrada4.reverse()
#print(entrada4)
'''
entrada5.reverse()
#print(entrada4)
'''
ini = time.time()
InsertionSort(entrada1)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada1)
print("\n->> InsertionSort 10 valores:")
print("\n  ->tempo: ", t)


ini = time.time()
InsertionSort(entrada2)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada2)
print("\n->> InsertionSort 1000 valores:")
print("\n  ->tempo: ", t)


ini = time.time()
InsertionSort(entrada3)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada3)
print("\n->> InsertionSort 10000 valores:")
print("\n  ->tempo: ", t)

ini = time.time()
InsertionSort(entrada4)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada4)
print("\n->> InsertionSort 100000 valores:")
print("\n  ->tempo: ", t)

'''
ini = time.time()
InsertionSort(entrada5)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada5)
print("\n->> InsertionSort 1000000 valores:")
print("\n  ->tempo: ", t)
'''