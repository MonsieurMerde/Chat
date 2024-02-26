"""Unit-тесты клиента"""

import unittest

from client import create_presence, process_server_answer
from common.variables import (ACCOUNT_NAME, ACTION, ERROR, PRESENCE, RESPONSE,
                              TIME, USER)


class ClientTestCase(unittest.TestCase):
    def test_create_presence(self):
        """Тест корректного запроса о присутствии клиента."""

        test_presence_dict = create_presence()
        test_presence_dict[TIME] = 1.1
        self.assertEqual(test_presence_dict,
                         {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}
                         )

    def test_process_answer_200(self):
        """Тест корректного разбора ответа 200 от сервера."""

        self.assertEqual(process_server_answer({RESPONSE: 200}), '200: OK')

    def test_process_answer_400(self):
        """Тест корректного разбора ответа 400 от сервера."""

        self.assertEqual(process_server_answer({RESPONSE: 400, ERROR: 'Bad Request'}),
                         '400: Bad Request'
                         )

    def test_process_answer_error(self):
        """Тест исключения."""

        self.assertRaises(ValueError, process_server_answer, 'some_message')


if __name__ == 'main':
    unittest.main()
