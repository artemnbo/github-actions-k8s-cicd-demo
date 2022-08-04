from flask import Flask, render_template
from waitress import serve
from dotenv import load_dotenv
import requests
import logging
import os



app = Flask(__name__)


def get_imdb_top_10():
    url = f"https://imdb-api.com/en/API/Top250Movies/{os.environ.get('API_KEY')}"
    response = requests.get(url)
    data = response.json()

    return data['items'][:10]


@app.route('/')
def index():
    return render_template('index.html', movies=get_imdb_top_10())


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    load_dotenv(os.environ.get("DOTENV_CREDENTIALS_PATH")) 
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.INFO)
    serve(app, host="0.0.0.0", port=5000)
