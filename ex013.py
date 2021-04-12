# Um algoritmo que leia o salário de um funcionario e mostra um novo salário com 15% de aumento.
salario = float(input('Insira o valor do Seu salário atual:'))
novo = salario + (salario * 15/100)
print('Um funcionario que ganha R${:.2f}, com 15% de aumento, passará a ganhar R${:.2f}' .format(salario, novo))
