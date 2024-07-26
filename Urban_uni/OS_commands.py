import os

print(os.getcwd()) #  распечатывает путь нахождения
# os.mkdir('module_9') #  создает папку в пути нахождения

# def touch(path):
#     with open(file, 'a'):
#         os.utime(path, None) #  непонятная херня создания файла


os.chdir('/Users/vk_home/PycharmProjects/Homeworks/Urban_uni/module_7') #  изменяет директорию на папку в пути нахождения

print(os.getcwd())
#
# with open(os.path.join('module_9', 'homework_9_2.py'), 'a') as fp: #  создаем файл
#     fp.close()