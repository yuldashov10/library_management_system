from abc import ABC, abstractmethod

__all__ = ["BaseAbstractManager"]


class BaseAbstractManager(ABC):
    @abstractmethod
    def create(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def all(self) -> list:
        pass

    @abstractmethod
    def get(self, title: str, author: str, year: int) -> list:
        pass

    @abstractmethod
    def delete(self, pk: str) -> None:
        pass
