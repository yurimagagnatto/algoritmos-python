# verifica se um número é primo
numero:int = int(input("Digite um número: "))
contadorDeZeros:int = 0

for i in range(1,numero+1):
  print(numero,"/",i,"Resto: ", numero%i)
  if numero%i == 0:
    contadorDeZeros = contadorDeZeros + 1
    # ou contadorDeZeros += 1

if contadorDeZeros == 2:
  print("O número é primo")
else:
  print("Não é primo")