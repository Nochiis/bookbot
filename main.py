def get_book_text():
    with open("books/frankenstein.txt", "r", encoding="utf-8") as f:
        print (f.read())

def main():
    libro = get_book_text()

main()
