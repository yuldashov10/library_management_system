import json
import os
from typing import Optional

from books.models import Book
from constants import DATABASE_FILE_PATH
from core.exceptions import BookNotFoundError
from core.managers import BaseAbstractManager

__all__ = ["BookManager"]


class BookManager(BaseAbstractManager):
    """
    Менеджер книг.

    Доступные операции:
        - create() - Создание новой книги.
        - all() - Список всех книг.
        - get() - Получение книг по поисковому запросу.
        - delete() - Удаление книги по id.
    """

    def __init__(
        self,
        file_path: str = DATABASE_FILE_PATH,
        encoding: str = "UTF-8",
        ensure_ascii: bool = False,
        indent: int = 4,
    ) -> None:
        self.__file = file_path
        self.encoding = encoding
        self.ensure_ascii = ensure_ascii
        self.indent = indent

    def create(
        self,
        title: str,
        author: str,
        year: int,
        status: str,
    ) -> None:
        """
        Добавляет новый объект в базу данных.
        :raises FileNotFoundError: Если файл базы данных не найден.
        """
        new_book = Book(
            title=title,
            author=author,
            year=year,
            status=status,
        )
        data = self.__read()
        data.append(new_book)
        self.__write(data)
        print(f"Книга '{new_book.title}' успешно добавлена")

    def all(self) -> list[Book]:
        """
        Возвращает список объектов из базы данных.
        :raises FileNotFoundError: Если файл базы данных не найден.
        """
        return self.__read()

    def get(
        self,
        title: Optional[str],
        author: Optional[str],
        year: Optional[int],
    ) -> list[Book]:
        """
        Получает книги по поисковому запросу.
        :raises FileNotFoundError: Если файл базы данных не найден.
        """
        return [
            book
            for book in self.__read()
            if (title and title.lower() in book.title.lower())
            or (author and author.lower() in book.author.lower())
            or (year and str(year) == str(book.year))
        ]

    def delete(self, pk: str) -> None:
        """
        Удаляет книгу по указанному id.
        :param pk: Идентификатор книги.
        :raise BookNotFoundError: Если книга не найлена.
        :raise FileNotFoundError: Если файл базы данных не найден.
        """
        data = self.__read()
        for index, book in enumerate(data):
            if book.id == pk:
                del data[index]
                self.__write(data)
                print(f"Книга '{book.title}' удалена")
                return None
        raise BookNotFoundError(f"Книга по id '{pk}' не найдена")

    def _file_exists(self) -> None:
        if os.path.exists(self.__file):
            raise FileNotFoundError(f"Файл '{self.__file}' не найден")

    def __read(self) -> list[Book]:
        if not self._file_exists():
            return []

        with open(
            self.__file,
            mode="r",
            encoding=self.encoding,
        ) as read_file:
            return [Book.from_json(item) for item in json.load(read_file)]

    def __write(self, data: list[Book]) -> None:
        with open(
            self.__file,
            mode="w",
            encoding=self.encoding,
        ) as write_file:
            json.dump(
                [item.to_json() for item in data],
                write_file,
                ensure_ascii=self.ensure_ascii,
                indent=self.indent,
                sort_keys=True,
            )
