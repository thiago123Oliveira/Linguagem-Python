__author__ = 'Thiago'


#///Função que conta números de preposição

def quantidadePreposições(lista):
    letrasTipoFatec='ftsjc'
    quantidade=0
    for preposições in lista:
        if len(preposições)%2==0 and 'x' not in preposições and preposições[(len(preposições)-1)] not in letrasTipoFatec:
            quantidade+=1
    return quantidade


#///Função que conta os verbos e os verbos em 1º Pessoa

def quantidadeVerbos(lista):
    letrasTipoFatec='ftsjc'
    quantidadeVerbo=0
    verbo1pessoa=0
    for verbo in lista:
        if len(verbo)==5 and verbo[0] not in letrasTipoFatec:
            quantidadeVerbo+=1
            if verbo[(len(verbo)-1)] in letrasTipoFatec:
                verbo1pessoa+=1
    return quantidadeVerbo,verbo1pessoa


#Função que remove palavras repetidas da lista

def palavraRepetida(lista):
    contador=0
    while contador <= (len(lista)-1):
        if lista.count(lista[contador]) != 1:
            lista.remove(lista[contador])
            contador=0
        else:
            contador+=1
    return lista


#/// Função que ordena as palavras de acordo com o alfabeto googlon

def alfabetoGooglon(lista):
    listaSemPalavrasRepetidas = palavraRepetida(lista)
    alfabeto_Googlon = "tshjmpnzwlrcbxkqvdgf"
    contador = 0
    começamComMesmaLetra = []
    listaOrdenada = []
    while True:
        if len(alfabeto_Googlon) <= contador:
            break
        for primeiraVerificação in listaSemPalavrasRepetidas:
            if primeiraVerificação[0] == alfabeto_Googlon[contador]:
                começamComMesmaLetra.append(primeiraVerificação)
        if len(começamComMesmaLetra) == 1:
            listaOrdenada.append(começamComMesmaLetra[0])
            começamComMesmaLetra.clear()
        if len(começamComMesmaLetra) > 1:
            vaiPraOutraFunção = ordenarPalavrasPrimeiraLetraIgual(começamComMesmaLetra, alfabeto_Googlon)
            listaOrdenada.extend(vaiPraOutraFunção)
        contador+=1
    return listaOrdenada


#função para ordenar palavras que começam com a mesma letra


def ordenarPalavrasPrimeiraLetraIgual(listaComeçaComMesmLetra, modeloAlfabeto):
    contador = 1
    indiceAlfabeto = 0
    testaDeNovo = []
    voltaPraFunção = []
    while True:
        if len(listaComeçaComMesmLetra) <= 0:
            break
        for segundaVerificação in listaComeçaComMesmLetra:
            if len(segundaVerificação) <= contador:
                voltaPraFunção.append(segundaVerificação)
                listaComeçaComMesmLetra.remove(segundaVerificação)
            else:
                if segundaVerificação[contador] == modeloAlfabeto[indiceAlfabeto]:
                    testaDeNovo.append(segundaVerificação)
        if len(testaDeNovo) == 1:
            voltaPraFunção.append(testaDeNovo[0])
            listaComeçaComMesmLetra.remove(testaDeNovo[0])
            testaDeNovo.clear()
            indiceAlfabeto = 0
        elif len(testaDeNovo) > 1:
            testaDeNovo.clear()
            indiceAlfabeto = 0
            contador+=1
        else:
            indiceAlfabeto+=1
    return voltaPraFunção


#///Função que faz a conversão de números Googlon

def conversãoNumerosGooglon(lista):
    alfabetoDicionario = {'t':0,'s':1,'h':2,'j':3,'m':4,'p':5,'n':6,'z':7,'w':8,'l':9,'r':10,'c':11,'b':12,'x':13,'k':14,'q':15,'v':16,'d':17,'g':18,'f':19}
    listaNumeros = []
    for palavras in lista:
        conversãoBase20 = 0
        contador = 0
        for numeros in palavras:
            conversãoBase20+=(alfabetoDicionario[numeros]*(20**contador))
            contador+=1
        listaNumeros.append(conversãoBase20)
    return listaNumeros

#///Função que verifica se é um número bonito

def numeroBonito(ListaNumeros):
    listaNumeroBonito = []
    for verificaNumerosBonito in ListaNumeros:
        numeroRepetido = 0
        soma = 0
        for teste in str(verificaNumerosBonito):
            soma += int(teste)
            teste2 = dentro(str(verificaNumerosBonito),teste)
            if teste2 == False:
                numeroRepetido+=1
        if numeroRepetido == 0 and soma%2 == 0:
            listaNumeroBonito.append(verificaNumerosBonito)
    return len(listaNumeroBonito)


#Função que verifica se tem numero repetido

def dentro(lista,x):
    contador=0
    verificador=0
    while contador < len(lista):
        if lista[contador]==x:
            verificador+=1
        contador+=1
    if verificador == 1:
        return True
    else:
        return False


#Entrada

file=open('txtB.txt', 'r')
arquivoTxtB=file.readline().rstrip().split(' ')
file.close()

preposições = quantidadePreposições(arquivoTxtB)
verbo = quantidadeVerbos(arquivoTxtB)
ordenação = alfabetoGooglon(arquivoTxtB)
resultadoNumeroBonito = numeroBonito(conversãoNumerosGooglon(arquivoTxtB))
arquivoResposta = open('resultado.txt', 'w')
arquivoResposta.write('A; %d\nB; %d\nC; %d\nD; %s\nE; %d'%(preposições,verbo[0],verbo[1],' '.join(ordenação),resultadoNumeroBonito))
arquivoResposta.close()
