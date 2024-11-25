__all__ = ["BookNotFoundError", "InvalidBookStatusError"]


class BookNotFoundError(Exception):
    message = "Книга не найдена"


class InvalidBookStatusError(Exception):
    message = "Недопустимый статус для книги"
