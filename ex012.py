#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do seu produto:R$'))
desc = preco - (preco * 5/ 100)
print('O preço desse produto é de R${} com 5% de Desconto é: R${}'.format(preco, desc))
