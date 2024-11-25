# Система управления библиотекой

> - [Техническое задание](./TASK.md)
> - Нажмите [здесь](./DEMO.md), чтобы открыть пример приложения

---

## Описание

Консольное приложение для управления библиотекой книг. Доступны возможности:

- добавлять;
- удалять;
- искать;
- отображать книги.

---

## Стек технологий

- Python 3.10+

---

## Как запустить проект

1. Клонировать проект и войти в директорию проекта:

```shell
git clone https://github.com/yuldashov10/library_management_system.git && cd library_management_system
```

> Шаги 2 – 4 можно пропустить, если не планируется генерировать случайные книги

2. Создать виртуальное окружение:

    - Linux/MacOS

      ```shell
       python3 -m venv .venv
      ```

    - Windows (Windows 10+)

       ```commandline
       python -m venv .venv
       ```

3. Активировать виртуальное окружение:

    - Linux/MacOS

      ```shell
       source .venv/bin/activate
      ```

    - Windows (Windows 10+)

       ```commandline
       call .venv\Scripts\activate
       ```

4. Установить зависимости:

    - Linux/MacOS

      ```shell
       pip3 install -r requirements.txt
      ```

    - Windows (Windows 10+)

       ```commandline
       pip install -r requirements.txt
       ```

5. Запустить проект:

    - Linux/MacOS

       ```shell
        python3 main.py
       ```

    - Windows (Windows 10+)

       ```commandline
       python main.py
       ```

---

## Как запустить тесты

- Запустить команду из корневой папки проекта:

    - Linux/MacOS

       ```shell
        python3 -m unittest -v
       ```

    - Windows (Windows 10+)

      ```commandline
      python -m unittest -v
      ```

## Автор

[Юлдашов Шохрух](https://t.me/shyuldashov/)
