Реализованы endpoint и частично регистрация и аутентификация.
Бот просто запускается. Логики пока нет.

    Запуск из терминала:
            cd src/ && poetry run python -m crm

    Для работы нужны все зависимости ("poetry install" в директории с клонированным репозиоторием). БД в postgresql.
    Нужно создать БД и указать адрес в settings.py "database_url" либо создать в корне .env файл с указанием url БД.
    Сервис работает на FastAPI, соответственно имеем встроенную документацию host:8000/docs с доступом ко всем маршрутам.

    На вход принимаются данные в виде JSON объектов. Все поля объекта описаны в моделях.

    Регистрация доступна по uri /auth/sign-up. После регистрации возможно создание/удаление/редактирование

    Аутентификация по JWT токену.

ФУНКЦИОНАЛ:

    -  для доступа к функционалу нужно зарегистрировать пользователя по uri /auth/sign-up.
        - создастся пользователь в ролью "staff".
        - будет доступны создание, редактирование и удаление записей (клиенты, обращения, статусы, типы обращений)

    - создание в БД записей об обращениях.
        - записи фильтруются по датам (период/начало/конец или точная дача).
        - записи фильтруются по типу и/или статусу обращения.
        - сортировка и по датам и по типам/статусам не возможна. (в разработке)
        - для создания обращения должны существовать в БД статус, типы обращения и клиенты.

    - просмотр, удаление и редактирование записей
        - доступны только аутентифицированных пользователям. Аутентификации доступна по uri /auth/sign-in
          В случае успешной аутентификации в ответ прилетит jwt token. (хранение токена предполагалось в куках (в разработке))
        - редактирование и удаление по id сущности БД.
