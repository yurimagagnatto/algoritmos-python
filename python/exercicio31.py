# soma vários números perguntando pro usuário se ele gostaria de somar mais um

soma:float = 0
continuaSomando = True

while continuaSomando == True:
  print("A soma está valendo:", soma)
  opcao:str = input("Você gostaria de somar mais um número (s|n): ")
  
  if opcao == "s":
    # SOMAR
    numero:float = float(input("Digite o número a ser somado: "))
    soma = soma + numero
  else:
    # FIM
    continuaSomando = False

print("Total:", soma)