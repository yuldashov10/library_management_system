import uuid
from typing import Any, Optional

from constants import BOOK_STATUS

__all__ = ["Book"]

from core.exceptions import InvalidBookStatusError


class Book:
    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        status: str = BOOK_STATUS.get("в наличии"),
        id: str = Optional[str],
    ) -> None:
        self.__id = id or str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.__status = status

    @property
    def id(self) -> str:
        return self.__id

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, value: str) -> None:
        self._validate_status(value)

        self.__status = value
        print(f"Статус книги изменён на '{BOOK_STATUS.get(value)}'")

    def to_json(self) -> dict[str, Any]:
        """
        Преобразует объект Book в JSON и возвращает.
        :return: Данные о книге в формате dict.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.__status,
        }

    @staticmethod
    def from_json(data: dict[str, Any]) -> "Book":
        """
        Преобразует JSON объект в объект класса  и возвращает.
        :param data: Данные о книге в формате dict.
        :return: Объект класса Book.
        :raise InvalidBookStatusError: Если указано недопустимое
        значение для статуса книги.
        """
        return Book(**data)

    def _validate_status(self, value: str) -> None:
        if value not in BOOK_STATUS:
            raise InvalidBookStatusError(
                "[Недопустимое значение] Возможные значения "
                f"для статуса {','.join(BOOK_STATUS.keys())}"
            )

    def __str__(self) -> str:
        return (
            f"\nИндентификатор: {self.id}"
            f"\nНазвание: {self.id}"
            f"\nАвтор: {self.id}"
            f"\nГод: {self.id}"
            f"\nСтатус: {self.id}"
        )
