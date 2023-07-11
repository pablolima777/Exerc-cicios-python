# 8)Ler um número inteiro de 1 a 10 e mostrar a sua tabuada.
n1 = int(input('Entre com um número inteiro: '))
contador = 1
while contador <= 10:
    res = n1 * contador
    print(res)
    contador +=1