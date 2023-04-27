from flask import Flask, render_template, request

import service

app = Flask(__name__)
app.config['DEBUG'] = True
TEMPLATES_AUTO_RELOAD = True


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/top-stats')
def top_stats():
    movies = service.get_top_stats()
    return render_template('top-stats.html', movies=movies)


@app.route('/transactions')
def transactions():
    transaction_list = service.get_transactions()
    return render_template('transactions.html', transactions=transaction_list)


@app.route('/search', methods=['POST'])
def search():
    searchq = request.form.get('searchMovie')
    movielist = service.search(searchq)
    return render_template('search.html', movies=movielist)


@app.route('/movie/<movie_id>')
def movie(movie_id):
    moviedict = service.get_movie(movie_id)
    return render_template('movie.html', movie=moviedict)


if __name__ == '__main__':
    app.run()
