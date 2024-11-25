__all__ = ["get_year_field_from_user"]


def get_year_field_from_user() -> int:
    while not (year := input("Введите год издания книги: ").strip()).isdigit():
        print(
            "[Некорректное значение] "
            "Укажите год издания книги в виде целого числа..."
        )

    return int(year)
