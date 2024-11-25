__all__ = ["get_user_search_query_fields"]


def get_user_search_query_fields() -> tuple[str, str, str]:
    return (
        input(
            "Название книги для поиска (нажмите Enter, чтобы пропустить): "
        ).strip(),
        input(
            "Автор книги для поиска (нажмите Enter, чтобы пропустить): "
        ).strip(),
        input(
            "Год издания книги для поиска (нажмите Enter, чтобы пропустить): "
        ).strip(),
    )
