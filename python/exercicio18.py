# Verifica se um número é positivo ou negativo
numero:int = int(input("Digite um número inteiro: "))

if numero > 0:
  print('positivo')
elif numero < 0:
  print('negativo')
else:
  print('zero')
