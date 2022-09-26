import os


def get_path(file_name):
    path = fr'{os.getcwd()}\{file_name}'
    return str(path.replace('\\', '\\\\'))
