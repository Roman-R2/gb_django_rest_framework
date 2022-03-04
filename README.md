# Django REST framework - «Web-сервис для работы с TODO-заметками»

## Практическое задание 1
1. Создать новый проект на github или gitlab.
2. Создать django-проект.
3. Установить DRF и подключить его к django-проекту.
4. Создать приложение для работы с пользователем.
5. Создать свою модель пользователя.
6. В ней поле email сделать уникальным.
7. Сделать для неё базовое API — по аналогии модели Author. В качестве полей выбрать
username, firstname, lastname, email. Если выбрать все поля, при попытке сериализации может
возникнуть ошибка сериализации связанного поля. Эту тему мы рассмотрим далее.
8. Подключить стандартную админку.
9. Создать суперпользователя.
10. (Задание со *) Создать management command — скрипт для запуска через manage.py для
автоматического создания суперпользователя и нескольких тестовых пользователей
(Management commands).
11. Сдать работу в виде ссылки на репозиторий с кодом.

## Практическое задание 2
1. С помощью create-react-app создать приложение для front-end-части проекта.
2. На React создать страницу для отображения списка пользователей из нескольких
компонентов. Пока эта страница будет доступна всем, после разграничения прав и только
для администратора.
3. Добавить на страницу компоненты Menu и Footer.
4. В главном приложении получить данные обо всех пользователях и вывести их на странице.

## Практическое задание 3
1. В проекте создать новое приложение для работы с TODO.
2. Добавить модель Project. Это проект, для которого записаны TODO. У него есть название,
может быть ссылка на репозиторий и набор пользователей, которые работают с этим
проектом. Создать модель, выбрать подходящие типы полей и связей с другими моделями.
3. Добавить модель TODO. Это заметка. У ToDo есть проект, в котором сделана заметка, текст
заметки, дата создания и обновления, пользователь, создавший заметку. Содержится и
признак — активно TODO или закрыто. Выбрать подходящие типы полей и связей с другими
моделями.
4. Создать API для моделей Projects и ToDo. Пока можно использовать ViewSets по аналогии с
моделью User.
5. При сериализации моделей выбрать нужный вид для связанных моделей.
6. (Задание со *) На стороне клиента используется camelCase в отличие от snake_case, который
мы используем в python. Реализовать представление данных в виде camelCase
(https://www.django-rest-framework.org/api-guide/parsers/#camelcase-json).