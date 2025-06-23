def get_book_text():
    with open("books/frankenstein.txt", "r", encoding="utf-8") as f:
        return f.read()

def contar_palabras():
    libro = get_book_text()
    words = libro.split()
    letras = len(words)
    num_words = f"{letras} words found in the document"
    print(num_words)

def cantidad_caracteres():
    libro = get_book_text()
    libro = libro.lower() 
    conteo = {}

    for caracter in libro:
        if caracter in conteo:
            conteo[caracter] += 1
        else:
            conteo[caracter] = 1

    return conteo 