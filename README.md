test_steelkiwi
==============

SteelKiwi Test

Создать django проект который управляет базой студентов, Сущности:
Студент - ФИО, дата-рождения, No.студ-билета, группа(FK(Группа))
Группа - Название, староста(FK(Студент))
Проект должен быть сконфигурирован на sqlite и иметь initial_data.json
с подготовленными данными(несколько групп и студентов)
Создать следующие views:
список групп (таблица - название, кол-во человек в группе, староста)
при нажатии на группу - страница с со списком студентов для этой группы
создание/редактирование/удаление групп/студентов
Добавить авторизацию для этих страниц (username/password)
Добавить авторизацию email+password
Сделать middleware который на всех страницах(content-type ==
text/html) добавляет время выполнения запроса и количество sql
запросов(перед закрывающим тегом </body>)
Django.Admin - создать admin views для Групп/студентов (студенты так
же должны быть как inline для Групп)
Шаблоны/Контекст - сделать template-context-processor который
добавляет django.settings в контекст шаблонов
Шаблоны/Теги - написать тег который принимает любой объект и рендерит
ссылку на его редактирование в админке (например {% edit_list
request.user %})
Сигналы - написать обработчик сигнала который для каждой модели
создает запись в базе о ее создании/редактировании/удалении
Команды - написать django комманду которая выводит список групп и
студентов в группе в консоль (что такое django-команда -
http://webnewage.org/2008/02/05/komandovat-paradom-budet-django/)
Django.TestFramework - написать django-testcase (unittest) который
логинится на сайт, добавляет группу и студента в созданную группу
