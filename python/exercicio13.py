opcao: str

print('1 - Quadrado')
print('2 - Retângulo')
print('3 - Triângulo')
print('4 - Círculo')

opcao = input('Qual forma geométrica você gostaria de descobrir a área? ')

if opcao == "1":
  lado: float
  lado = float(input("Digite o lado do quadrado: "))
  print("A área do quadrado é", lado ** 2)
elif opcao == "2":
  ladoA: float = float(input("Digite o lado A: "))
  ladoB: float = float(input("Digite o lado B: "))
  print("A área do retângulo é", ladoA * ladoB)
elif opcao == "3":
  base: float = float(input("Informe a base do triângulo: "))
  altura: float = float(input("Informe a altura do triângulo: "))
  print("A área do triângulo é", (base*altura)/2)
elif opcao == "4":
  raio: float = float(input("Digite o raio do círculo: "))
  print("A área do círculo é", 3.14 * (raio ** 2))
else:
  print("Você informou uma opção inválida.")