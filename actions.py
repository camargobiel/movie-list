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
    current_movie = current_movie.replace("\'", "\"")

    file_data['movies'].remove(json.loads(current_movie))

  with open(filename, 'w') as file:
    json.dump(file_data, file, indent=2)