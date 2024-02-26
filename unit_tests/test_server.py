"""Unit-тесты сервера"""

import unittest

from common.variables import (ACCOUNT_NAME, ACTION, ERROR, PRESENCE, RESPONSE,
                              TIME, USER)
from server import process_client_message


class ServerTestCase(unittest.TestCase):
    test_response_ok = {RESPONSE: 200}
    test_response_error = {RESPONSE: 400, ERROR: 'Bad Request'}

    def test_process_client_message_ok(self):
        """Тест корректного разбора сообщения от клиента, если словарь-сообщение корректное."""

        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1, USER: {ACCOUNT_NAME: 'Guest'}}),
            self.test_response_ok)

    def test_process_client_message_no_action(self):
        """
        Тест корректного разбора сообщения от клиента,
        если словарь-сообщение не содержит ключа ACTION.
        """

        self.assertEqual(process_client_message(
            {TIME: 1, USER: {ACCOUNT_NAME: 'Guest'}}), self.test_response_error)

    def test_process_client_message_wrong_action(self):
        """
        Тест корректного разбора сообщения от клиента,
        если в словаре-сообщении значение по ключу ACTION не равно PRESENCE
        (message[ACTION] != PRESENCE).
        """

        self.assertEqual(process_client_message(
            {ACTION: 'wrong', TIME: 1, USER: {ACCOUNT_NAME: 'Guest'}}),
            self.test_response_error)

    def test_process_client_message_no_time(self):
        """
        Тест корректного разбора сообщения от клиента,
        если словарь-сообщение не содержит ключа TIME.
        """

        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.test_response_error)

    def test_process_client_message_no_user(self):
        """
        Тест корректного разбора сообщения от клиента,
        если словарь-сообщение не содержит ключа USER.
        """

        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1}), self.test_response_error)

    def test_process_client_message_other_user(self):
        """
        Тест корректного разбора сообщения от клиента,
        если в словаре-сообщении по ключу USER
        в словаре по ключу ACCOUNT_NAME значение не равно 'Guest'
        (message[USER][ACCOUNT_NAME] != 'Guest').
        """

        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1, USER: {ACCOUNT_NAME: 'Other User'}}),
            self.test_response_error)


if __name__ == '__main__':
    unittest.main()
