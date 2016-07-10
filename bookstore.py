class BookStore(object):
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def search_books(self, title=None, author=None):
        if title:
            return [t for t in self.books if title.lower() in t.title.lower()]
        elif author:
            return [t for t in self.books if author.lower() in t.author.name.lower()]
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
            
        
        
import unittest


class BookstoreTestCase(unittest.TestCase):
    def test_class_relationships(self):
        store = BookStore()

        # Authors
        poe = Author(name="Edgar Allan Poe", nationality="American")
        doyle = Author(name="Arthur Conan Doyle", nationality='British')

        # Books
        raven = Book(title="The Raven", author=poe)
        study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)

        # main
        store.add_book(raven)
        store.add_book(study_in_scarlet)

        self.assertEqual(store.books, [raven, study_in_scarlet])

        self.assertEqual(raven.author, poe)
        self.assertEqual(study_in_scarlet.author, doyle)
        


    def test_search_books_by_title(self):
        store = BookStore()

        # Authors
        poe = Author(name="Edgar Allan Poe", nationality="American")
        doyle = Author(name="Arthur Conan Doyle", nationality='British')

        # Books
        raven = Book(title="The Raven", author=poe)
        study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)

        # main
        store.add_book(raven)
        store.add_book(study_in_scarlet)

        results = store.search_books(title='raven')

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], raven)

    def test_search_books_by_authors_name(self):
        store = BookStore()

        # Authors
        poe = Author(name="Edgar Allan Poe", nationality="American")
        doyle = Author(name="Arthur Conan Doyle", nationality='British')

        # Books
        raven = Book(title="The Raven", author=poe)
        study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)

        # main
        store.add_book(raven)
        store.add_book(study_in_scarlet)

        results = store.search_books(author='doyle')

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], study_in_scarlet)

    def test_search_without_title_or_author_raises_error(self):
        store = BookStore()
        with self.assertRaises(AttributeError):
            store.search_books()
            
class ObjectsComparisonTestCase(unittest.TestCase):
    def test_compare_books(self):
        """Books with same author and title should be equal"""
        poe = Author(name="Edgar Allan Poe", nationality="American")

        b1 = Book(title="The Raven", author=poe)
        b2 = Book(title="The Raven", author=poe)
        self.assertEqual(b1, b2)

    def test_compare_authors(self):
        """Authors with same name and nationality should be equal"""
        a1 = Author(name="Edgar Allan Poe", nationality="American")
        a2 = Author(name="Edgar Allan Poe", nationality="American")

        self.assertEqual(a1, a2)       
            
t1 = BookstoreTestCase()
t1.test_class_relationships()
t2 = BookstoreTestCase()
t2.test_search_books_by_title()
t3 = BookstoreTestCase()
t3.test_search_books_by_authors_name()
t4 = BookstoreTestCase()
t4.test_search_without_title_or_author_raises_error()
t5 = ObjectsComparisonTestCase()
t5.test_compare_books()
t6 = ObjectsComparisonTestCase()
t6.test_compare_authors()



