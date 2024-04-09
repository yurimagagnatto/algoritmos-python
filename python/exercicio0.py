# calcular média com base nas 3 notas informadas pelo usuário

nota1: float
nota2: float
nota3: float
media: float

nota1 = float( input("Digite a nota 1: ") )
nota2 = float( input("Digite a nota 2: ") )
nota3 = float( input("Digite a nota 3: ") )

media = (nota1 + nota2 + nota3) / 3

print(media)