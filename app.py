from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Path al file domande.txt
DOMANDE_FILE = 'domande.txt'

# Funzione per leggere le domande dal file
def read_questions():
    if not os.path.exists(DOMANDE_FILE):
        return []
    with open(DOMANDE_FILE, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

# Funzione per scrivere le domande nel file
def write_questions(questions):
    with open(DOMANDE_FILE, 'w', encoding='utf-8') as file:
        for question in questions:
            file.write(question + '\n')

@app.route('/')
def index():
    questions = read_questions()
    return render_template('index.html', questions=questions)

@app.route('/add', methods=['POST'])
def add_question():
    question = request.json.get('question')
    if question:
        questions = read_questions()
        questions.append(question)
        write_questions(questions)
    return jsonify({'status': 'success'})

@app.route('/delete', methods=['POST'])
def delete_question():
    question = request.json.get('question')
    questions = read_questions()
    if question in questions:
        questions.remove(question)
        write_questions(questions)
    return jsonify({'status': 'success'})

@app.route('/clear', methods=['POST'])
def clear_questions():
    write_questions([])  # Svuota il file
    return jsonify({'status': 'success'})

@app.route('/get-questions', methods=['GET'])
def get_questions():
    questions = read_questions()
    return jsonify({'questions': questions})

if __name__ == '__main__':
    app.run(debug=True)
