# epolsoft backend 1 задание
Написать Java приложение (maven проект) (или язык на ваш выбор), со следующим функционалом:

- Запуск через консоль.
- Единственный параметр (параметр передаваемый через консоль при запуске приложения) - путь к файлу с настройками.
- После запуска приложение копирует все файлы по SFTP (параметры подключения беруться из файла настройки пункта #2 из удаленной директории (sftp_remote_dir) в локальную (local_dir).
- В локальную базу данных (MySQL или SQLite на выбор - параметры подключения берутся из файла настройки пункта #2) записываются дата-время и название скопированного файла.
- После окончания копирования пользователю на экран выводится содержимое базы данных (скопированные файлы и дата-время их копирования).

____
__Выбранный язык программирования - Python. Выбранная СУБД - MySQL.__
____
SQL скрипт для создания базы данных, таблицы и пользователя:
```
    CREATE DATABASE sftp;
    USE sftp;
    CREATE TABLE file_stat (
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
    	fname VARCHAR(256),
    	ctime DATETIME(6)
    );
    CREATE USER 'user'@'localhost' IDENTIFIED BY '4321';
    GRANT ALL PRIVILEGES ON sftp.file_stat TO 'user'@'localhost';
```
____
Файл настроек csv.config. Оформлен в виде csv файла.
____
В качестве SFTP сервера использовался локальный сервер https://www.rebex.net/tiny-sftp-server/. После его загрузки в папке RebexTinySftpServer-Binaries-Latest была создана дирректория folder и в файле RebexTinySftpServer.exe.config были изменены значения по умолчанию на следующие:
```
<!-- user credentials and root directory -->
    <add key="userName" value="admin" />
    <add key="userPassword" value="1111" />
    <add key="userRootDir" value="folder" />

```
____
Файлы с кодом: main.py, database.py, client.py. Работа скрипта осуществляется через запуск файла main.py.
____
Файл requirements.txt содержит описание всех необходимых модулей.
