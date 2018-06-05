__author__ = 'Aluno'

valor=float(input('Digite o preço do produto: '))
desconto=float(input('Digite a porcentagem do desconto: '))
valor_desconto=((valor/100)*desconto)
valor_mercadoria=(valor-valor_desconto)
print('valor do desconto =R$%.2f'%(valor_desconto))
print('valor da mercadoria =R$%.2f'%(valor_mercadoria))

