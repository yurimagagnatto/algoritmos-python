# soma vários números até o usuário digitar 0 para parar

soma:float = 0
continuaSomando = True

while continuaSomando == True:
  print("A soma está valendo:", soma)
  
  numero:float = float(input("Digite o número a ser somado (digite 0 para parar): "))
  
  if numero != 0:
    soma = soma + numero
  else:
    continuaSomando = False

print("Total:", soma)