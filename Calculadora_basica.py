def soma(*n):
    return sum(n)

def sub(*n):
    resultado = 0
    for num in n[0: ]:
        resultado -= num 
    return resultado

def multiplicacao(*n):
    resultado = 1
    for num in n:
        resultado *= num
    return  resultado

def divisao(*n):
    resultado = n[0]
    for num in n[1:]:
        if num == 0:
            print('os números não podem ser divisíveis por 0')
        else:
            resultado /= num
    return resultado