from flask import Flask, render_template

app = Flask(__name__)

tasks = [
  {
    'name': 'Estudar',
    'finished': False
  },
  {
    'name': 'Dormir',
    'finished': True
  }
]

@app.route('/')
def home():
  return render_template('home.html', tasks=tasks)

@app.route('/bye')
def bye():
  return 'bye'

app.run(debug=True)
