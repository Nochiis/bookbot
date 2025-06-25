def get_book_text(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()

def contar_palabras(ruta):
    libro = get_book_text(ruta)
    words = libro.split(ruta)
    letras = len(words)
    num_words = f'Found {letras} total words'
    print(num_words)

def cantidad_caracteres(ruta):
    libro = get_book_text(ruta)
    libro = libro.lower()
    conteo = {}

    for caracter in libro:
        if caracter in conteo:
            conteo[caracter] += 1
        else:
            conteo[caracter] = 1

    return conteo

# función para ordenar por 'num'
def sort_on(item):
    return item["num"]

def ordenada(ruta):
    caracteres = cantidad_caracteres(ruta)
    lista = []

    for letra in caracteres:
        if letra.isalpha():  # solo letras
            lista.append({"char": letra, "num": caracteres[letra]})

    lista.sort(reverse=True, key=sort_on)
    return lista