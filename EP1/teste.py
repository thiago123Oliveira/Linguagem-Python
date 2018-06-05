__author__ = 'Thiago'

def verificaPontuação(posiçõesJogadorOposto,listaPosição):
    listaOk=0
    listaNok=0
    resultados=[0,0,0,0,0]
    códigos=[4,5,1,2]
    contadorDicionário=1
    while contadorDicionário<=len(posiçõesJogadorOposto):
        for preencher in posiçõesJogadorOposto[str(contadorDicionário)]:
            contadorCódigo=1
            primeiro=int(preencher[contadorCódigo:])
            if contadorDicionário==1:
                while contadorCódigo<=códigos[(contadorDicionário)-1]:
                    if listaPosição[preencher[0]][(primeiro+contadorCódigo)-2]=='OK1':
                        listaOk+=1
                        contadorCódigo+=1
                    else:
                        listaNok+=1
                        contadorCódigo+=1
                if listaOk==4:
                    resultados[0]+=5
                    resultados[2]+=1
                else:
                    if listaNok==4:
                        resultados[4]+=1
                    else:
                        resultados[0]+=listaOk
                        resultados[1]+=1
                        resultados[3]+=1
        contadorDicionário+=1
    return resultados
