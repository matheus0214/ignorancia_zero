"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
uma para fazer a conversão e uma para a saída. Assim, a função para efetuar as
conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores
de entrada todas as vezes que desejar.
"""


def convert_hour(hour, minute):
    return (hour, minute) if hour < 13 else (hour-12, minute)


def printer(converted, type_hour):
    hour, minute = converted

    return f"{hour}:{minute} {type_hour}"


print(printer(convert_hour(14, 25), "PM"))
print(printer(convert_hour(9, 25), "AM"))
