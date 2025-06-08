from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

FILE_DOMANDE = "domande.txt"

# Endpoint per la home
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint per aggiungere una domanda
@app.route('/aggiungi_domanda', methods=['POST'])
def aggiungi_domanda():
    domanda = request.form.get('domanda')  # Recupera la domanda dal form
    if domanda:
        with open(FILE_DOMANDE, "a", encoding="utf-8") as f:
            f.write(domanda + "\n")
        return jsonify({"success": True, "message": "Domanda aggiunta!"}), 200
    else:
        return jsonify({"success": False, "message": "Domanda vuota!"}), 400

# Endpoint per ottenere la lista delle domande
@app.route('/get_domande', methods=['GET'])
def get_domande():
    domande = []
    if os.path.exists(FILE_DOMANDE):
        with open(FILE_DOMANDE, "r", encoding="utf-8") as f:
            domande = [line.strip() for line in f]
    return jsonify({"domande": domande}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
