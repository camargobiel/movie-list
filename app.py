from flask import Flask, render_template, request, redirect
from actions import write_database, read_database, remove_from_database

movies = []
movies_types = ['Terror', 'Ação', 'Animação', 'Comédia', 'Romance', 'Drama']
movies_classification = ['L', '10', '12', '14', '16', '18']

app = Flask(__name__)

@app.route('/')
def home():
  movies = read_database()

  return render_template('home.html', movies=movies)

@app.route('/create', methods=['POST'])
def create():
  movie_name = request.form['movie_name']
  movie_type = request.form['movie_type']
  movie_classification = request.form['movies_classification']

  write_database({'name': movie_name, 'movie_type': movie_type, 'movie_classification': movie_classification})

  return redirect_to_home()

@app.route('/create_page')
def create_page():
  return render_template('create_movie.html', movies_types=movies_types, movies_classification=movies_classification)

@app.route('/remove', methods=['POST'])
def remove():
  current_movie = request.form['movie']
  movies = remove_from_database(current_movie)

  return redirect_to_home()

def redirect_to_home():
  return redirect('/', code=302)

app.run(debug=True)
