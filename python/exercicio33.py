# exemplo de um menu com while
# CALCULADORA
# diferente da calculadora criada anteriormente, esta possibilita que cada operação seja executada com vários números (implementado apenas na soma!)

opcao:int = 1
while opcao != 0:
  print('1 - Somar')
  print('2 - Subtrair')
  print('3 - Multiplicação')
  print('4 - Divisão')
  print('0 - Sair')

  opcao = int(input('Digite uma opção: '))

  if opcao >= 1 and opcao <= 4:
    if opcao == 1:
      # aqui vou pedir pra digitar N números
      quantidade:int = int(input("Quantas vezes você gostaria de somar? "))
      soma:float = 0

      for i in range(1,quantidade+1):
        numero:float = float(input("Digite o número a ser somado: "))
        soma = soma + numero

      print("a soma é:", soma)
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
