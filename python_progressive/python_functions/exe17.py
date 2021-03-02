"""
Faça um programa que converta da notação de 24 horas para a notação
de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A
entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma
para fazer a conversão e uma para a saída. Registre a informação A.M./P.M.
como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as
conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua
um loop que permita que o usuário repita esse cálculo para novos valores de
entrada todas as vezes que desejar.
    """


def converterBR(hour):
    if hour > 12 and hour != 24:
        count = 0
        for v in range(hour):
            if v >= 12:
                count += 1
            return count
    elif hour == 24:
        return 0
    else:
        return hour


def menu():
    hour = int(input('Hour: '))
    minute = int(input('Minute: '))

    print(f'{hour}:{minute} = {converterBR(hour),minute}')


while True:
    menu()
