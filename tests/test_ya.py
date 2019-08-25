import unittest
import ya


class TestingYa(unittest.TestCase):

    def test_translation(self):
        self.assertEqual(''.join(ya.translate_it('hi')['text']), 'привет')

    def test_wrong_translation(self):
        self.assertNotEqual(''.join(ya.translate_it('cat')['text']), 'собака')

    @unittest.expectedFailure
    def test_wrong_translation_fails(self):
        self.assertEqual(''.join(ya.translate_it('cat')['text']), 'собака')

    def test_return_code(self):
        self.assertEqual(ya.translate_it('hi', 'en', 'ru')['code'], 200)

    @unittest.expectedFailure
    def test_return_code_fails(self):
        self.assertEqual(ya.translate_it('hi', 1, 2)['code'], 200)


if __name__ == '__main__':
    unittest.main()
