# Todas as tabuadas entre 2 números
numero1: int = int(input("Digite o primeiro número: "))
numero2: int = int(input("Digite o segundo número: "))

for numeroAtual in range(numero1,numero2+1):
  print("Tabuada do", numeroAtual)
  for numeroDaTabuada in range(0,11):
    resultado:str = str(numeroDaTabuada)+"x"+str(numeroAtual)+"="+str(numeroDaTabuada*numeroAtual)
    print(resultado)