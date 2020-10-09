import unittest
import json

import connexion
import logging

from app import listStore
from app import createStore
from app import updateStore

class TestStore(unittest.TestCase):
    def test01CreateStore(self):
        with open('createStoreTestCase.json') as payloadFile:
            payload = json.load(payloadFile)
            for testCase in payload:
                self.assertEqual(str(createStore(testCase["input"])), testCase["output"], "Create store failed!")

    def test02UpdateStore(self):
        print("")
        with open('updateStoreTestCase.json') as payloadFile:
            payload = json.load(payloadFile)
            for testCase in payload:
                self.assertEqual(updateStore(testCase['input'], testCase['input']['id'])[1], testCase['output'], "Update store failed!")

    def test03ListStore(self):
        with open('listStoreTestCase.json') as payloadFile:
            payload = json.load(payloadFile)
            for testCase in payload:
                inputTest = testCase['input']
                self.assertEqual(list(inputTest['storeId'], inputTest['categoryTerm'], inputTest['unitTerm'], inputTest['nameTerm'], inputTest['pageSize'], inputTest['pageIndex']), testCase['output'], "List store failed!")
        print("")

if __name__ == '__main__':
    unittest.main()
