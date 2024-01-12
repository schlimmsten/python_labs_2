class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str):
        super().__init__(name, author)
        self.pages = 0

    def set_pages(self, pages: int) -> None:
        if pages > 0 and isinstance(pages, int):
            self.pages = pages
        else:
            print("Incorrect number of pages")

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}. Страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str):
        super().__init__(name, author)
        self.duration = 0

    def set_duration(self, duration: float) -> None:
        if duration > 0 and isinstance(duration, float):
            self.duration = duration
        else:
            print("Incorrect number of pages")

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}. Длительность {self.duration}"


