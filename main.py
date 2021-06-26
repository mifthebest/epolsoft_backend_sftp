from sys import argv
from csv import DictReader

from sftp_client import copy_files_from_server
from database import add_into_db


try:
    with open(argv[1]) as csv_file:
        reader = DictReader(csv_file)
        for info in reader:
            data = copy_files_from_server(
                info['sftp_host'],
                info['sftp_port'],
                info['sftp_user'],
                info['sftp_password'],
                info['sftp_remote_dir'],
                info['local_dir']
            )
            result = add_into_db(
                info['sql_user'],
                info['sql_password'],
                info['sql_database'],
                data
            )

except IndexError:
    print('ERROR: Отсутствует путь к файлу настроек')
except FileNotFoundError:
    print('ERROR: Путь к файлу настроек указан некорректно')
else:
    for item in result:
        print(f"FILE: {item['fname']}       TIME: {item['ctime']}")