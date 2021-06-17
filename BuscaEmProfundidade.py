grafo = {
    'S' : ['W','R'],
    'W' : ['T','X'],
    'R' : ['V'],
    'T' : ['U'],
    'X' : ['Y'],
    'V' : [],
    'U' : [],
    'Y' : []
    }

def dfs(grafo, inicio, busca):
       path = []
       stack = [inicio]
       tempo = 0
       while(len(stack) != 0):
           tempo = tempo+1
           s = stack.pop()

           if s not in path:

               path.append(s)

           if s not in grafo:

               #leaf node
               continue
           if s == busca:
               print("Tempo:", tempo)
               print("Tempo Final:", tempo+1)
               return " ".join(path)
           for neighbor in grafo[s]:

               stack.append(neighbor)
       if(s == busca):
           return " ".join(path)
       else:
           print("Elemento não encontrado no grafo!!")
           print("Tempo:", tempo)
           return " ".join(path)

       
   
    
busca = (input(" Valor que deseja procurar -> "))
busca = busca.upper()
caminho = dfs(grafo, "S", busca)

print("Caminho:",caminho)