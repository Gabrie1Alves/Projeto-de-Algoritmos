class Huffman:
    #incicializa
    def __init__(self, caminho):
        self.caminho = caminho
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    #cria a arvore binária
    class HeapNode:
        def __init__(self, char, frequencia):
            self.char = char
            self.frequencia = frequencia
            self.esq = None
            self.dir = None

        def __lt__(self, other):
            return self.frequencia < other.frequencia

        def __eq__(self, other):
            if(other == None):
                return False
            if(not isinstance(other, self.HeapNode)):
                return False
            return self.frequencia == other.frequencia
        
        
    #Implementação das funções heappush e heappop
    #++++++++++++++++++++++++++++++++++++++
    def _siftup(self, pos):
        posFinal = len(self.heap)
        posInicial = pos
        novoItem = self.heap[pos]
        filhoEsq = 2*pos + 1 
        while filhoEsq < posFinal:
            posDir = filhoEsq + 1
            if posDir < posFinal and not self.heap[filhoEsq] < self.heap[posDir]:
                filhoEsq = posDir
            self.heap[pos] = self.heap[filhoEsq]
            pos = filhoEsq
            filhoEsq = 2*pos + 1
        self.heap[pos] = novoItem
        self._siftdown(posInicial, pos)
        
    def _siftdown(self, posInicial, pos):
        novoItem = self.heap[pos]
        while pos > posInicial:
            paiPos = (pos - 1) >> 1
            pai = self.heap[paiPos]
            if novoItem < pai:
                self.heap[pos] = pai
                pos = paiPos
                continue
            break
        self.heap[pos] = novoItem
        
    #Adiciona um elemento ao heap sem alterar o heap atual
    def heappush(self, item):
        self.heap.append(item)
        self._siftdown(0, len(self.heap)-1)
    #Retorna o maior elemento de dados da heap
    def heappop(self):
        lastelt = self.heap.pop()
        if self.heap:
            retornaItem = self.heap[0]
            self.heap[0] = lastelt
            self._siftup(0)
            return retornaItem
        return lastelt
    
    
	# Implementação das funções para compressão e descompressão
    #calcula a frequência que cada caracter aparece nos arquivo aberto em questão
    def calculaFrequencia(self, arquivoDeTexto):
        frequencia = {}
        for caracter in arquivoDeTexto:
            if not caracter in frequencia:
                frequencia[caracter] = 0
            frequencia[caracter] += 1
        return frequencia

    def fazPilha(self, frequencia):
        for busca in frequencia:
            node = self.HeapNode(busca, frequencia[busca])
            self.heappush(node)
#Cria os nós da arvore
    def fazerNos(self):
        while(len(self.heap)>1):
            no1 = self.heappop()
            no2 = self.heappop()
            junta = self.HeapNode(None, no1.frequencia + no2.frequencia)
            junta.esq = no1
            junta.dir = no2
            self.heappush(junta)
#cria o codigo binario, raiz esquerda recebe 0 e a direita recebe 1
    def make_codes_helper(self, root, codigoAtual):
        if(root == None):
            return

        if(root.char != None):
            self.codes[root.char] = codigoAtual
            self.reverse_mapping[codigoAtual] = root.char
            return

        self.make_codes_helper(root.esq, codigoAtual + "0")
        self.make_codes_helper(root.dir, codigoAtual + "1")


    def fazCod(self):
        root = self.heappop()
        codigoAtual = ""
        self.make_codes_helper(root, codigoAtual)

#codifica caracter por caracter e retorna o texto codificado
    def codificaTexto(self, arquivoDeTexto):
        textoCodificado = ""
        for caracter in arquivoDeTexto:
            textoCodificado += self.codes[caracter]
        return textoCodificado


    def codificaPad(self, textoCodificado):
        padExtra = 8 - len(textoCodificado) % 8
        for i in range(padExtra):
            textoCodificado += "0"

        padInfo = "{0:08b}".format(padExtra)
        textoCodificado = padInfo + textoCodificado
        return textoCodificado


    def obtemByte(self, codificaPadTexto):
        #se o tamanho dividido por 8 for diferente de zero o algoritmo para com o erro
        if(len(codificaPadTexto) % 8 != 0):
            print("O arquivo de texto não foi preenchido corretamente!!")
            exit(0)

        b = bytearray()
        for i in range(0, len(codificaPadTexto), 8):
            byte = codificaPadTexto[i:i+8]
            b.append(int(byte, 2))
        #retorna o tamanho em byte
        return b

