# n is size of heap 
def heapify(arranjo, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arranjo[i] < arranjo[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arranjo[largest] < arranjo[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arranjo[i],arranjo[largest] = arranjo[largest],arranjo[i]  # swap 
  
        # Heapify the root. 
        heapify(arranjo, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arranjo): 
    n = len(arranjo) 
  
    # Build a maxheap. 
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arranjo, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arranjo[i], arranjo[0] = arranjo[0], arranjo[i]   # swap 
        heapify(arranjo, i, 0) 
        
        
        
def busca(lista, chave):
    esquerda = 0
    direita = len(lista) -1
    encontrado = False
    
    while(esquerda <= direita and not encontrado):
        #print("Comparações: +1")
        meio = (esquerda + direita) // 2
        #print("Comparações: +1")
        if(lista[meio] == chave):
            print("Valor na lista:", lista[meio], "==", chave, "chave?")
            print("A chave:", chave, "FOI encontrada na posicao:" ,meio)
            encontrado = True
        else:
            if(chave < lista[meio]):
                #print("Comparações: +1")
                print("Valor na lista:", lista[meio], "==", chave, "chave?")
                #print("A chave esta entre as posicoes:", esquerda, "e", direita)
                direita = meio - 1
            else:
                #print("A chave esta entre as posicoes:", esquerda, "e", direita)
                print("Valor na lista:", lista[meio], "==", chave, "chave?")
                esquerda = meio + 1
                
    #print("Comparações: +1")
    if(encontrado == False):
        print("A chave:", chave, "NAO foi encontrada!!")
        
    
        
arranjo = [20,10,30,5,15,25,35,2,7,13,17,22,27,32,37,1,3,6,8,12,14,16,18,21,23,26,28,31,33,36,38]
heapSort(arranjo) 
n = len(arranjo) 


sair = 5
escolha = 0
while(sair != 0):
    #print("\n\n-----------------------------------------------------")
    print("Escolha a operação desejada: ")
    print("---- 1 -> Ver o array ordenado com o heapsort")
    print("---- 2 -> Buscar valor com a funcao Busca")
    #print("---------------------------------------------------------\n")
    escolha = int(input(" Informe a operacao -> "))
    if(escolha == 1):
        for i in range(n):
            print("", arranjo[i], end="  ")
    elif(escolha == 2):
        #print("---------------------------------------------------------")
        chave =int(input(" Informe o valor que deseja buscar -> "))
        #print("---------------------------------------------------------\n\n")
        comparacao = busca(arranjo, chave)
    else:
        print("Escolha invalida!")
    print("\n---------------------------------------------------------")
    print("Deseja continuar?")
    print("-- 0 -> Nao")
    print("-- Outro valor para continuar")
    print("---------------------------------------------------------\n")
    
    sair = int(input(" Informe o valor -> "))












