# exemplo de um menu com while
# CALCULADORA

opcao:int = 1
while opcao != 0:
  print('1 - Somar')
  print('2 - Subtrair')
  print('3 - Multiplicação')
  print('4 - Divisão')
  print('0 - Sair')

  opcao = int(input('Digite uma opção: '))

  if opcao >= 1 and opcao <= 4:
    n1:float = float(input("Digite o primeiro número: "))
    n2:float = float(input("Digite o segundo número: "))

    if opcao == 1:
      print("A soma é:", n1+n2)
    elif opcao == 2:
      print("A subtração é:", n1-n2)
    elif opcao == 3:
      print("A multiplicação é:", n1*n2)
    elif opcao == 4:
      print("A divisão é:", n1/n2)
  elif opcao == 0:
    print("FIM")
  else:
    print("Digite uma opção válida!")
