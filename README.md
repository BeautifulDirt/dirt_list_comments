# Веб-приложение заполнения формы обратной связи с сохранением результата в базу данных. Тестовое задание для кандидатов на стажировку в офис ритейл-компании

<img src="https://github.com/BeautifulDirt/dirt_list_comments/blob/main/banner.jpg" data-canonical-src="https://github.com/BeautifulDirt/dirt_list_comments/blob/main/banner.jpg" width="640" height="320" />

:star: **STAR ME!**

Задание было разделено на 2 части. Базовую и дополнительную. Базовая часть была обязательна для выполнения. Выполнение дополнительной рассматривались в качестве плюса. Так же плюсом было выполнение ограничений указанных после основных частей.

- [X] - было мною реализовано
- [ ] - не было реализовано в рамках данной работы

Итак, погнали:

0. [Тест. Базовая часть](https://github.com/BeautifulDirt/dirt_list_comments/blob/main/README.md#%D1%82%D0%B5%D1%81%D1%82-%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F-%D1%87%D0%B0%D1%81%D1%82%D1%8C)
1. [Тест. Дополнительная часть](https://github.com/BeautifulDirt/dirt_list_comments/blob/main/README.md#%D1%82%D0%B5%D1%81%D1%82-%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D1%87%D0%B0%D1%81%D1%82%D1%8C)
2. [Тест. Необязательные ограничения](https://github.com/BeautifulDirt/dirt_list_comments#%D1%82%D0%B5%D1%81%D1%82-%D0%BD%D0%B5%D0%BE%D0%B1%D1%8F%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BE%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)
3. [Запуск веб-приложения](https://github.com/BeautifulDirt/dirt_list_comments#%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA-%D0%B4%D0%B0%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE-%D0%B2%D0%B5%D0%B1-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-linux)


## Тест. Базовая часть

- [X] Создать базу данных в выбранной СУБД (*sqlite*, mysql, postgreesql или другая SQL-совместимая СУБД). Создать необходимые для выполнения задания таблицы и справочные данные (сделать это в виде sql скрипта).

- [X] Написать *python веб-приложение* заполнения формы обратной связи с сохранением результата в базу данных. Приложение должно реализовывать возможность просмотра и удаления добавленных записей.

- [X] **Добавление комментариев.** После запуска приложения при обращении по относительному пути */comment/* должна отображаться форма для заполнения. Форма состоит из следующих полей:
  - фамилия
  - имя
  - отчество
  - регион
  - город
  - контактный телефон
  - e-mail
  - комментарий. 

- [X] Поля фамилия, имя и комментарий являются обязательными. Поле комментарий текстовое. Для полей телефон и email следует производить проверку ввода. Номер телефона в формате «(код города) номер». Поля с некорректным вводом и не заполненные обязательные поля должны визуально выделяться красным цветом. Поля регион и город являются выпадающими списками, при этом список выбора поля город зависит от выбранного поля регион. Данные для этих списков должны храниться в СУБД. Значение в поля город должно динамически подгружаться по технологии *ajax* в соответствии с выбранным полем регион. Таблица соответствия для примера:

| Регион | Город | 
|---|---|
| Краснодарский край | Краснодар |
|  | Кропоткин |
|  | Славянск |
| Ростовская область | Ростов |
|  | Шахты |
|  | Батайск |
| Ставропольский край | Ставрополь |
|  | Пятигорск |
|  | Кисловодск |

## Тест. *Дополнительная часть*

- [X] **Просмотр комментариев.** При обращении по относительному пути /view/ должна выводиться таблица со списком добавленных комментариев. В этом же представлении должна быть возможность удалить определенную запись.

- [X] **Удаление комментариев.** В представлении просмотра комментариев реализовать возможность удаления отдельно выбранного комментария.

- [ ] **Просмотр статистики.** При обращении по относительному пути /stat/ должна выводиться таблица со списком тех регионов у которых количество комментариев больше 5, выводить так же и количество комментариев по каждому региону. Каждая строчка должны быть ссылкой на список города этого региона в котором отображается количество комментариев по этому городу.

## Тест. *Необязательные ограничения*

- [X] При реализации не использовать библиотек/модулей или фреймворков не входящих в стандартную библиотеку python или javascript


## Запуск данного веб-приложения (Linux)

1. Сменить права доступа у директории с проектом
    ```shell
       $ chmod +x dirt_list_comments
       $ chmod -r dirt_list_comments
    ```
2. Переходим в директорию с проектом
    ```shell
       $ cd dirt_list_comments
    ```
3. Запускаем веб-приложение
    ```shell
       $ python3 -m http.server --cgi
    ```
    или
    ```shell
       $ python -m SimpleHTTPServer 8000
    ```
4. В адресной строке браузера вписываем `localhost:8000` или `http://localhost:8000`
5. Профит :star:

**P.S. Работа была принята. И я, как кандидат, была принята на стажировку :3**


:calendar: *Август, 2018*
