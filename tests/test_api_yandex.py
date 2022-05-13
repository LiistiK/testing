import unittest
import api_yandex


class TestYaApi(unittest.TestCase):

    def setUp(self) -> None:
        print('setUp --> work')

    def test_success_create_folder(self):
        self.assertEqual(api_yandex.create_folder('test'),201)

    def test_passed_create_folder(self):
        self.assertEqual(api_yandex.create_folder('test_passed'),409)

    def tearDown(self) -> None:
        api_yandex.delete_folder('test')
        print('tearDown --> work')


if __name__ == '__main__':
    unittest.main()
