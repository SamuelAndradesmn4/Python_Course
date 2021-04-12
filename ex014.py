#Um program que converte temperatura digitando em graus Celsius e converte para Fhrenheit.
temperatura = float(input('Informe a temperatura atual em Graus Celsius:'))
fahrenheit = ((9*temperatura)/5)+32
print ('A temperatura de {}°C corresponde a {}°F!'. format(temperatura, fahrenheit))
