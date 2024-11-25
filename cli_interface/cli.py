from typing import Callable, Optional

from books import Book
from books.managers import BookManager
from core.exceptions import BookNotFoundError, InvalidBookStatusError
from core.utils import (
    BookTableView,
    get_book_fields,
    get_user_search_query_fields,
)

__all__ = ["LibraryCLI"]

table_view = BookTableView()


class LibraryCLI:
    """
    Интерфейс командной строки для управления библиотекой книг.

    Доступные команды:
        - add_book() - Добавление новой книги.
        - delete_book() - Удаление книги по ID.
        - search_books() - Поиск книг по названию, автору или году.
        - update_book_status() - Обновление статуса книги.
        - run() - Запуск интерактивного CLI.
    """

    def __init__(self) -> None:
        self.manager = BookManager()

    def add_book(self) -> None:
        title, author, year = get_book_fields()
        try:
            self.manager.create(title=title, author=author, year=year)
        except Exception as err_msg:
            print(f"[Ошибка] при добавлении книги {err_msg}")

    def delete_book(self) -> None:
        book_id: str = input("ID книги для удаления: ").strip()
        try:
            self.manager.delete(book_id)
        except BookNotFoundError as err_msg:
            print(f"[Ошибка] {err_msg}")
        except Exception as err_msg:
            print(f"[Ошибка] при удалении книги {err_msg}")

    def search_books(self) -> None:
        title, author, year = get_user_search_query_fields()
        try:
            books: list[Book] = self.manager.get(
                title=title or None,
                author=author or None,
                year=int(year) if year.isdigit() else None,
            )
        except Exception as err_msg:
            print(f"[Ошибка] при поиске книг {err_msg}")
        else:
            queries: tuple[str, ...] = (title, author, year)
            print(f"\nРезультаты поиска по запросу: '{self._join(queries)}'")
            table_view(books)

    def all_books(self) -> None:
        try:
            books: list[Book] = self.manager.all()
        except Exception as err_msg:
            print(f"[Ошибка] при отображении книг {err_msg}")
        else:
            table_view(books)

    def update_book_status(self) -> None:
        book_id: str = input("ID книги: ").strip()
        status: str = input("Новый статус: ").strip()
        try:
            self.manager.update(book_id, status)
        except (BookNotFoundError, InvalidBookStatusError) as err_msg:
            print(f"[Ошибка] {err_msg}")

    def _join(self, queries: tuple[str, ...]) -> str:
        return ",".join(query for query in queries if query)

    def _get_available_commands_name(self) -> str:
        available_commands: tuple[str, ...] = (
            "Добавить книгу",
            "Удалить книгу",
            "Найти книгу",
            "Отобразить все книги",
            "Изменить статус книги",
        )
        return "\n".join(
            f"{index}. {cmd}"
            for index, cmd in enumerate(available_commands, start=1)
        )

    def menu(self) -> None:
        header: str = "\nУправление библиотекой:\n"
        print(
            header,
            self._get_available_commands_name(),
            "0. Выход",
            sep="\n",
        )

    def run(self) -> None:
        commands: dict[str, Callable] = {
            "1": self.add_book,
            "2": self.delete_book,
            "3": self.search_books,
            "4": self.all_books,
            "5": self.update_book_status,
        }

        while True:
            self.menu()

            choice: str = input("Введите номер команды: ").strip()
            action: Optional[Callable] = commands.get(choice)

            if choice == "0":
                print("[Завершение] До свидания!")
                break
            elif action is None:
                print("[Неверный выбор] Пожалуйста, попробуйте снова")
            else:
                action()


if __name__ == "__main__":
    cli = LibraryCLI()
    cli.run()
