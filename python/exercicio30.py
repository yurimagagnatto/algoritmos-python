# soma vários números perguntando pro usuário quantos números ele quer somar

quantidade:int = int(input("Quantas vezes você gostaria de somar? "))
soma:float = 0

for i in range(1,quantidade+1):
  numero:float = float(input("Digite o número a ser somado: "))
  soma = soma + numero

print("a soma é:", soma)