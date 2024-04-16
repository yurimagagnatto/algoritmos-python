# 1 – Triângulo escaleno: triângulo que possui todos os lados com medidas diferentes.
# 2 – Triângulos isósceles: triângulo que possui dois lados com medidas iguais.
# 3 – Triângulo equilátero: triângulo que possui todos os lados com medidas iguais.

ladoA: float
ladoB: float
ladoC: float

ladoA = float( input("Digite o tamanho do primeiro lado: ") )
ladoB = float( input("Digite o tamanho do segundo lado: ") )
ladoC = float( input("Digite o tamanho do terceiro lado: ") )

if ladoA == ladoB and ladoB == ladoC:
  print('Triângulo equilátero')
elif ladoA == ladoB or ladoB == ladoC or ladoC == ladoA:
  print('Triângulos isósceles')
else:
  print('Triângulo escaleno')
