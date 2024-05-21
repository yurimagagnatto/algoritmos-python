# Com base em uma categoria definimos uma porcentagem de desconto para o produto
categoria:str = input("Digite a categoria (A, B ou C): ")
preco:float = float(input("Digite o preço do produto: ")) # reais
desconto:float = 0 # reais

if categoria == "A":
  desconto = preco * 0.10
elif categoria == "B":
  desconto = preco * 0.15
elif categoria == "C":
  desconto = preco * 0.20

precoFinal:float = preco - desconto
print("o preço final é", precoFinal)