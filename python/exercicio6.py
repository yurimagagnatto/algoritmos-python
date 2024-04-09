# Verificar se um número é par ou ímpar

x: int
resto: int

x = int( input("Digite um número: ") )

resto = x % 2

if resto == 0 :
  print("É par")
else :
  print("É ímpar")