#comprimi o texto e adiciona a um arquivo .dvz
    def comprimir(self, nomeDoArquivo):
        caminhoFinal = nomeDoArquivo + ".dvz"

        with open(self.caminho, 'r+') as file, open(caminhoFinal, 'wb') as resultado:
            arquivoDeTexto = file.read()
            arquivoDeTexto = arquivoDeTexto.rstrip()
            frequencia = self.calculaFrequencia(arquivoDeTexto)
            self.fazPilha(frequencia)
            self.fazerNos()
            self.fazCod()
            textoCodificado = self.codificaTexto(arquivoDeTexto)
            codificaPadTexto = self.codificaPad(textoCodificado)
            b = self.obtemByte(codificaPadTexto)
            resultado.write(bytes(b))

        print("Comprimido!")
        return caminhoFinal



#Funções para descomprimir
    def remove_padding(self, codificaPadTexto):
        padInfo = codificaPadTexto[:8]
        padExtra = int(padInfo, 2)
        codificaPadTexto = codificaPadTexto[8:] 
        textoCodificado = codificaPadTexto[:-1*padExtra]
        return textoCodificado
#decodifica o texto comprimido
    def decode_text(self, textoCodificado):
        codigoAtual = ""
        textoDecodificado = ""

        for bit in textoCodificado:
            codigoAtual += bit
            if(codigoAtual in self.reverse_mapping):
                caracter = self.reverse_mapping[codigoAtual]
                textoDecodificado += caracter
                codigoAtual = ""

        return textoDecodificado

#descomprimi o texto voltando para o .txt
    def descompressor(self, input_path, nomeDoArquivo):
        caminhoFinal = nomeDoArquivo + "_Descomprimido" + ".txt"

        with open(input_path, 'rb') as file, open(caminhoFinal, 'w') as resultado:
            bit_string = ""

            byte = file.read(1)
            while(len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            textoCodificado = self.remove_padding(bit_string)
            textoDescomp = self.decode_text(textoCodificado)
            resultado.write(textoDescomp)
        print("Descomprimido!")
        return caminhoFinal
    
    
print("\n\n\n")
##########################################################################
#comprimindo arquivo 1
caminho = "Compressor_1.txt"
#-4 por causa do ".txt"
t = len(caminho) - 4
#nome do arquivo vai receber até a posição t da string, exemplo:descompressor_1.txt -> descompressor_1
nomeDoArquivo = caminho[0:t]

h = Huffman(caminho)

caminhoFinal = h.comprimir(nomeDoArquivo)
print("Arquivo: "+caminho, "  ->  " + caminhoFinal)
print("\n")
decom_path = h.descompressor(caminhoFinal, nomeDoArquivo)
print("Arquivo: "+caminhoFinal,"  ->  " + decom_path)

print("\n +++++++++++++++++++++++++++++++\n")
##########################################################################
#comprimindo arquivo 2
caminho = "Compressor_2.txt"
t = len(caminho) - 4
nomeDoArquivo = caminho[0:t]

h = Huffman(caminho)

caminhoFinal = h.comprimir(nomeDoArquivo)
print("Arquivo: "+caminho, "  ->  " + caminhoFinal)
print("\n")
decom_path = h.descompressor(caminhoFinal, nomeDoArquivo)
print("Arquivo: "+caminhoFinal,"  ->  " + decom_path)

print("\n +++++++++++++++++++++++++++++++\n")
##########################################################################
#comprimindo arquivo 3
caminho = "Compressor_3.txt"
t = len(caminho) - 4
nomeDoArquivo = caminho[0:t]

h = Huffman(caminho)

caminhoFinal = h.comprimir(nomeDoArquivo)
print("Arquivo: "+caminho, "  ->  " + caminhoFinal)
print("\n")
decom_path = h.descompressor(caminhoFinal, nomeDoArquivo)
print("Arquivo: "+caminhoFinal,"  ->  " + decom_path)

print("\n +++++++++++++++++++++++++++++++\n")
##########################################################################
#comprimindo arquivo 4
caminho = "Compressor_4.txt"
t = len(caminho) - 4
nomeDoArquivo = caminho[0:t]

h = Huffman(caminho)

caminhoFinal = h.comprimir(nomeDoArquivo)
print("Arquivo: "+caminho, "  ->  " + caminhoFinal)
print("\n")
decom_path = h.descompressor(caminhoFinal, nomeDoArquivo)
print("Arquivo: "+caminhoFinal,"  ->  " + decom_path)

print("\n +++++++++++++++++++++++++++++++\n")
##########################################################################
#comprimindo arquivo 5
caminho = "Compressor_5.txt"
t = len(caminho) - 4
nomeDoArquivo = caminho[0:t]

h = Huffman(caminho)

caminhoFinal = h.comprimir(nomeDoArquivo)
print("Arquivo: "+caminho, "  ->  " + caminhoFinal)
print("\n")
decom_path = h.descompressor(caminhoFinal, nomeDoArquivo)
print("Arquivo: "+caminhoFinal,"  ->  " + decom_path)