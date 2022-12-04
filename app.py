from flask import Flask, render_template, request
import ast
import requests

app = Flask(__name__)

tasks = []

movies_types = ['Terror', 'Ação', 'Animação', 'Comédia', 'Romance', 'Drama']
movies_classification = ['L', '10', '12', '14', '16', '18']

@app.route('/')
def home():
  return render_template('home.html', tasks=tasks)

@app.route('/bye')
def bye():
  return 'bye'

@app.route('/create', methods=['POST'])
def create():
  movie_name = request.form['movie_name']
  movie_type = request.form['movie_type']
  movie_classification = request.form['movies_classification']

  task = { 'name': movie_name, 'movie_type': movie_type, 'movie_classification': movie_classification}
  tasks.append(task)
  return home()

@app.route('/go_to_create_page')
def go_to_create_page():
  return render_template('create_movie.html', movies_types=movies_types, movies_classification=movies_classification)

@app.route('/remove', methods=['POST'])
def remove():
  current_task = request.form['task']
  json_task = ast.literal_eval(current_task)
  tasks.remove(json_task)
  return home()

app.run(debug=True)
