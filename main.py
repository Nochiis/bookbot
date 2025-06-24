from stats import contar_palabras, ordenada

print("============== BOOKBOT ==============")
print("Analyzing book found at books/frankenstein.txt...")

# ----------- Word Count ----------
print("---------- Word Count ----------")
contar_palabras()

# ----------- Character Count ----------
print("---------- Character Count ----------")
lista_ordenada = ordenada()

for item in lista_ordenada:
    print(f"{item['char']}: {item['num']}")

print("============== END ==============")