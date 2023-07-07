#4)Ler um número inteiro (N) e, se N é maior que 1,mostrar os números inteiros de 1 até N. Senão, mostre os números de N até1.
n = int(input('Entre com um número inteiro'))
if n>1:
    conta = 1
    while conta <= n:
        print(conta)
        conta = conta + 1
else:
    while n <=1:
        print(n)
        n = n +1
