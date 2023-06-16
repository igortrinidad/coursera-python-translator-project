# Python Project for AI & Application Development - Assignment

This project is a web translator application built using Python and the Flask web framework. The goal of the application is to provide a user-friendly interface for translating text between English and French languages.

The project utilizes the `deep_translator` library, which provides a translation API called `MyMemoryTranslator`. This API allows the application to translate text from one language to another. Specifically, the application supports two translation routes:

1. `/englishToFrench`: This route receives a text input in English through a GET request parameter named `textToTranslate`. It uses the `MyMemoryTranslator` API to translate the English text to French and returns the translated text as the response.

2. `/frenchToEnglish`: Similar to the previous route, this route receives a text input in French through a GET request parameter named `textToTranslate`. It uses the `MyMemoryTranslator` API to translate the French text to English and returns the translated text as the response.

Additionally, the application provides a default route `/` that renders an HTML template named `index.html`. This template likely includes a form where users can enter the text to be translated and select the translation direction.

To run the application, the main script checks if it's being executed directly (not imported as a module) and then starts the Flask development server on the IP address `0.0.0.0` and port `8080`.

This project can be used as a practical exercise to learn about building web applications using Python and Flask, integrating external APIs for translation purposes, and developing basic user interfaces for interacting with the application.

### Getting started
``` bash
pip install -r requirements.txt
python3 server.py
```

### Run tests
``` bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

