from deep_translator import MyMemoryTranslator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated = MyMemoryTranslator(source='en', target='french').translate(textToTranslate)
    return translated

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated = MyMemoryTranslator(source='french', target='en').translate(textToTranslate)
    return translated

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
