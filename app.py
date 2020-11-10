from flask import Flask, escape, request, render_template
from bs4 import BeautifulSoup
import requests
import json
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


@app.route('/favorites')
def favorites():
    base_url = "http://www.omdbapi.com/"
    response = requests.get(base_url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find('title')

    # Read out favorited movies.
    filename = os.path.join('data.json')
    with open(filename) as data_file:
        data = json.load(data_file)
        return data
    return render_template('favorites.html')


@app.route('/search', methods=['POST'])
def search():
    """if POST, query movie api for data and return results."""
    query = request.form['title']
    return f'Hello, {query}!'


@app.route('/movie/<movie_id>')
def movie_detail():
    """if fetch data from movie database by oid and display info."""
    qs_name = request.args.get('name', '')
    qs_id = request.args.get('id', '')
    return f'Hello, {escape(name)}!'
