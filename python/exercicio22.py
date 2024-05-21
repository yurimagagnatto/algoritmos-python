# Tabuada de um número:
numero: int = int(input("Digite um número: "))

for i in range(0,11):
  resultado:str = str(i)+"x"+str(numero)+"="+str(i*numero)
  print(resultado)