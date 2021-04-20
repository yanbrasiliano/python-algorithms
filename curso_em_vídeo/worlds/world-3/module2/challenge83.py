#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
#A lista tem que ficar vazia, ou seja, a cada um '(' deve haver um ')' para fechar ou apagar ele da lista; caso esteja assim - expressão correta, senão, expressão errada.

expr = str(input('Enter a expression: '))
stack = []
for x in expr:
	if x == '(':
		stack.append('(')
	elif x == ')':
		if len(x) > 0: ## se o tamanho da pilha estiver maior que zero, apagar o ultimo valor da pilha.
			stack.pop()
		else: ## fecha a expressão.
			stack.append(')')
			break

###verificar se a pilha está cheia ou vazia.
if len(stack) == 0:
	print('xxx C.o.r.r.e.c.t xxx')
else:
	print('xxx E.r.r.o.r xxx')