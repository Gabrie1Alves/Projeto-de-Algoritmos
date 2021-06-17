import time

def selectionSort(entrada):
    #percorre todos os elementos
    for i in range(len(entrada)):
        #Encontra o menor elemento
        minimo = i
        #i + 1 para nao comparar com o valor minimo da linha anterior e não comparar com os elementos que já foram trocados de posicao
        for num in range(i+1, len(entrada)):
            if entrada[minimo] > entrada[num]:
                #se o valor que setamos (minimo = i (por exemplo)) for maior que o valor da posicao atual
                #a variavel minimo recebe esse valor
                minimo = num
        #troca o menor elemento encontrado pelo primeiro
        entrada[i], entrada[minimo] = entrada[minimo], entrada[i]
                    
        
print("=====================================================================\n")
print("               ELEMENTOS EM ORDEM ALEATORIA!!!!!!\n")
#=====================================================================
#pega a entrada com 10 numeros!!        
entrada1 = []
valores = open("entrada10.txt", "r")

for line in valores:
    entrada1.append(int(line))
valores.close()
ini = time.time()
selectionSort(entrada1)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada1)
print("\n->> Selection sort 10 valores:\n")
print("\n  ->tempo: ", t)

#=====================================================================
#pega a entrada com 1000 numeros!!        
entrada2 = []
valores = open("entrada1000.txt", "r")

for line in valores:
    entrada2.append(int(line))
valores.close()
ini = time.time()
selectionSort(entrada2)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada2)
print("\n->> Selection sort 1000 valores:\n")
print("\n  ->tempo: ", t)

#=====================================================================
#pega a entrada com 10000 numeros!!        
entrada3 = []
valores = open("entrada10000.txt", "r")

for line in valores:
    entrada3.append(int(line))
valores.close()
ini = time.time()
selectionSort(entrada3)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada3)
print("\n->> Selection sort 10000 valores:\n")
print("\n  ->tempo: ", t)

#=====================================================================
#pega a entrada com 100000 numeros!!        
entrada4 = []
valores = open("entrada100000.txt", "r")

for line in valores:
    entrada4.append(int(line))
valores.close()
ini = time.time()
selectionSort(entrada4)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada4)
print("\n->> Selection sort 100000 valores:\n")
print("\n  ->tempo: ", t)
'''
#=======================================================================
#pega a entrada com 1000000 numeros!!        
entrada5 = []
valores = open("entrada1000000.txt", "r")

for line in valores:
    entrada5.append(int(line))
valores.close()
ini = time.time()
selectionSort(entrada5)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada5)
print("\n->> Selection sort 1000000 valores:\n")
print("\n  ->tempo: ", t)

#Todos os array já foram ordenados nos codigos acima, logo não precisarei fazer alterações nos mesmos
'''
print("=====================================================================\n")
print("               ELEMENTOS EM ORDEM CRESCENTE!!!!!!\n")

ini = time.time()
selectionSort(entrada1)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada1)
print("\n->> Selection sort 10 valores:\n")
print("\n  ->tempo: ", t)


ini = time.time()
selectionSort(entrada2)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada2)
print("\n->> Selection sort 1000 valores:\n")
print("\n  ->tempo: ", t)


ini = time.time()
selectionSort(entrada3)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada3)
print("\n->> Selection sort 10000 valores:\n")
print("\n  ->tempo: ", t)


ini = time.time()
selectionSort(entrada4)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada4)
print("\n->> Selection sort 100000 valores:\n")
print("\n  ->tempo: ", t)

'''
ini = time.time()
selectionSort(entrada5)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada5)
print("\n->> Selection sort 1000000 valores:\n")
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
selectionSort(entrada1)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada1)
print("\n->> Selection sort 10 valores:\n")
print("\n  ->tempo: ", t)


ini = time.time()
selectionSort(entrada2)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada2)
print("\n->> Selection sort 1000 valores:\n")
print("\n  ->tempo: ", t)


ini = time.time()
selectionSort(entrada3)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada3)
print("\n->> Selection sort 10000 valores:\n")
print("\n  ->tempo: ", t)


ini = time.time()
selectionSort(entrada4)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada4)
print("\n->> Selection sort 100000 valores:\n")
print("\n  ->tempo: ", t)

'''
ini = time.time()
selectionSort(entrada5)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada5)
print("\n->> Selection sort 1000000 valores:\n")
print("\n  ->tempo: ", t)
'''