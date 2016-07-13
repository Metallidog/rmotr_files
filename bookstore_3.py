class BookStore(object):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_books(self, title=None, author=None):
        if title:
            for book in (t for t in self.books if title.lower() in t.title.lower()):
                yield book
        elif author:
            for book in (t for t in self.books if author.lower() in t.author.name.lower()):
                yield book
        else:
            raise AttributeError

class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def __eq__(self, other):
        return True if self.name == other.name and \
        self.nationality == other.nationality else False

class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return True if self.title == other.title and \
        self.author == other.author else False