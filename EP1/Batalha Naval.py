__author__ = 'Thiago'

print('Bem vindo ao Jogo Batalha Naval')

#Dicionário de Posições

posições={'A':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'B':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'C':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'D':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'E':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'F':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'G':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'H':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'I':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'J':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'L':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'M':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'N':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'O':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
          'P':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']}


#///Função de Criar Lista de Tiros e dicionário de Jogadas (recebe arquivo de entrada)

def listaDicionário(file):
    PosiçõesJogador={}
    jogadasJogador=[]
    for linha in file.readlines():
        jogador=linha.rstrip().split(';')
        if jogador[0]!='#Jogada':
            if jogador[0]=='T':
                jogadasJogador=jogador[1]
            else:
                PosiçõesJogador[jogador[0]]=jogador[1]
                PosiçõesJogador[jogador[0]]=jogador[1].split('|')
    return jogadasJogador, PosiçõesJogador


#///Função Validando quantidade de Posições das Jogadas e Posições Existentes


def validandoQuantidade(PosiçõesJogador):
    acumuladorDeErros=[]
    contadorValidação=1
    letrasValidas='ABCDEFGHIJLMNOP'

#Verifica se as letras e números das posições existem

    while contadorValidação<=len(PosiçõesJogador):
        for letrasPosições in PosiçõesJogador[str(contadorValidação)]:
            if letrasPosições[0] not in letrasValidas:
                acumuladorDeErros.append('Posição inexistente\n')
                break
            if len(letrasPosições)==3:
                if letrasPosições[1:]>'15':
                    acumuladorDeErros.append('Posição inexistente\n')
                    break
        contadorValidação+=1

#Verifica se a quantidade de jogadas e tiros estão corretas

    contadorValidação=1
    while contadorValidação<=len(PosiçõesJogador):
        if contadorValidação==1:
            if len(PosiçõesJogador[str(contadorValidação)])!=2:
                acumuladorDeErros.append('Quantidade de peças código 1 errada\n')
                break
        if contadorValidação==2:
            if len(PosiçõesJogador[str(contadorValidação)])!=2:
                acumuladorDeErros.append('Quantidade de peças código 2 errada\n')
                break
        if contadorValidação==3:
            if len(PosiçõesJogador[str(contadorValidação)])!=5:
                acumuladorDeErros.append('Quantidade de peças código 3 errada\n')
                break
        if contadorValidação==4:
            if len(PosiçõesJogador[str(contadorValidação)])!=4:
                acumuladorDeErros.append('Quantidade de peças código 4 errada\n')
                break
        contadorValidação+=1
    return acumuladorDeErros


#///Função para Preencher posições e verificar se está sobreposto (Recebe a Função preencherPosições )


def verificaSobreposição(preencher,jogador,variavelCodigo,listaPosição):
    códigos=[4,5,1,2]
    contadorCódigo=1
    primeiro=int(preencher[contadorCódigo:])
    if primeiro+(códigos[(variavelCodigo)-1]-1)>15:
        return False
    while contadorCódigo<=códigos[(variavelCodigo)-1]:
        if jogador==1:
            if listaPosição[preencher[0]][(primeiro+contadorCódigo)-2]=='X' or posições[preencher[0]][(primeiro+contadorCódigo)-2]=='O':
                return False
            else:
                listaPosição[preencher[0]][(primeiro+contadorCódigo)-2]='X'
                contadorCódigo+=1
        else:
            if listaPosição[preencher[0]][(primeiro+contadorCódigo)-2]=='X' or posições[preencher[0]][(primeiro+contadorCódigo)-2]=='O':
                return False
            else:
                listaPosição[preencher[0]][(primeiro+contadorCódigo)-2]='O'
                contadorCódigo+=1
    return True


#///Função com a rotina para preenchimento das posições (chama a função verificaSobreposição)

def preencherPosições(posiçõesJogador,jogador):
    acumuladorErrosSobrepor=[]
    contadorDicionário=1
    while contadorDicionário<=len(posiçõesJogador):
        for preencher in posiçõesJogador[str(contadorDicionário)]:
            if contadorDicionário==1:
                if verificaSobreposição(preencher,jogador,contadorDicionário,posições) == False:
                    acumuladorErrosSobrepor.append('Posição já preenchida ou posição exece o limite')
                    break
            if contadorDicionário==2:
                if verificaSobreposição(preencher,jogador,contadorDicionário,posições) == False:
                    acumuladorErrosSobrepor.append('Posição já preenchida ou posição exece o limite')
                    break
            if contadorDicionário==3:
                if verificaSobreposição(preencher,jogador,contadorDicionário,posições) == False:
                    acumuladorErrosSobrepor.append('Posição já preenchida ou posição exece o limite')
                    break
            if contadorDicionário==4:
                if verificaSobreposição(preencher,jogador,contadorDicionário,posições) == False:
                    acumuladorErrosSobrepor.append('Posição já preenchida ou posição exece o limite')
                    break
        contadorDicionário+=1
    return acumuladorErrosSobrepor


#///Função com a rotina para preenchimento dos Tiros e verificação de tiros sobrepostos e tiros existentes

def verificaSobreposiçãoTiros(tiros,jogador,listaTirosPosição):
    acumuladorErrosTiros=[]
    letrasValidas='ABCDEFGHIJLMNOP'
    separadorPosições=tiros.split('|')
    if (len(separadorPosições))!=20:
        acumuladorErrosTiros.append('Quantidade de tiros errada\n')
    for letras in separadorPosições:
        if len(letras)==3:
            if int(letras[1:])>15:
                acumuladorErrosTiros.append('Tiro inexistente\n')
                break
        if letras[0] not in letrasValidas:
            acumuladorErrosTiros.append('Tiro inexistente\n')
            break
        else:
            primeiro=int(letras[1:])
            if jogador==1:
                if listaTirosPosição[letras[0]][(primeiro)-1]=='X' or listaTirosPosição[letras[0]][(primeiro)-1]=='OK1' or listaTirosPosição[letras[0]][(primeiro)-1]=='ER1'\
                        or listaTirosPosição[letras[0]][(primeiro)-1]=='OK2' or listaTirosPosição[letras[0]][(primeiro)-1]=='ER2':
                    acumuladorErrosTiros.append('Tiro inválido')
                    break
                elif listaTirosPosição[letras[0]][(primeiro)-1]=='O':
                    listaTirosPosição[letras[0]][(primeiro)-1]='OK1'
                else:
                    listaTirosPosição[letras[0]][(primeiro)-1]='ER1'
            if jogador==2:
                if listaTirosPosição[letras[0]][(primeiro)-1]=='O' or listaTirosPosição[letras[0]][(primeiro)-1]=='OK1' or listaTirosPosição[letras[0]][(primeiro)-1]=='ER1'\
                        or listaTirosPosição[letras[0]][(primeiro)-1]=='OK2' or listaTirosPosição[letras[0]][(primeiro)-1]=='ER2':
                    acumuladorErrosTiros.append('Tiro inválido')
                    break
                elif listaTirosPosição[letras[0]][(primeiro)-1]=='X':
                    listaTirosPosição[letras[0]][(primeiro)-1]='OK2'
                else:
                    listaTirosPosição[letras[0]][(primeiro)-1]='ER2'
    return acumuladorErrosTiros


#///Função para soma de pontos

def verificaPontuação(posiçõesJogadorOposto,jogador,listaPosição):
    resultados=[0,0,0,0,0]
    códigos=[4,5,1,2]
    contadorDicionário=1
    while contadorDicionário<=len(posiçõesJogadorOposto):
        for preencher in posiçõesJogadorOposto[str(contadorDicionário)]:
            listaOk=0
            listaNok=0
            contadorCódigo=1
            primeiro=int(preencher[contadorCódigo:])
            while contadorCódigo<=códigos[(contadorDicionário)-1]:
                if jogador==1:
                    variavelescolhejogador='OK1'
                if jogador==2:
                    variavelescolhejogador='OK2'
                if listaPosição[preencher[0]][(primeiro+contadorCódigo)-2]==variavelescolhejogador:
                    listaOk+=1
                    contadorCódigo+=1
                else:
                    listaNok+=1
                    contadorCódigo+=1
            if listaOk==códigos[(contadorDicionário)-1]:
                resultados[0]+=((códigos[(contadorDicionário)-1])+1)
                resultados[2]+=1
            else:
                if listaNok==códigos[(contadorDicionário)-1]:
                    resultados[4]+=1
                else:
                    resultados[0]+=listaOk
                    resultados[1]+=1
                    resultados[3]+=1
        contadorDicionário+=1
    return resultados



#Entrada do Arquivo

Arquivo1=open('Jogador1.txt','r')
jogadasJogador1,PosiçõesJogador1=listaDicionário(Arquivo1)
Arquivo1.close()

Arquivo2=open('Jogador2.txt','r')
jogadasJogador2,PosiçõesJogador2=listaDicionário(Arquivo2)
Arquivo2.close()

#Validação dos Arquivos de Entrada
jogador=''
erro=''
while True:
    quantidadePosiçõesJ1=validandoQuantidade(PosiçõesJogador1)
    if len(quantidadePosiçõesJ1)!=0:
        jogador='Jogador 1:\n'
        erro=quantidadePosiçõesJ1
        break
    quantidadePosiçõesJ2=validandoQuantidade(PosiçõesJogador2)
    if len(quantidadePosiçõesJ2)!=0:
        jogador='Jogador 2:\n'
        erro=quantidadePosiçõesJ2
        break
#Preenchendo posições e validando posição sobreposta
    posiçõesSobrepostaJ1=preencherPosições(PosiçõesJogador1,1)
    if len(posiçõesSobrepostaJ1)!=0:
        jogador='Jogador 1:\n'
        erro=posiçõesSobrepostaJ1
        break
    posiçõesSobrepostaJ2=preencherPosições(PosiçõesJogador2,2)
    if len(posiçõesSobrepostaJ2)!=0:
        jogador='Jogador 2:\n'
        erro=posiçõesSobrepostaJ2
        break

#Validando Tiros
    quantidadeTirosSobrepostaJ1=verificaSobreposiçãoTiros(jogadasJogador1,1,posições)
    if len(quantidadeTirosSobrepostaJ1)!=0:
        jogador='Jogador 1:\n'
        erro=quantidadeTirosSobrepostaJ1
        break
    quantidadeTirosSobrepostaJ2=verificaSobreposiçãoTiros(jogadasJogador2,2,posições)
    if len(quantidadeTirosSobrepostaJ2)!=0:
        jogador='Jogador 2:\n'
        erro=quantidadeTirosSobrepostaJ2
        break
    break
print(jogador,''.join(erro))

#Somando Pontuação

if jogador=='':
    resultadoJogador1=verificaPontuação(PosiçõesJogador2,1,posições)
    resultadoJogador2=verificaPontuação(PosiçõesJogador1,2,posições)
    if resultadoJogador1[0]>resultadoJogador2[0]:
        primeiroColocado='Jogador 1'
        segundoColocado='Jogador 2'
        print(' Classificação','\n',
    'O 1º Colocado Foi %s'%primeiroColocado,'\n',
    'O 2º Colocado Foi %s'%segundoColocado,'\n')
    if resultadoJogador2[0]>resultadoJogador1[0]:
        primeiroColocado='Jogador 2'
        segundoColocado='Jogador 1'
        print(' Classificação','\n',
    'O 1º Colocado Foi %s'%primeiroColocado,'\n',
    'O 2º Colocado Foi %s'%segundoColocado,'\n')
    if resultadoJogador2[0]==resultadoJogador1[0]:
        print(' Classificação','\n',
    'Jogador 1 e Jogador 2 Empataram','\n')

    print(' Alvos Acertados','\n',
    'Jogador 1 acertou %d alvo(s) Parciais e %d alvo(s) Inteiro(s)'%(resultadoJogador1[1],resultadoJogador1[2]),'\n',
    'Jogador 2 acertou %d alvo(s) Parciais e %d alvo(s) Inteiro(s)'%(resultadoJogador2[1],resultadoJogador2[2]),'\n',
    '\n','Peças que restaram no Tabuleiro','\n',
    'Jogador 1 Restaram %d alvo(s) Parciais e %d alvo(s) Inteiro(s)'%(resultadoJogador1[3],resultadoJogador1[4]),'\n',
    'Jogador 2 Restaram %d alvo(s) Parciais e %d alvo(s) Inteiro(s)'%(resultadoJogador2[3],resultadoJogador2[4]),'\n',
    '\n','Pontuação Final','\n',
    'Jogador 1 fez %d ponto(s)'%resultadoJogador1[0],'\n',
    'Jogador 2 fez %d ponto(s)'%resultadoJogador2[0],'\n')















