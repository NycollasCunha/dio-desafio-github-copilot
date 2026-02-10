# Solicitar uma palavra e verificar se é um palíndromo

palavra = input("Digite uma palavra: ").lower()

palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"'{palavra}' é um PALÍNDROMO!")
else:
    print(f"'{palavra}' NÃO é um palíndromo")
