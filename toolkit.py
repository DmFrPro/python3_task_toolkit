import file_name_without_.py as file

from inspect import getmembers, isfunction

# This is a dict which will be filled by functions_to_dict()
tasks = {}


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


def print_error(user_ans):
    print('')
    print("Задачи " + str(user_ans) + " не существует, повторите попытку")


def start_task_by_number():
    while True:
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
            print_error(user_ans)


def start():
    functions_to_dict()
    start_task_by_number()


# Automatically start the program
start()
