import unittest
import main
import json
from unittest.mock import patch

documents = []
directories = {}


def setUpModule():
    with open('fixtures/directories.json', 'r', encoding='utf-8-sig') as dirs:
        directories.update(json.load(dirs))
    with open('fixtures/documents.json', 'r', encoding='utf-8-sig') as docs:
        documents.extend(json.load(docs))


def check_doc_in_docs(number):
    for doc in documents:
        if number in doc.values():
            return True
    return False


def check_doc_in_dirs(number):
    for doc in directories.values():
        if number in doc:
            return True
    return False


def check_doc(number):
    if check_doc_in_docs(number) and check_doc_in_dirs(number):
        return True
    return False


def check_shelf(number):
    for shelf in directories.keys():
        if number in shelf:
            return True
    return False


@patch('main.documents', documents, create=True)
@patch('main.directories', directories, create=True)
class TestMain(unittest.TestCase):

    def test_delete_doc(self):
        self.assertTrue(check_doc('11-2'))
        with patch('main.input', return_value='11-2') as doc_input:
            main.del_doc()
        self.assertFalse(check_doc('11-2'))

    @patch('builtins.input')
    def test_add_doc(self, mock_input):
        self.assertFalse(check_doc('322'))
        self.assertTrue(check_shelf('3'))
        mock_input.side_effect = ['driver license', '322', 'AV', '3']
        with unittest.mock.patch('builtins.input', mock_input):
            main.add_doc()
        self.assertTrue(check_doc('322'))

    def test_create_shelf(self):
        self.assertFalse(check_shelf('4'))
        with patch('main.input', return_value='4') as shelf_input:
            main.create_shelf()
        self.assertTrue(check_shelf('4'))

    @patch('builtins.input')
    def test_move_doc(self, mock_input):
        self.assertTrue('10006' in directories['2'] and not directories['4'])
        mock_input.side_effect = ['10006', '4']
        with unittest.mock.patch('builtins.input', mock_input):
            main.move_doc()
        self.assertTrue('10006' in directories['4'] and not directories['2'])


if __name__ == '__main__':
    unittest.main()
