__author__ = 'thiago'

cigarros_dia=float(input('Quantidade de cigarros por dia: '))
anos=float(input('Há Quantos anos é fumante: '))
total_dia=(cigarros_dia*0.16)
total=((total_dia*365)*anos)
print('Voce perdeu %d dias de sua vida'%total)
