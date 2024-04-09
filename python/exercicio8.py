numero1: int
numero2: int
operacao: int

numero1 = int( input("digite o primeiro número: ") )
numero2 = int( input("digite o segundo número: ") )

operacao = int( input("você gostaria de somar (1) ou subtrair (2)? ") )

if operacao == 1 :
  soma: int = numero1 + numero2
  print(numero1, "+", numero2, "=", soma)

if operacao == 2 :
  sub: int = numero1 - numero2
  print(numero1, "-", numero2, "=", sub)

print("tchau!")