from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
FILE_DOMANDE = "domande.txt"

def salva_domanda(domanda):
    with open(FILE_DOMANDE, "a", encoding="utf-8") as f:
        f.write(domanda + "\n")

def carica_domande():
    if os.path.exists(FILE_DOMANDE):
        with open(FILE_DOMANDE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    return []

def cancella_tutte():
    open(FILE_DOMANDE, "w", encoding="utf-8").close()

def cancella_domanda_singola(domanda):
    domande = carica_domande()
    domande = [d for d in domande if d != domanda]
    with open(FILE_DOMANDE, "w", encoding="utf-8") as f:
        for d in domande:
            f.write(d + "\n")

@app.route("/", methods=["GET"])
def index():
    domande = carica_domande()
    return render_template("index.html", domande=domande)

@app.route("/add", methods=["POST"])
def add_domanda():
    domanda = request.form.get("domanda", "").strip()
    if domanda:
        salva_domanda(domanda)
    return redirect(url_for("index"))

@app.route("/delete_all", methods=["POST"])
def delete_all():
    cancella_tutte()
    return redirect(url_for("index"))

@app.route("/delete_one", methods=["POST"])
def delete_one():
    domanda = request.form.get("domanda", "").strip()
    if domanda:
        cancella_domanda_singola(domanda)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
