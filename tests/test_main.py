import unittest
import main
from parameterized import parameterized
from unittest.mock import patch

class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp --> work')

    @parameterized.expand(
        [
            ("2207 876234", True),
            ("11-2", True),
            ("10006", True)
        ]
    )
    def test_check_document_existance(self, user_doc_number, result):
        self.assertEqual(main.check_document_existance(user_doc_number), result)

    def tearDown(self) -> None:
        print('tearDown --> work')

    @patch('builtins.input', return_value="2207 876234")
    def test_using_side_effect1(self, mock_input):
        result = "Василий Гупкин"
        self.assertEqual(main.get_doc_owner_name(), result)

    @patch('builtins.input', return_value="11-2")
    def test_using_side_effect2(self, mock_input):
        result = "Геннадий Покемонов"
        self.assertEqual(main.get_doc_owner_name(), result)

    def test_get_all_doc_owners_names(self):
        user_list = {'Василий Гупкин', 'Геннадий Покемонов', 'Михаил'}
        self.assertEqual(main.get_all_doc_owners_names(), user_list)

    @patch('builtins.input', return_value='1')
    def test_add_new_shelf(self, mock_input):
        shelt = ['2207 876234', '11-2', '5455 028765']
        self.assertEqual(main.add_new_shelf(), (('1'), False))

    def test_add_new_doc(self):
        self.assertEqual(main.add_new_doc('7311', 'pass', 'Михаил', 2), 2)

    def test_delete_doc(self):
        self.assertTrue(main.delete_doc('10006'))

if __name__ == '__main__':
    unittest.main()


