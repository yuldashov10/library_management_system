from .get_year_field import get_year_field_from_user

__all__ = ["get_book_fields"]


def get_book_fields() -> tuple[str, str, int]:
    return (
        input("Введите название книги: ").strip(),
        input("Введите автора книги: ").strip(),
        get_year_field_from_user(),
    )
