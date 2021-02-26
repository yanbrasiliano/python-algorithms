"""
11. Faça um programa com uma função chamada somaImposto. A função
possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
sobre vendas expressa em percentagem e custo, que é o custo de um item
antes do imposto. A função “altera” o valor de custo para incluir o imposto
sobre vendas.
"""
def sumTaxes(tax,cost):

	tax = tax/100

	return cost +(cost * tax)


old_value = float(input('Product Value:R$  '))
tax = float(input('Tax amount as a percentage %: '))
print()
print(f'New value:R${sumTaxes(tax,old_value)}')

