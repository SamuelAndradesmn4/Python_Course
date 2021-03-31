# CONVERSOR DE MEDIDAS - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
medida = float(input('Digite uma distancia em Metros:'))
cm = medida * 100
mm = medida * 1000
dm = medida * 10

print('{}m em outras unidades de medidas corresponde a:\n{}cm\n{}mm\n{}dm.'.format(medida, cm, mm,dm))
