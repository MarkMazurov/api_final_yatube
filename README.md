## Описание проекта
*Yatube_API* создан для простого и удобного взаимодействия с базой данных проекта *Yatube*.

*Yatube_API* спроектирован на базе **Django REST Framework**.

Сервис позволяет пользователям отправлять запросы к БД для получения постов, групп, комментариев
и подписок. Также авторизованным пользователям доступны функции создания, редактирования и удаления
постов и комментариев из БД. Авторизованные пользователи могут подписаться на других пользователей.

## Установка
1) Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/MarkMazurov/api_final_yatube.git
```
```
cd api_final_yatube
```
2) Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/scripts/activate
```
3) Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
4) Выполнить миграции:
```
python manage.py migrate
```
5) Запустить проект:
```
python manage.py runserver
```

## Примеры запросов
```
Получение всех постов: GET /api/v1/posts/
```
```
Редактирование поста: PUT /api/v1/posts/{id}/
```
```
Добавление комментария: POST /api/v1/posts/{post_id}/comments/
```
```
Получение подписок пользователя: GET /api/v1/follow/
```
```
Получение списка групп: GET /api/v1/groups/
```
## Автор проекта:

<h3 align="center"><a href="https://github.com/MarkMazurov" target="_blank">#Марк Мазуров#</a> 
</h3>
