__author__ = 'Aluno'

salario=float(input('Digite o valor do salário R$ '))
aumento=float(input('Digite a porcentagem do aumento: '))
valor_aumento=((salario/100)*aumento)
aumento_salario=(salario+valor_aumento)
print('valor do aumento =R$%.2f'%(valor_aumento))
print('Novo salario =R$%.2f'%(aumento_salario))

