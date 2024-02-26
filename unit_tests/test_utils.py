"""Unit-тесты утилит (функций)"""

import json
import unittest

from common.utils import get_message, send_message
from common.variables import (ACCOUNT_NAME, ACTION, ENCODING,
                              MAX_PACKAGE_LENGTH, PRESENCE, TIME, USER)


class TestSocket:
    """
    Тестовый класс сокета для отправки и получения данных.
    Написан для того, чтобы не пришлось запускать модули с сокетами для тестирования функций.
    """

    def __init__(self, message):
        self.encoded_message = json.dumps(message).encode(ENCODING)
        self.received_message = None

    def send(self, message):
        """Метод отправляет данные в сокет."""

        self.received_message = message

    def recv(self, package_length=MAX_PACKAGE_LENGTH):
        """Метод получает данные из сокета."""

        return self.encoded_message


class UtilsTestCase(unittest.TestCase):
    test_message = {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Test'}}
    encoded_test_message = json.dumps(test_message).encode(ENCODING)

    def test_send_message(self):
        """Тест корректной отправки сообщения в сокет."""

        test_socket = TestSocket(self.test_message)

        send_message(test_socket, self.test_message)
        self.assertEqual(test_socket.received_message, test_socket.encoded_message)

    def test_get_message_ok(self):
        """Тест корректного декодирования словаря из сокета."""

        test_socket = TestSocket(self.test_message)
        self.assertEqual(get_message(test_socket), self.test_message)

    def test_get_message_no_dict(self):
        """Тест исключения."""

        test_socket = TestSocket("no dict message")
        self.assertRaises(ValueError, get_message, test_socket)


if __name__ == '__main__':
    unittest.main()
