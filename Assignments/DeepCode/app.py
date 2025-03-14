from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import subprocess
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
db = SQLAlchemy(app)

# Database Models
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    example_input = db.Column(db.Text, nullable=False)
    example_output = db.Column(db.Text, nullable=False)

class Submission(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    question_id = db.Column(db.Integer, nullable=False)
    user_code = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(20), nullable=False)
    result = db.Column(db.Text)

# API Routes
@app.route('/api/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    return jsonify([{
        'id': q.id,
        'title': q.title,
        'description': q.description,
        'example_input': q.example_input,
        'example_output': q.example_output
    } for q in questions])

@app.route('/api/submit', methods=['POST'])
def submit_code():
    data = request.json
    question_id = data['question_id']
    user_code = data['code']
    language = data['language']

    # Save submission
    submission = Submission(
        question_id=question_id,
        user_code=user_code,
        language=language
    )
    db.session.add(submission)
    db.session.commit()

    # Run code
    if language == "python":
        result = run_python_code(user_code)
    else:
        result = "Language not supported"
    
    # Update result in database
    submission.result = result
    db.session.commit()

    return jsonify({'submission_id': submission.id, 'result': result})

def run_python_code(code):
    try:
        with open('temp_script.py', 'w') as file:
            file.write(code)

        result = subprocess.run(
            ['python3', 'temp_script.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5
        )
        return result.stdout.decode('utf-8') or result.stderr.decode('utf-8')
    except subprocess.TimeoutExpired:
        return "Code execution timed out"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
