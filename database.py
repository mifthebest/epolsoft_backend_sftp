from pymysql.cursors import DictCursor
from pymysql import connect
from datetime import datetime
from pymysql.err import OperationalError


def add_into_db(sql_user, sql_password, sql_database, data):
    result = []
    try:
        connection = connect(
            host='localhost',
            user=sql_user,
            password=sql_password,
            db=sql_database,
            charset='utf8mb4',
            cursorclass=DictCursor
        )
    except OperationalError:
        print('ERROR: Не удалось подключиться к базе данных')
    else:
        with connection.cursor() as cursor:

            for item in data:
                time = datetime.fromtimestamp(item['time'])
                query = f"INSERT INTO file_stat (fname, ctime) VALUES (%s, %s)"
                try:
                    cursor.execute(query, (item['name'], time))
                except OperationalError:
                    print('ERROR: Не удалось добавить данные в базу данных')

            query = f"SELECT * FROM file_stat"
            try:
                cursor.execute(query)
            except OperationalError:
                print('ERROR: Не удалось извлечь данные из базы данных')
            else:
                result = list(cursor)
                connection.commit()
                connection.close()

    return result