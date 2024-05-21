# Todos números pares do 0 ao número que o usuário digitou
numero:int = int(input("Digite um número: "))

for i in range(0,numero+1):
  if i%2 == 0:
    print("o número", i, "é par")