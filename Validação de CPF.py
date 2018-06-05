__author__ = 'Thiago'

Arquivo=[]
contador=1
entrada=int(input('MENU:\nDigite 1 para Calcular os digitos de controle do CPF:\nDigite 2 para Validar o CPF:\n'))

#///Função Para Calcular Digito de Controle

def calcularDigitoControle(lista):
    variavelSoma=1
    soma1=0
    soma2=0
    listaTeste=lista
    for numeros in listaTeste:
        soma1+=(int(numeros)*(variavelSoma))
        variavelSoma+=1
    primeiroDigito=soma1%11
    listaTeste.append(primeiroDigito)
    variavelSoma=0
    for segundo in listaTeste:
        soma2+=(int(segundo)*(variavelSoma))
        variavelSoma+=1
    segundoDigito=soma2%11
    listaTeste.append(segundoDigito)
    return primeiroDigito,segundoDigito,listaTeste

#Entrada

if entrada==1:
    while contador<=9:
        entradaCalcularCPF=int(input('Digite os 9 primeiros digitos do CPF: '))
        Arquivo.append(entradaCalcularCPF)
        contador+=1
    d1,d2,resultado=calcularDigitoControle(Arquivo)
    resposta=''
    for inteiro in resultado:
        resposta+=str(inteiro)
    print('Primeiro Digito: ',d1,'Segundo Digito: ',d2, 'CPF: ',resposta)


if entrada==2:
    while contador<=11:
        entradaCalcularCPF=input('Digite os 11 primeiros digitos do CPF: ')
        Arquivo.append(entradaCalcularCPF)
        contador+=1
    d1,d2,resultado=calcularDigitoControle((Arquivo[:-2]))
    if d1==(int(Arquivo[11-2])):
        if d2==(int(Arquivo[11-1])):
            print('CPF válido')
        else:
            print('CPF inválido')
    else:
        print('CPF inválido')






