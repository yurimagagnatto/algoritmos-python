# Faça um Programa que calcule a área de um retângulo

ladoA: float
ladoB: float
area: float
resposta: str

ladoA = float(input("Digite o lado A: "))
ladoB = float(input("Digite o lado B: "))
area = ladoA * ladoB

resposta = "A área do retângulo é " + str(area)

print(resposta)