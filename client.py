"""Программа-клиент"""

import json
import socket
import sys
import time

from common.utils import get_message, send_message
from common.variables import (ACCOUNT_NAME, ACTION, DEFAULT_IP_ADDRESS,
                              DEFAULT_PORT, ERROR, PRESENCE, RESPONSE, TIME,
                              USER)


def create_presence(account_name='Guest'):
    """
    Функция генерирует запрос о присутствии клиента.
    :param account_name:
    :return:
    """

    # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_server_answer(message):
    """
    Функция разбирает ответ сервера.
    :param message:
    :return:
    """

    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200: OK'
        return f'400: {message[ERROR]}'
    raise ValueError


def main():
    """
    Загрузка параметров командной строки.
    client.py <addr> [<port>]:
    addr - IP-адрес сервера;
    port - TCP-порт на сервере.
    Например: client.py 192.168.1.153 8079
    Если нет параметров, то задаются значения по умолчанию.
    """

    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print("В качестве порта может быть указано только число в диапазоне от 1024 до 65535.")
        sys.exit(1)

    # Инициализация сокета и обмен

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
    send_message(transport, message_to_server)
    try:
        answer = process_server_answer(get_message(transport))
        print(answer)
    except(ValueError, json.JSONDecodeError):
        print("Не удалось декодировать сообщение сервера.")


if __name__ == "__main__":
    main()
