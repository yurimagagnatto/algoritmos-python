# soma "n" notas e calcula a média
soma:float = 0
quantidade:int = int(input("Quantas notas quer calcular?"))

for i in range(1,quantidade+1):
  nota:float = float(input("Digite a nota " + str(i) + ": "))
  soma = soma + nota

print("Média", soma/quantidade)