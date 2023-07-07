# 3)Ler um número inteiro (N) maior que 1 e mostrar os números inteiros de 1 até N.
contador = 0
n = int(input('Entre com o valor inteiro de N: '))
while True:
    if contador == n:
        break
    else:
        contador = contador +1
        print(contador)
   