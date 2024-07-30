import os

print(os.getcwd()) #  распечатывает путь нахождения
# os.mkdir('module_9') #  создает папку в пути нахождения

# def touch(path):
#     with open(file, 'a'):
#         os.utime(path, None) #  непонятная херня создания файла


os.chdir('../../') #  изменяет директорию на папку в пути нахождения

print(os.getcwd())

#os.mkdir('') #  создает папку в пути нахождения

#
#with open(os.path.join('module_9', 'homework_9_3.py'), 'a') as fp: #  создаем файл
 #    fp.close()