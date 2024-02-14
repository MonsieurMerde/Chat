"""Утилиты"""

import json
from common.variables import ENCODING, MAX_PACKAGE_LENGTH


def get_message(sock):
    """
    Утилита приёма и декодирования сообщения.
    Принимает сокет, получает из него байты, выдаёт словарь.
    Если принято что-нибудь другое, отдаёт ошибку значения.
    :param sock:
    :return:
    """

    encoded_response = sock.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    """
    Утилита кодирования и отправки сообщения.
    :param sock: сокет, которому нужно отправить сообщение.
    :param message: словарь-сообщение, который нужно отправить.
    :return:
    """

    json_message = json.dumps(message)
    encoded_message = json_message.encode(ENCODING)
    sock.send(encoded_message)
