# Verifica se um ano é bissexto
ano: int
ano = int( input("Digite um ano: ") )

if ano % 4 == 0 and ano % 100 != 0:
  print("É bissexto!")
elif ano % 400 == 0:
  print("É bissexto!")
else:
  print("Não é bissexto!")

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
  print("É bissexto!")
else:
  print("Não é bissexto!")