from flask import Flask, render_template
from rottenonions.movie import MovieDatabase, Movie

app = Flask(__name__)


@app.route('/')
def route_root():
    md = MovieDatabase()
    movies = list()
    for i in md:
        movies.append(i)

    return render_template('home.html', movies=movies)


@app.route('/movie/<int:year>/<title>')
def route_movie(title, year):
    md = MovieDatabase()
    try:
        m = md.get(title, year)
        return render_template('movie.html', movie=m)
    except Exception:
        return render_template('404.html')
