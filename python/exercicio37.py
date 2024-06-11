# criar um novo array (array3) intercalando 2 arrays (array1 e array2)

lista1 = [1,5,7,8]
lista2 = [6,2,1,4]

lista3 = []

contador:int = 0

while contador <= len(lista1)-1:
  lista3.append(lista1[contador])
  lista3.append(lista2[contador])
  
  contador = contador + 1

print(lista3)