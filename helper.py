from datetime import datetime
import os, os.path

def get_time():
    print('time init')
    now = datetime.now()
    return '{}-{}-{}-'.format(now.year, now.month, now.day)

def get_storage_filecount():
    path = '{}/storage/'.format(os.getcwd())
    return len(os.listdir(path))

def generate_filename():
    print('fn init')
    name = '{}{}'.format(get_time(), get_storage_filecount())
    print(name)
    return name
    

def get_path(filename):
    print('received: {}'.format(filename))
    path = ''
    path += os.getcwd()
    path += '/storage/'
    path += filename
    return path

def get_extension(filename):
    name, ext = filename.split('.')
    return '.'+ext