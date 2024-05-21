# Usuário informa 3 números distintos e verificamos qual é o número que não é nem o menor, nem o maior 
a:int = int(input("Digite o primeiro número: "))
b:int = int(input("Digite o segundo número: "))
c:int = int(input("Digite o terceiro número: "))

if (a > b and a < c) or (a > c and a < b):
  print("o número do meio é o", a)
elif (b > a and b < c) or (b > c and b < a):
  print("o número do meio é o", b)
else:
  print("o número do meio é o", c)
