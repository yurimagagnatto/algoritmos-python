numero1: float
numero2: float
operacao: str

print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite a opção desejada: ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if operacao == "1" or operacao == "Adição":
  # Adição
  print(numero1 + numero2)

elif operacao == "2" or operacao == "Subtração":
  # Subtração
  print(numero1 - numero2)

elif operacao == "3" or operacao == "Multiplicação":
  # Multiplicação
  print(numero1 * numero2)

elif operacao == "4" or operacao == "Divisão":
  # Divisão
  print(numero1 / numero2)
else:
  print("Você não digitou uma opeção válida.")