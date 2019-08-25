import unittest
import main
import json

documents = []
directories = {}


def setUpModule():
    with open('fixtures/directories.json', 'r', encoding='utf-8-sig') as dirs:
        directories.update(json.load(dirs))
    with open('fixtures/documents.json', 'r', encoding='utf-8-sig') as docs:
        documents.extend(json.load(docs))


class TestMain(unittest.TestCase):
    def Test1(self):
        pass

if __name__ == '__main__':
    unittest.main()
    
