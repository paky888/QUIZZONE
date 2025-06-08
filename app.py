from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
DOMANDE_FILE = "domande.txt"

@app.route('/')
def index():
    if os.path.exists(DOMANDE_FILE):
        with open(DOMANDE_FILE, 'r', encoding='utf-8') as f:
            questions = [line.strip() for line in f.readlines()]
    else:
        questions = []
    return render_template('index.html', questions=questions)

@app.route('/add', methods=['POST'])
def add_question():
    data = request.get_json()
    question = data.get('question', '').strip()
    if question:
        with open(DOMANDE_FILE, 'a', encoding='utf-8') as f:
            f.write(question + '\n')
        return jsonify({'status': 'ok', 'question': question})
    return jsonify({'status': 'error', 'message': 'Domanda mancante'}), 400

@app.route('/get-questions')
def get_questions():
    if os.path.exists(DOMANDE_FILE):
        with open(DOMANDE_FILE, 'r', encoding='utf-8') as f:
            questions = [line.strip() for line in f.readlines()]
    else:
        questions = []
    return jsonify({'questions': questions})

@app.route('/delete', methods=['POST'])
def delete_question():
    data = request.get_json()
    question_to_delete = data.get('question', '').strip()
    if os.path.exists(DOMANDE_FILE):
        with open(DOMANDE_FILE, 'r', encoding='utf-8') as f:
            questions = [line.strip() for line in f.readlines()]
        questions = [q for q in questions if q != question_to_delete]
        with open(DOMANDE_FILE, 'w', encoding='utf-8') as f:
            for q in questions:
                f.write(q + '\n')
    return jsonify({'status': 'ok'})

@app.route('/clear', methods=['POST'])
def clear_questions():
    open(DOMANDE_FILE, 'w', encoding='utf-8').close()
    return jsonify({'status': 'cleared'})

if __name__ == '__main__':
    app.run(debug=True)
