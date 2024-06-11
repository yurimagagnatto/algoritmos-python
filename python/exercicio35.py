# palíndromo com palavras (sem espaços)

palavra1:str = input("Digite uma palavra: ")

tamanho:int = len(palavra1)
contador:int = tamanho - 1

palavra2:str = ""

while contador >= 0:
  palavra2 = palavra2 + palavra1[contador]
  contador = contador - 1

if palavra1 == palavra2:
  print("é um palíndromo")
else:
  print("não é um palíndromo")