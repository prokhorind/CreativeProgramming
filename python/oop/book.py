class Book:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year}, Копій: {self.copies}"

class Library:
    def __init__(self):
        self.genres = {}

    def add_book(self, genre, book):
        if genre not in self.genres:
            self.genres[genre] = []
        self.genres[genre].append(book)

    def find_book(self, title):
        for genre, books in self.genres.items():
            for book in books:
                if book.title == title:
                    return f"Знайдено книгу '{title}' у жанрі '{genre}': {book}"
        return "Книгу не знайдено"

    def display_books_by_genre(self, genre):
        if genre in self.genres:
            print(f"Книги у жанрі '{genre}':")
            for book in self.genres[genre]:
                print(book)
        else:
            print("Жанр не знайдено")

    def display_all_books(self):
        print("Всі книги у бібліотеці:")
        for genre, books in self.genres.items():
            print(f"\nЖанр '{genre}':")
            for book in books:
                print(book)

# Створення бібліотеки
library = Library()
library.add_book("Фантастика", Book("Дюна", "Френк Герберт", 1965, 4))
library.add_book("Фантастика", Book("1984", "Джордж Орвелл", 1949, 3))
library.add_book("Детектив", Book("Шерлок Холмс", "Артур Конан Дойл", 1892, 5))
library.add_book("Роман", Book("Гордість і упередження", "Джейн Остін", 1813, 2))

# Використання методів
print(library.find_book("1984"))
library.display_books_by_genre("Фантастика")
library.display_all_books()
