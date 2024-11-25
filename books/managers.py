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
    ) -> None:
        """
        Добавляет новый объект в базу данных.
        """
        new_book = Book(
            title=title,
            author=author,
            year=year,
        )
        data = self.__read()
        data.append(new_book)
        self.__write(data)
        print(f"Книга '{new_book.title}' успешно добавлена")

    def all(self) -> list[Book]:
        """
        Возвращает список объектов из базы данных.
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
        """
        return [
            book
            for book in self.__read()
            if (title and title.lower() in book.title.lower())
            or (author and author.lower() in book.author.lower())
            or (year and year == book.year)
        ]

    def update(self, pk: str, new_status: str) -> None:
        """
        Обновляет статус книги по id.
        :param pk: Идентификатор книги.
        :param new_status: Новый статус для книги.
        :raise:
        """
        data = self.__read()
        for index, book in enumerate(data):
            if book.id == pk:
                if data[index].status == new_status:
                    print(f"Книга уже в статусе '{new_status}'")
                else:
                    data[index].status = new_status
                    self.__write(data)

    def delete(self, pk: str) -> None:
        """
        Удаляет книгу по указанному id.
        :param pk: Идентификатор книги.
        :raise BookNotFoundError: Если книга не найлена.
        """
        data = self.__read()
        for index, book in enumerate(data):
            if book.id == pk:
                del data[index]
                self.__write(data)
                print(f"Книга '{book.title}' была удалена")
                return
        raise BookNotFoundError(f"Книга по id '{pk}' не найдена")

    def _file_exists(self) -> bool:
        return os.path.exists(self.__file)

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
