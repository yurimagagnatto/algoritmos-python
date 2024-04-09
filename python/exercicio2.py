# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

quantidadeDeHorasTrabalhadas: float
valorDaHora: float
total: float

quantidadeDeHorasTrabalhadas = float( input("Digite a quantidade de horas trabalhadas: ") )

valorDaHora = float( input("Digite o valor da hora: ") )

total = quantidadeDeHorasTrabalhadas * valorDaHora

print("O total é:", total)