from inspect import getmembers, isfunction
from importlib import import_module
import os

import pathlib
import sys

my_path = pathlib.Path().absolute()
sys.path.insert(0, my_path)


# This is a dict which will be filled by functions_to_dict()
tasks = {}


def choose_file():
    files_list = {}
    global file

    print('Вам доступен список файлов')
    print('')

    # Put file names to the files_list
    number = 1

    for file in os.scandir():
        current_file_name = os.path.basename(__file__)

        if file.is_file() and '.py' in file.name and file.name not in current_file_name:

            files_list[str(number)] = file.name
            print(str(number) + '. ' + file.name)  # print the file name
            number += 1

    print('')
    text = 'Выберите файл из предложенного списка\n' \
           'Укажите номер файла: '

    user_ans = str(input(text))

    #  Check for correct answer
    if user_ans in files_list.keys():

        # This is a file with tasks chosen by user
        file_name = files_list[user_ans]
        file = __import__(file_name[0: -3])

    else:
        print_error(user_ans, True)
        choose_file()


def functions_to_dict():

    for function_name, link in getmembers(file):
        if isfunction(link):

            # Save number in function's name
            tmp = function_name.split('_')
            number = tmp[-1]

            # Put number-function_name pairs to tasks
            tasks[number] = function_name

    # If tasks dict is empty, then user haven't added start() to file end
    if tasks == {}:
        text = 'В файле отсутствуют задачи, пожалуйста, добавьте хотя бы одну'

        print(text)
        print('')


def solve(method):
    print('')

    # Start the function from file
    getattr(file, method)()

    while True:
        print('')

        # asking for restart the task
        text = 'Чтобы перезапустить задачу, нажмите Enter\n' \
               'Чтобы выйти из программы, напишите quit\n' \
               'Чтобы выйти на главное меню, нажмите любой другой символ: '

        user_ans = str(input(text))

        if user_ans == '':
            print('')

            # Start the function from file
            getattr(file, method)()

        elif 'quit' in user_ans:
            quit()

        else:
            print('')
            break


def print_error(user_ans, isFile):
    print('')
    if isFile:
        print("Файла  под номером " + str(user_ans) + " не существует, повторите попытку")
    else:
        print("Задачи " + str(user_ans) + " не существует, повторите попытку")


def start_task_by_number():
    while True:
        print('')
        print('Вам доступен список задач')
        print('')

        for number, task in tasks.items():
            print(number + '. ' + task)

        print('')

        text = 'Чтобы выйти из программы, напишите quit\n' \
               'Введите номер задачи: '

        user_ans = str(input(text))

        # If user wants to play task
        if user_ans in tasks.keys():
            # Start the function
            solve(tasks[user_ans])

        # If user wants to exit program
        elif 'quit' in user_ans:
            quit()

        else:
            print_error(user_ans, False)


def start():
    choose_file()
    functions_to_dict()
    start_task_by_number()


#  Automatically start the program
start()
