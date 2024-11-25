from books.models import Book

__all__ = ["BookTableView"]


class BookTableView:
    """
    Класс для отображения списка книг в табличном формате.
    """

    _HORIZONTAL_RULE_WIDTH: int = 120
    _BOOK_TITLE_MAX_WIDTH: int = 30
    _BOOK_AUTHOR_NAME_MAX_WIDTH: int = 20
    _TABLE_HEADERS: tuple[str, ...] = (
        "ID",
        "Название",
        "Автор",
        "Год",
        "Статус",
    )
    _TABLE_ROW_FORMAT: str = "{:<40} {:<30} {:<30} {:<6} {:<10}"

    def __call__(self, books: list[Book]) -> None:
        self._display(books)

    def _display(self, books: list[Book]) -> None:
        """
        Отображает список книг в табличном формате.

        :param books: Список объектов Book для отображения.
        """
        if not books:
            print("Список книг пуст.")
            return
        print()
        print(self._TABLE_ROW_FORMAT.format(*self._TABLE_HEADERS))
        print("-" * self._HORIZONTAL_RULE_WIDTH)

        for book in books:
            print(
                self._TABLE_ROW_FORMAT.format(
                    book.id,
                    book.title[: self._BOOK_TITLE_MAX_WIDTH],
                    book.author[: self._BOOK_AUTHOR_NAME_MAX_WIDTH],
                    book.year,
                    book.status,
                )
            )
