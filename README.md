# Тестовое задание для Python разработчика: IT Factory

# Стек технологий

- [Python 3.10](https://www.python.org/)
- [Django 4.2.2](https://www.djangoproject.com/)
- [Django REST Framework 3.14.0](https://www.django-rest-framework.org/)
- [Poetry](https://python-poetry.org/)

### Функционал
- Получение списка Торговых точек привязанных к переданному номеру телефона
```html
GET: http://127.0.0.1:8000/a_store/?phone=89096869722
```
- Посещение в Торговой точки
```html
POST: http://127.0.0.1:8000/visit/?phone=89096869722
```

### Админка
- ##### Работник
> - создание
> - редактирование
> - удаление
> - поиск по имени
> - 
- ##### Торговая точка
> - создание
> - редактирование
> - удаление
> - поиск по названию 
- ##### Посещение
> - просмотр
> - поиск по названию торговой точки
> - поиск по имени работника

## Запуск
### из IDE
##### Файл .env для локального запуска:
>* SECRET_KEY=
---------------
>* pip install poetry
>* poetry install
>* python manage.py migrate
>* python manage.py runserver