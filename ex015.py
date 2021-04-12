# Um programa que pergunte a quantidaded e Km percorridos por um carro alugado e a quantidade de dias pelos quais ele
# foi alugado. Calcule o preço a pagar, Sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Insira a quantidade de Km percorridos:'))
dias = int(input('Durante quantos dias voce ficou com o carro?'))
pago = (dias*60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'. format(pago))
