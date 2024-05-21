# jogo adivinhação
import random

numeroAleatorio:int = random.randint(1,100)
numeroDigitado:int = 0

while numeroAleatorio != numeroDigitado:
  numeroDigitado:int = int(input('digite um número: '))
  if numeroDigitado < numeroAleatorio:
    print('o número digitado é menor!')
  elif numeroDigitado > numeroAleatorio:
    print('o número digitado é maior!')

print('vc acertou!')