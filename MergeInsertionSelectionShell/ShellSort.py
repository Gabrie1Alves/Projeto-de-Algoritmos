import time

def ShellSort(entrada, tamanhoEntrada):
  
    #divide o tamnho do vetor entrada no meio (pega só a parte inteira)
    metade = tamanhoEntrada//2
  
    #enquanto a metade for maisor que 0 o loop continua
    while metade > 0:
  
        for i in range(metade,tamanhoEntrada):
  
            # auxiliar vai armazenar o valor do vetor entrada na posicao i
            auxiliar = entrada[i]
  
            # a variavel posicao vai guardar a posicao do contador i
            posicao = i
            while  posicao >= metade and entrada[posicao-metade] >auxiliar:
                entrada[posicao] = entrada[posicao-metade]
                posicao = posicao - metade
  
            #quando acabar o loop, o vetor entrada na posicao 'posicao', vai receber o valor de 'auxiliar'
            entrada[posicao] = auxiliar
        #metade vai ser dividido por 2 novamente
        metade = metade // 2

print("=====================================================================\n")
print("               ELEMENTOS EM ORDEM ALEATORIA!!!!!!\n")
#=====================================================================
#pega a entrada com 10 numeros!!        
entrada1 = []
valores = open("entrada10.txt", "r")

for line in valores:
    entrada1.append(int(line))
tam = len(entrada1)
valores.close()
ini = time.time()
ShellSort(entrada1, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada1)
print("\n->> ShellSort 10 valores:")
print("\n  ->tempo: ", t)

#=====================================================================
#pega a entrada com 1000 numeros!!        
entrada2 = []
valores = open("entrada1000.txt", "r")

for line in valores:
    entrada2.append(int(line))
tam = len(entrada2)
valores.close()
ini = time.time()
ShellSort(entrada2, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada2)
print("\n->> ShellSort 1000 valores:")
print("\n  ->tempo: ", t)

#=====================================================================
#pega a entrada com 10000 numeros!!        
entrada3 = []
valores = open("entrada10000.txt", "r")

for line in valores:
    entrada3.append(int(line))
tam = len(entrada3)
valores.close()
ini = time.time()
ShellSort(entrada3, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada3)
print("\n->> ShellSort 10000 valores:")
print("\n  ->tempo: ", t)

#=====================================================================
#pega a entrada com 100000 numeros!!        
entrada4 = []
valores = open("entrada100000.txt", "r")

for line in valores:
    entrada4.append(int(line))
tam = len(entrada4)
valores.close()
ini = time.time()
ShellSort(entrada4, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada4)
print("\n->> ShellSort 100000 valores:")
print("\n  ->tempo: ", t)

#=======================================================================
#pega a entrada com 1000000 numeros!!        
entrada5 = []
valores = open("entrada1000000.txt", "r")

for line in valores:
    entrada5.append(int(line))
tam = len(entrada5)
valores.close()
ini = time.time()
ShellSort(entrada5, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada5)
print("\n->> ShellSort 1000000 valores:")
print("\n  ->tempo: ", t)

#Todos os array já foram ordenados nos codigos acima, logo não precisarei fazer alterações nos mesmos

print("=====================================================================\n")
print("               ELEMENTOS EM ORDEM CRESCENTE!!!!!!\n")

tam = len(entrada1)
ini = time.time()
ShellSort(entrada1, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada1)
print("\n->> ShellSort 10 valores:")
print("\n  ->tempo: ", t)

tam = len(entrada2)
ini = time.time()
ShellSort(entrada2, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada2)
print("\n->> ShellSort 1000 valores:")
print("\n  ->tempo: ", t)

tam = len(entrada3)
ini = time.time()
ShellSort(entrada3, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada3)
print("\n->> ShellSort 10000 valores:")
print("\n  ->tempo: ", t)

tam = len(entrada4)
ini = time.time()
ShellSort(entrada4, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada4)
print("\n->> ShellSort 100000 valores:")
print("\n  ->tempo: ", t)

tam = len(entrada5)
ini = time.time()
ShellSort(entrada5, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada5)
print("\n->> ShellSort 1000000 valores:")
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

tam = len(entrada1)
ini = time.time()
ShellSort(entrada1, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada1)
print("\n->> ShellSort 10 valores:")
print("\n  ->tempo: ", t)

tam = len(entrada2)
ini = time.time()
ShellSort(entrada2, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada2)
print("\n->> ShellSort 1000 valores:")
print("\n  ->tempo: ", t)

tam = len(entrada3)
ini = time.time()
ShellSort(entrada3, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada3)
print("\n->> ShellSort 10000 valores:")
print("\n  ->tempo: ", t)

tam = len(entrada4)
ini = time.time()
ShellSort(entrada4, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada4)
print("\n->> ShellSort 100000 valores:")
print("\n  ->tempo: ", t)

tam = len(entrada5)
ini = time.time()
ShellSort(entrada5, tam)
fim = time.time()
t = fim-ini
#print("Entrada ordenada: ", entrada5)
print("\n->> ShellSort 1000000 valores:")
print("\n  ->tempo: ", t)