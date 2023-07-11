#Exercício7-Ler um número inteiro (N) e, se N é maior que 1, mostrar os números inteiros pares de 1 até N. Senão, mostre os números inteiros ímpares de N até 1
contador = 0
n = int(input('Entre com um número inteiro: '))
if n > 1:
    contador = 2
    while contador <= n:
        print(contador)
        contador = contador +2
else:
    n = n + (-(n%2))+1
    if n <= 1:
        print(n)
    else:
        n = n +2