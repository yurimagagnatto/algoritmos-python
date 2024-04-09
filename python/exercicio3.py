# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit: float
celsius: float

fahrenheit = float( input("Digite a temperatura em Fahrenheit: ") )

celsius = (fahrenheit - 32) / 1.8

print("A temperatura em graus Celsius é:", celsius)