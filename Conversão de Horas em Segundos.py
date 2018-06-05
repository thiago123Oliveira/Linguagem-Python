#Programa que converte dias, horas, minutos em segundos

__author__ = 'Aluno'

dias=int(input('Digite a quantidade de dias: '))
horas=int(input('Digite a quantidade de horas: '))
minutos=int(input('Digite a quantidade de minutos: '))
segundos=int(input('Digite a quantidade de segundos: '))
dias_seg=((dias*24)*3600)
horas_seg=(horas*3600)
min_seg=(minutos*60)
resultado=(dias_seg+horas_seg+min_seg+segundos)
print(resultado, 'segundos')



