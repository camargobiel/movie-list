import json

def write_database(movie, filename='database.json'):
  with open(filename, 'r+') as file:
    file_data = json.load(file)
    file_data['movies'].append(movie)

    file.seek(0)
    json.dump(file_data, file, indent=2)

def read_database():
  database = open('database.json')
  data = json.load(database)
  movies = data['movies']

  database.close()

  return movies

def remove_from_database(current_movie, filename='database.json'):
  with open(filename, 'r+') as file:
    file_data = json.load(file)

    if type(current_movie) is not dict:
      current_movie = current_movie.replace("\'", "\"")
    else:
      current_movie = json.dumps(current_movie)

    file_data['movies'].remove(json.loads(current_movie))

  with open(filename, 'w') as file:
    json.dump(file_data, file, indent=2)

def edit_database(current_movie, edited_movie, filename='database.json'):
  with open(filename, 'r+') as file:
    movies = json.load(file)
    movies = movies['movies']

    for movie in movies:
      print(movie)
      print(current_movie)
      if str(movie) == str(current_movie):
        remove_from_database(movie)
        write_database(edited_movie)
        return movie