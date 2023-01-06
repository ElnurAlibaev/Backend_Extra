import os, time, shutil

def show_current_directories() -> None:

    print('Том в устройстве C не имеет метки.')
    print('Серийный номер тома: B218-516C\n')

    print(f'Содержимое папки {os.getcwd()}\n')

    for dir in os.listdir():
        last_edit_time=time.strftime('%d.%m.%y %H:%M', time.localtime(os.path.getmtime(dir)))

        if os.path.isfile(dir):
            print(f'{last_edit_time}               {os.stat(dir).st_size} {dir}')
        else:
            print(f'{last_edit_time}   <DIR>          {dir}')

def move_between_directories(command:str) -> None:
    if command[3:]=='..':
        os.chdir("..")
    elif command[3:] in os.listdir():
        os.chdir(f'{command[3:]}')
    else:
        print('Неверно задано имя папки.')

def create_file(name:str) -> None:
    if os.path.exists(f'{name}.txt'):
        print('Файл с таким названием уже существует')
    else:
        new_file=open(f'{name}.txt', 'w')
        new_file.close()

def create_directory(name:str) -> None:
    if os.path.exists(f'{name}'):
        print('Папка с таким названием уже существует')
    else:
        os.mkdir(f'{name}')

def delete_file(name:str) -> None:
    if os.path.exists(f'{name}')==False:
        print('Файла с таким названием не существует')
    elif os.path.isfile(f'{name}'):
        os.remove(f'{name}')
    else:
        print('Вы пытаетесь удалить папку, а не файл. Для удаления папки используйте команду rmdir')

def delete_directory(name:str) -> None:
    if os.path.exists(f'{name}'):
        try:
            os.rmdir(f'{name}')
        except:
            print("Внутри папки присутствуют другие файлы, вы уверены, что хотите удалить её? (Напишите Да или Нет)")
            s=input()
            if s=="Да":
                shutil.rmtree(f'{name}')
    else:
        print('Папки с таким названием не существует')

def rename_file_or_directory(name:str, new_name:str) -> None:
    if os.path.exists(f'{new_name}'):
        print('Папка или файл с таким названием уже существует')
    elif os.path.exists(f'{name}'):
        os.rename(name, new_name)
    else:
        print('Папки или файла с таким названием не существует')

def read_file(name:str) -> None:
    if os.path.exists(f'{name}') and os.path.isfile(f'{name}'):
        try:
            file=open(f'{name}', 'r', encoding='utf-8')
            print(file.read())
            file.close()
        except:
            print('Невозможно отркыть данный файл')
    else:
        print('Файла с таким названием не существует')


os.chdir('C:/Users/User/')

while True:

    command=input(f'{os.getcwd()}>')

    if command=='dir':
        show_current_directories()

    elif command[:3]=='cd ':
        move_between_directories(command)
    
    elif command[:3]=='mk ':
        create_file(command[3:])
    
    elif command[:6]=='mkdir ':
        create_directory(command[6:])

    elif command[:4]=='del ':
        delete_file(command[4:])

    elif command[:6]=='rmdir ':
        delete_directory(command[6:])
    
    elif command[:7]=='rename ':
        rename_file_or_directory(command[7:].split()[0], command[7:].split()[1])
    
    elif command[:5]=='read ':
        read_file(command[5:])

    elif command=='exit':
        break
    
    else:
        print(f'"{command}" не является внутренней или внешней командой, исполняемой программой или пакетным файлом.')

    print('\n')
