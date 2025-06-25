import sys
from stats import contar_palabras, ordenada


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    ruta = sys.argv[1]
    
    # ----------- Word Count ----------
    print("---------- Word Count ----------")
    contar_palabras(ruta)

    # ----------- Character Count ----------
    print("---------- Character Count ----------")
    lista_ordenada = ordenada(ruta)

    for item in lista_ordenada:
        print(f"{item['char']}: {item['num']}")

    print("============== END ==============")

