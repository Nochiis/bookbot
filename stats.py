def get_book_text():
    with open("books/frankenstein.txt", "r", encoding="utf-8") as f:
        return f.read()
    
    
def contar_palabras():
    libro = get_book_text()
    words = libro.split()
    letras = len(words)
    num_words = f"{letras} words found in the document"
    
    print(num_words)
    