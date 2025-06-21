def get_book_text():
    with open("books/frankenstein.txt", "r", encoding="utf-8") as f:
        return f.read()
    
def main():
    libro = get_book_text()
    wordss()   
    
def wordss():
    contador = 0
    librosin = get_book_text()
    words = librosin.split()
    for i in words:
        contador += 1 

    num_words = f"{contador} words found in the document"
    
    print(num_words)
    
main()
