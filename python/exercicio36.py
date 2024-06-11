# palíndromo com frases (com espaços)

frase:str = input("Digite uma frase: ")
# "socorram me subi no onibus em marrocos"

fraseSemEspacos:str = ""
fraseSemEspacosInvertida:str = ""

contador:int = 0

while contador <= len(frase)-1:
  letraAtual:str = frase[contador]
  if letraAtual != " ":
    fraseSemEspacos = fraseSemEspacos + letraAtual
  contador = contador + 1

# "socorrammesubinoonibusemmarrocos"

contador = len(fraseSemEspacos) - 1

while contador >= 0:
  letraAtual:str = fraseSemEspacos[contador]
  fraseSemEspacosInvertida = fraseSemEspacosInvertida + letraAtual
  contador = contador - 1

if fraseSemEspacos == fraseSemEspacosInvertida:
  print("a frase é um palíndromo")
else:
  print("a frase não é um palíndromo")
