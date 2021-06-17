graph = {
    'S' : ['W','R'],
    'W' : ['T','X'],
    'R' : ['V'],
    'T' : ['U'],
    'X' : ['Y'],
    'V' : [],
    'U' : [],
    'Y' : []
    }

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node, busca):
    visited.append(node)
    queue.append(node)
    pai = 0
    filho = 1
    tamV = 0
    saida = 0
    pares=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    linha = 6
    distancia=0
    
    while queue:
        if(saida == 1):
            break
        s = queue.pop(0)

        #print(s)
        if(s == busca):
            if(busca == 'S'):
                print("NULL é pai de: S")
                print("Distância: 0")
            #print( visited)
            #print("Valor encontrado!")
                
            return 0


        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)

                queue.append(neighbour)
        
        tamV = len(visited)
        for i in range(2):
            if(tamV > filho):
                #print(visited[pai], "é pai de:", visited[filho])
                pares[linha][0] = visited[pai]
                pares[linha][1] = visited[filho]
                linha-=1
                if(busca == visited[filho]):
                    #print(visited[pai], "é pai de:", visited[filho])
                    print("O pai de", visited[filho], "é:", visited[pai])
                    saida = 1
                    break
                filho+=1
        pai+=1
        
    print("\n Matriz -> pai,filho:")
    print(" ", pares)
    if(saida != 1):
        return 0
    valor = busca
    for i in range(7):
        if(pares[i][1] == valor):
            distancia+=1
            valor = pares[i][0]
    print("A distancia de", busca,"é:", distancia)
    


busca = (input(" Valor que deseja procurar -> "))
busca = busca.upper()
bfs(visited, graph, 'S', busca)