isbn_db = {
    'ABC123': ('Pan tadeusz', 'Adam'),
    'ABC124': ('Zawod programista', 'Maciej Aniserowicz'),
    'ABC125': ('DNA', 'Maciej Aniserowicz'),
}


class Book:
    total_number_of_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_number_of_books += 1
        self.id = Book.total_number_of_books

    @classmethod
    def from_isbn(cls, isbn):
        title, author = isbn_db.get(isbn)
        return Book(title, author)


if __name__ == '__main__':
    book1 = Book('Ogień', 'Jan Nowak')
    book2 = Book('Ogień2', 'Jan Nowak2')
    book3 = Book('Ogień', 'Jan Nowak3')
    print(book1.id)
    print(book2.id)
    print(book3.id)
    book4 = Book.from_isbn('ABC123')
    # print(isbn_db.get('ABC123'))
    print(book4.title, book4.author, book4.id)
