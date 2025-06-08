import tkinter as tk
import subprocess
import threading
import os

FILE_DOMANDE = "domande.txt"

def parla_testo(testo):
    def run():
        # Usa -r 150 per una lettura leggermente più lenta del normale
        subprocess.call(['say', '-r', '150', testo])
    threading.Thread(target=run).start()

def aggiungi_domanda():
    nuova_domanda = entry_domanda.get().strip()
    if nuova_domanda:
        crea_bottone_domanda(nuova_domanda)
        salva_domanda(nuova_domanda)
        entry_domanda.delete(0, tk.END)

def crea_bottone_domanda(domanda):
    btn = tk.Button(frame_domande, text=domanda, font=("Arial", 12), width=40,
                    command=lambda: parla_testo(domanda))
    btn.pack(pady=3)

def salva_domanda(domanda):
    with open(FILE_DOMANDE, "a", encoding="utf-8") as f:
        f.write(domanda + "\n")

def carica_domande():
    if os.path.exists(FILE_DOMANDE):
        with open(FILE_DOMANDE, "r", encoding="utf-8") as f:
            for riga in f:
                domanda = riga.strip()
                if domanda:
                    crea_bottone_domanda(domanda)

# GUI setup
root = tk.Tk()
root.title("QUIZZONE  RSD1A by PdS")
root.geometry("600x500")

label = tk.Label(root, text="Inserisci una nuova domanda", font=("Arial", 14))
label.pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack()

entry_domanda = tk.Entry(frame_input, font=("Arial", 12), width=40)
entry_domanda.pack(side=tk.LEFT, padx=5)

btn_aggiungi = tk.Button(frame_input, text="Aggiungi", command=aggiungi_domanda)
btn_aggiungi.pack(side=tk.LEFT)

frame_domande = tk.Frame(root)
frame_domande.pack(pady=20)

carica_domande()

root.mainloop()
