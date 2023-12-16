# ScheduleApp

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 13.1.2.

## Запуск приложения
Приложение представлено набором html, js, css файлов.
Для запуска откройте файл ./client/runnable_app/schedule-app/index.html с помощью любого live-server-а

В JB IDE кликните ПКМ на файл -> Open In -> Browser -> Chrome

В VS code можно установить плагин Live Server и открыть с помощью него.

**Через двойной клик по файлу приложение не загрузится и будет пустая html-страница**

## Ручная сборка
Для сборки необходимо установить nodejs v18, npm, angular-cli

Все файлы в директории runnable_app являются билдом angular-приложения.
Если есть необходимость внести изменения, сначала они вносятся в сами исходники в папке /src,
затем исполняется команда для сборки
```angular_cli
ng build
```
В папке dist появятся новые файлы со внесенными изменениями.
