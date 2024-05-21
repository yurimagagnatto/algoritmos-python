# contagem do 1 ao número que o usuário digitou

numero:int = int(input('digite um número: '))

# exemplo com "for"
for i in range(1,numero+1):
  print(i)

# exemplo com "while"
i:int = 1
while i <= numero:
  print(i)
  i = i + 2