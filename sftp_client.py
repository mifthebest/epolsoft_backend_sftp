from paramiko import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import NoValidConnectionsError
from stat import S_ISDIR
from os import mkdir, path


result = []


def get_all_files(sftp, path_on_client, path_on_server=''):
    files = sftp.listdir(path_on_server)
    for file in files:
        if S_ISDIR(sftp.lstat(f'{path_on_server}\\{file}').st_mode):
            try:
                mkdir(f'{path_on_client}\\{file}')
            except FileExistsError:
                print(f'ERROR: Файл {path_on_client}\\{file} уже существует')
            finally:
                get_all_files(sftp, f'{path_on_client}\\{file}', f'{path_on_server}\\{file}')
        else:
            sftp.get(f'{path_on_server}\\{file}', f'{path_on_client}\\{file}')
            time = path.getctime(f'{path_on_client}\\{file}')
            result.append({'name': f'{path_on_client}\\{file}', 'time': time})


def copy_files_from_server(sftp_host, sftp_port, sftp_user, sftp_password, sftp_remote_dir, local_dir):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    try:
        client.connect(
            hostname=sftp_host,
            port=sftp_port,
            username=sftp_user,
            password=sftp_password,
            allow_agent=False,
            look_for_keys=False
        )
    except NoValidConnectionsError:
        print('ERROR: Не удалось подключиться к серверу')
    else:

        try:
            sftp = client.open_sftp()
        except Exception:
            print('ERROR: Ошибка открытия SFTP соединения')
        else:
            get_all_files(sftp, local_dir, sftp_remote_dir)
        finally:
            sftp.close()

    finally:
        client.close()

    return result