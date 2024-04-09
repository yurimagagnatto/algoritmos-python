'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1. O produto do dobro do primeiro com metade do segundo.
2. A soma do triplo do primeiro com o terceiro.
3. O terceiro elevado ao cubo.
4. A raiz cúbica do segundo
'''

primeiroNumero: int
segundoNumero: int
terceiroNumero: float

primeiroNumero = int( input("Digite o primeiro número (inteiro): ") )
segundoNumero = int( input("Digite o segundo número (inteiro): ") )
terceiroNumero = float( input("Digite o terceiro número (real): ") )

resultado1: float
resultado2: float
resultado3: float
resultado4: float

resultado1 = (primeiroNumero * 2) * (segundoNumero / 2)
resultado2 = (primeiroNumero * 3) + terceiroNumero
resultado3 = terceiroNumero ** 3
resultado4 = segundoNumero ** (1/3) # raiz cúbica

print(resultado1, resultado2, resultado3, resultado4)