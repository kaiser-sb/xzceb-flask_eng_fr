from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench/<textToTranslate>")
def englishToFrench(textToTranslate):
    textToTranslate = request.args.get('textToTranslate')
    
    return render_template(englishToFrench(textToTranslate))

@app.route("/frenchToEnglish/<textToTranslate>")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    
    return render_template(frenchToEnglish(textToTranslate))

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
