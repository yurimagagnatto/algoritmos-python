# ARRAY / LISTA / VETOR

# declarar uma lista (array ou vetor)
lista = [10, 20, 30, 40, 50]
print('array', lista) # imprime a lista toda
print('len', len(lista)) # imprime o tamanho da lista

# adiciona um item na lista
lista.append(60)

# varre a lista com FOR
for i:int in range(0,len(lista)):
  print(lista[i])

# varre a lista com WHILE
i:int = 0
while i < len(lista):
  print(lista[i])
  i = i + 1

# varre a lista com WHILE (de trás para a frente)
i = len(lista) - 1
while i >= 0:
  print(lista[i])
  i = i - 1

# procura um número na lista e fala quantas vezes encontrou
numero:int = 25
encontrei:bool = False
contador:int = 0

i = 0
while i < len(lista):
  # print(lista[i])
  if lista[i] == numero:
    encontrei = True
    contador = contador + 1
  i = i + 1

if encontrei == True:
  print("achei!")
else:
  print("não achei")

print("encontrei", contador, "vez(es)")


# inverte uma palavra/frase informada pelo usuário
# cada palavra/frase (string) é considerada uma lista de caracteres (letra)
palavra:str = input("Digite uma palavra: ")
espelho:str = ""

i:int = len(palavra) - 1
while i >= 0:
  # print(palavra[i])
  espelho = espelho + palavra[i]
  i = i - 1

print(espelho)