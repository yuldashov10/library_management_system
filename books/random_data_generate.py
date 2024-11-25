from typing import Optional

from faker import Faker

from .managers import BookManager

__all__ = ["RandomDataGenerator"]


class RandomDataGenerator:
    """
    Генерации случайных книг и заполнения базы.
    """

    _DEFAULT_RANDOM_BOOKS_COUNT: int = 10

    def __init__(
        self,
        manager: BookManager,
        books_count: Optional[int] = None,
    ) -> None:
        """
        :param manager: Объект менеджера книг.
        :param books_count: Количество случайных книг. По умолчанию 10.
        """
        self.manager = manager
        self.books_count = books_count or self._DEFAULT_RANDOM_BOOKS_COUNT
        self.faker = Faker()

    def generate_books(self) -> None:
        """Генерирует список случайных книг."""
        [
            self.manager.create(
                title=self.faker.company(),
                author=self.faker.name(),
                year=int(self.faker.year()),
            )
            for _ in range(self.books_count)
        ]
        print(f"База данных заполнена {self.books_count} случайными книгами")
