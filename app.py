from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

FILE_DOMANDE = "domande.txt"

# Funzione per caricare le domande dal file
def carica_domande():
    domande = []
    if os.path.exists(FILE_DOMANDE):
        with open(FILE_DOMANDE, "r", encoding="utf-8") as f:
            domande = [riga.strip() for riga in f if riga.strip()]
    return domande

# Funzione per aggiungere una nuova domanda
def salva_domanda(domanda):
    with open(FILE_DOMANDE, "a", encoding="utf-8") as f:
        f.write(domanda + "\n")

@app.route('/')
def index():
    domande = carica_domande()
    return render_template('index.html', domande=domande)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    nuova_domanda = request.form['domanda']
    if nuova_domanda:
        salva_domanda(nuova_domanda)
    return jsonify({'status': 'success', 'domanda': nuova_domanda})

if __name__ == "__main__":
    app.run(debug=True)
