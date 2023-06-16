import unittest
from flask import Flask
from flask.testing import FlaskClient
from unittest.mock import patch

from server import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    @patch('deep_translator.MyMemoryTranslator.translate')
    def test_englishToFrench_translation(self, mock_translate):
        mock_translate.return_value = "Bonjour!"
        response = self.app.get('/englishToFrench?textToTranslate=Hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Bonjour!")
        mock_translate.assert_called_with('Hello')

    @patch('deep_translator.MyMemoryTranslator.translate')
    def test_frenchToEnglish_translation(self, mock_translate):
        mock_translate.return_value = "Hello!"
        response = self.app.get('/frenchToEnglish?textToTranslate=Bonjour')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Hello!")
        mock_translate.assert_called_with('Bonjour')

    def test_renderIndexPage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Text to be translated', response.data)

    if __name__ == '__main__':
        unittest.main()