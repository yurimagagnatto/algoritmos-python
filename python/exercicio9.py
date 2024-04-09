peso: float
altura: float
imc: float

peso = float( input("Informe o peso (em quilogramas): "))
altura = float( input("Informe a altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
  print('MAGREZA')
else:
  # >= 18.5
  # NORMAL, SOBREPESO	I, OBESIDADE	II, OBESIDADE GRAVE	III
  if imc < 25:
    print('NORMAL')
  else:
    # >= 25
    # SOBREPESO	I, OBESIDADE	II, OBESIDADE GRAVE	III
    if imc < 30:
      print('SOBREPESO	I')
    else:
      # >= 30
      # OBESIDADE	II, OBESIDADE GRAVE	III
      if imc < 40
        print('OBESIDADE	II')
      else
        print('OBESIDADE GRAVE	III')

print('FIM')