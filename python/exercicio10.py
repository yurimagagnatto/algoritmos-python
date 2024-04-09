peso: float
altura: float
imc: float

peso = float( input("Informe o peso (em quilogramas): "))
altura = float( input("Informe a altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
  # 1
  print('MAGREZA')
elif imc < 25:
  # 2
  print('NORMAL')
elif imc < 30:
  # 3
  print('SOBREPESO	I')
elif imc < 40:
  # 4
  print('OBESIDADE	II')
else:
  # 5
  print('OBESIDADE GRAVE	III')

print('FIM')