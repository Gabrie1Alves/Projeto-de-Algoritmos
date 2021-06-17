class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)
    
def insere(raiz, nodo):
    """Insere um nodo em uma árvore binária de pesquisa."""
    # Nodo deve ser inserido na raiz.
    if raiz is None:
        raiz = nodo

    # Nodo deve ser inserido na subárvore direita.
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)

    # Nodo deve ser inserido na subárvore esquerda.
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)
    
def busca(raiz, chave):
    #se a chave não existir
    print("O nó existe?")
    if raiz is None:   #se a raiz não existir, a função de busca acaba, sem achar valores
        print("Não há mais valores na arvore!")
        return None
    #Se a chave que queremos for a raiz, ela será retornada na segunda verificação, no caso essa
    print(chave, " == ", raiz.chave,"?")
    if chave == raiz.chave: #se entrar nesse if, a chave foi encontrado
        return raiz
    #se a chave for maior que a raiz, ela procura em modo recursivo, até achar, pelo lado direito
    print(chave, " > ", raiz.chave,"?")
    if chave > raiz.chave:
        return busca(raiz.direita, chave)
    #se a chave for menor que a raiz, ela também vai ser procurada em modo recursivo, até ser encontrada
    #print(chave, " < ", raiz.chave,"?")
    else:
        #print(chave, " < ", raiz.chave,"?")
        return busca(raiz.esquerda, chave)






arranjo = [20,10,30,5,15,25,35,2,7,13,17,22,27,32,37,1,3,6,8,12,14,16,18,21,23,26,28,31,33,36,38]
sair = 1

#inserindo na arvore
for n in arranjo:
    if(arranjo.index(n) == 0):
        raiz = NodoArvore(n) #insere a raiz
    else:
        nodo = NodoArvore(n)
        insere(raiz, nodo)


#busca!
#coloque o valor que deseja ser procurado AQUI!!

while(sair != 0):
    print("\n\n\nDigite o valor que deseja encontrar: ")
    ValorASerProcurado = int(input(" Valor-> "))

    print("\n Comparaçoes:\n")
    resultado = busca(raiz, ValorASerProcurado)
    if resultado:
        print("Busca pela chave {}: Encontrada!".format(ValorASerProcurado))
    else:
        print("Busca pela chave {}: Falha!".format(ValorASerProcurado))
    
    print("\n\n-------------------------------------------")
    print("Digite:")
    print("----- 0 -> Exit")
    print("-----> Outro valor para repetir a operacao!")
    sair = int(input(" Valor -> "))








