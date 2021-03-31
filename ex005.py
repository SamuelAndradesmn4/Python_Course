#Analisando o Antecessor e Sucessor de um numero inteiro
n = int(input("Digite um numero:"))
ant = n-1
suc = n+1
print('O antecessor de {} é: {} e seu sucessor é: {}'.format(n, ant, suc))
#Economizando memória
print('O antecessor de {} é: {} e seu sucessor é: {}'.format(n, (n-1), (n+1)))


