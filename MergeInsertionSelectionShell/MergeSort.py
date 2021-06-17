import time

def MergeSort(minhaLista):
    if len(minhaLista) > 1:
        meio = len(minhaLista) // 2
        esq = minhaLista[:meio]
        dir = minhaLista[meio:]

        #chamada recursiva em cada metade
        MergeSort(esq)
        MergeSort(dir)

        # variavreis para percorrer as duas metades
        i = 0
        j = 0
        
        # variavel para percorrer a lista principal
        k = 0
        
        while i < len(esq) and j < len(dir):
            if esq[i] < dir[j]:
              # lista principal recebe o valor de esq na posição i
              minhaLista[k] = esq[i]
              # acrescenta variavel que percorre a metade da esquerda
              i += 1
            else:
                minhaLista[k] = dir[j]
                j += 1
            # acrescenta variavel que percorre a lista principal
            k += 1

        while i < len(esq):
            minhaLista[k] = esq[i]
            i += 1
            k += 1

        while j < len(dir):
            minhaLista[k]=dir[j]
            j += 1
            k += 1

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
MergeSort(entrada1)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada1)
print("\n->> MergeSort 10 valores:\n")
print("\n  ->tempo: ", t)


#=====================================================================
#pega a entrada com 1000 numeros!!        
entrada2 = []
valores = open("entrada1000.txt", "r")

for linha in valores:
    entrada2.append(int(linha))
valores.close()
ini = time.time()
MergeSort(entrada2)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada2)
print("\n->> MergeSort 1000 valores:\n")
print("\n  ->tempo: ", t)

#=====================================================================
#pega a entrada com 10000 numeros!!        
entrada3 = []
valores = open("entrada10000.txt", "r")

for linha in valores:
    entrada3.append(int(linha))
valores.close()
ini = time.time()
MergeSort(entrada3)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada3)
print("\n->> MergeSort 10000 valores:\n")
print("\n  ->tempo: ", t)

#=====================================================================
#pega a entrada com 100000 numeros!!        
entrada4 = []
valores = open("entrada100000.txt", "r")

for linha in valores:
    entrada4.append(int(linha))
valores.close()
ini = time.time()
MergeSort(entrada4)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada4)
print("\n->> MergeSort 100000 valores:\n")
print("\n  ->tempo: ", t)

#=======================================================================
#pega a entrada com 1000000 numeros!!        
entrada5 = []
valores = open("entrada1000000.txt", "r")

for linha in valores:
    entrada5.append(int(linha))

ini = time.time()
MergeSort(entrada5)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada5)
print("\n->> MergeSort 1000000 valores:\n")
print("\n  ->tempo: ", t)


#Todos os array já foram ordenados nos codigos acima, logo não precisarei fazer alterações nos mesmos

print("=====================================================================\n")
print("               ELEMENTOS EM ORDEM CRESCENTE!!!!!!\n")


ini = time.time()
MergeSort(entrada1)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada1)
print("\n->> MergeSort 10 valores:")
print("\n  ->tempo: ", t)


ini = time.time()
MergeSort(entrada2)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada2)
print("\n->> MergeSort 1000 valores:")
print("\n  ->tempo: ", t)


ini = time.time()
MergeSort(entrada3)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada3)
print("\n->> MergeSort 10000 valores:")
print("\n  ->tempo: ", t)

ini = time.time()
MergeSort(entrada4)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada4)
print("\n->> MergeSort 100000 valores:")
print("\n  ->tempo: ", t)


ini = time.time()
MergeSort(entrada5)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada5)
print("\n->> MergeSort 1000000 valores:")
print("\n  ->tempo: ", t)


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
entrada5.reverse()
#print(entrada4)

ini = time.time()
MergeSort(entrada1)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada1)
print("\n->> MergeSort 10 valores:")
print("\n  ->tempo: ", t)


ini = time.time()
MergeSort(entrada2)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada2)
print("\n->> MergeSort 1000 valores:")
print("\n  ->tempo: ", t)


ini = time.time()
MergeSort(entrada3)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada3)
print("\n->> MergeSort 10000 valores:")
print("\n  ->tempo: ", t)

ini = time.time()
MergeSort(entrada4)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada4)
print("\n->> MergeSort 100000 valores:")
print("\n  ->tempo: ", t)


ini = time.time()
MergeSort(entrada5)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada5)
print("\n->> MergeSort 1000000 valores:")
print("\n  ->tempo: ", t)