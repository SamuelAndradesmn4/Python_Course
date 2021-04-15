# Um programa que pergunte a quantidaded e Km percorridos por um carro alugado e a quantidade de dias pelos quais ele
# foi alugado. Calcule o preço a pagar, Sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
modelo = str(input('Insira o modelo do Carro Alugado'))
placa = str(input('Insira a numeração da placa:'))
data = int(input('Insira a data em que o carro foi alugado '))
km = float(input('Insira a quantidade de Km percorridos com o Carro:'))
dias = int(input('Insira a quantidade de dias passados com o Carro:' ))
pago = (dias*60) + (km * 0.15)
print('O carro de modelo{}, de placa{}, alugado na data{}, tem valor total a pagar é de R${:.2f}'. format(modelo, placa, data, pago))
