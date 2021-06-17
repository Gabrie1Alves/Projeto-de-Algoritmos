class No(object):
 
    def __init__(self, valor, anterior, proximo):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo
 
 
class ListaCircularDuplamenteEncadeada(object):
 
    inicio = None
    fim = None
 
    def inserir(self, valor):

        novo_no = No(valor, None, None)


        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            
            novo_no.anterior = self.fim
            
            novo_no.proximo = self.inicio
            
            self.fim.proximo = novo_no
            
            self.fim = novo_no
            self.inicio.anterior = novo_no
              
    def busca(self, tamanhoDoArray, chave):
        #contadorDeComparacoes = 0  
        metadeDaLista = tamanhoDoArray//2  #metade da lista
        valorNaoEncontrado = 0
        
        #Setei todos os nós no inicio
        no_0Esq = self.inicio
        no_MeioEsq = self.inicio
        no_0Dir = self.inicio
        no_MeioDir = self.inicio
        
        
        
        #Setei o nó que vai trabalhar na metade do array
        for i in range(0, metadeDaLista):
            no_MeioEsq = no_MeioEsq.proximo
            #print(no_Meio.valor)
        no_MeioDir = no_MeioEsq
        
        
        #pra nao começar com o no esq e direito com o mesmo valor, eu avancei 1 dos dois, para evitar comparações iguais
        no_0Esq = no_0Esq.anterior 
        no_MeioDir = no_MeioDir.proximo
        
        
        for j in range(0, ((metadeDaLista//2)+1)):
            
            #contadorDeComparacoes = contadorDeComparacoes + 1
            if(no_0Dir.valor == chave):
                print(no_0Dir.valor, "==" ,chave)
                print("Chave encontrada na primeira metade pela direita!")
                #print("0 ->")
                #print("Numero de comparações: ", contadorDeComparacoes)
                valorNaoEncontrado = 1
                break
            elif(no_0Esq.valor == chave):
                #contadorDeComparacoes = contadorDeComparacoes + 1
                print(no_0Esq.valor, "==" ,chave)
                print("Chave encontrada na primeira metade pela esquerda!")
                #print("<- 0")
                #print("Numero de comparações: ", contadorDeComparacoes)
                valorNaoEncontrado = 1
                break
            elif(no_MeioDir.valor == chave):
                #contadorDeComparacoes = contadorDeComparacoes + 2
                print(no_MeioDir.valor, "==" ,chave)
                print("Chave encontrada na segunda metade pela direita!")
                #print(metadeDaLista ," ->")
                #print("Numero de comparações: ", contadorDeComparacoes)
                valorNaoEncontrado = 1
                break
            elif(no_MeioEsq.valor == chave):
                #contadorDeComparacoes = contadorDeComparacoes + 3
                print(no_MeioEsq.valor, "==" ,chave)
                print("Chave encontrada na segunda metade pela esquerda!")
                #print("<- ", metadeDaLista)
                #print("Numero de comparações: ", contadorDeComparacoes)
                valorNaoEncontrado = 1
                break
            #contadorDeComparacoes = contadorDeComparacoes + 3
            
            
            #apos verificar as 4 comparações, caso não encontre o resultado, move o ponteiro dos 4 nós
            no_0Dir = no_0Dir.proximo
            no_0Esq = no_0Esq.anterior
            no_MeioDir = no_MeioDir.proximo
            no_MeioEsq = no_MeioEsq.anterior

        if(valorNaoEncontrado == 0):
            print(chave, " -> Valor não encontrado!")
            #print("Numero de comparações: ", contadorDeComparacoes+1)
            
            
            
            
            
        
arranjo = [20,10,30,5,15,25,35,2,7,13,17,22,27,32,37,1,3,6,8,12,14,16,18,21,23,26,28,31,33,36,38]
lista = ListaCircularDuplamenteEncadeada()
#pega o tamanho do arranjo
tamanhoDoArray = len(arranjo)

for n in arranjo:
    lista.inserir(n)

sair = 1
while(sair != 0):
    print("\n-----------------------------------------")
    print("Digite o numero que deseja procurar:")
    Valor = int(input(" Valor -> "))
    lista.busca(tamanhoDoArray, Valor)
    
    print("\n-----------------------------------------\n")
    print("------ 0 -> Exit")
    print("------ Outro valor para sair")
    print("\n-----------------------------------------\n")
    sair = int(input(" Valor -> "))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    