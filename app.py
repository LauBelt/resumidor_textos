import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from resumen_texto import Resumentexto

load_dotenv() 

app = Flask(__name__)
resumen_texto = Resumentexto(api_key=os.getenv("API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resumir', methods=['POST'])
def resumir():
    texto = request.form['texto']
    idioma = request.form['idioma']
    resumen = resumen_texto.resumen(texto, idioma)
    return render_template('resultado.html', resumen=resumen, idioma=idioma)

if __name__ == '__main__':
    app.run(debug=True)
