__author__ = 'thiago'

km=float(input('Digite a quantidade de KM percorridos: '))
dias=float(input('Digite a quantidade de dias do aluguel: '))
valor_dia=(60.00*dias)
valor_km=(0.15*km)
preco_a_pagar=(valor_dia+valor_km)
print('Valor a pagar = R$%.2f'%preco_a_pagar)
