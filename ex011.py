#Pintando a Parede - Um Program que lê a largura e altura de uma parede em metros e calcule a área e quantidade de
# tinta necessária, Sabendo que cada L de tinta pinta uma área de 2m quadrados
larg = float(input('Digite a Largura da Sua Parede em metros:'))
alt = float(input('Digite a Altura da Sua Parede em metros:'))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar sua parede voce precisará de {}l de tinta'.format(tinta))
