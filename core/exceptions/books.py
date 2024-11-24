__all__ = ["BookNotFoundError"]


class BookNotFoundError(Exception):
    message = "Книга не найдена"
