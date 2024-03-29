"""Программа запуска сервера и клиента со значениями по умолчанию."""

import subprocess

PROCESS = []

while True:
    ANSWER = input('Выберите действие: q - выход, s - запустить сервер и клиенты, '
                   'x - закрыть все окна: ')
    if ANSWER == 'q':
        break
    if ANSWER == 's':
        PROCESS.append(subprocess.Popen('python server.py',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))
        for i in range(5):
            PROCESS.append(subprocess.Popen('python client.py',
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif ANSWER == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
    else:
        print('Вы ввели неверную команду.')
