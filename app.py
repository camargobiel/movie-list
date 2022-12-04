from flask import Flask, render_template, request, redirect
import ast

movies = []
movies_types = ['Terror', 'Ação', 'Animação', 'Comédia', 'Romance', 'Drama']
movies_classification = ['L', '10', '12', '14', '16', '18']

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html', movies=movies)

@app.route('/create', methods=['POST'])
def create():
  movie_name = request.form['movie_name']
  movie_type = request.form['movie_type']
  movie_classification = request.form['movies_classification']

  movies.append({ 'name': movie_name, 'movie_type': movie_type, 'movie_classification': movie_classification})

  return redirect_to_home()

@app.route('/create_page')
def create_page():
  return render_template('create_movie.html', movies_types=movies_types, movies_classification=movies_classification)

@app.route('/remove', methods=['POST'])
def remove():
  current_task = request.form['task']
  json_task = ast.literal_eval(current_task)
  movies.remove(json_task)

  return redirect_to_home()

def redirect_to_home():
  return redirect('/', code=302)

app.run(debug=True)
