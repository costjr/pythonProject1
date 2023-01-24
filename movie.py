import logging
import requests
import numpy as np
import pandas as pd
import random
import csv
from flask import Flask, request, jsonify, current_app
from scipy.stats import pearsonr

logging.basicConfig(level=logging.INFO)
PORT = 5000
HOST = 'localhost'
API_ENDPOINT= 'localhost:5000'
RATING_PATH = './data/rating.small.csv'
TITLE_PATH = './data/movie.csv'
LINK_PATH = './data/links.csv'

app = Flask(__name__)

def create_rating_matrix(path):
    df = pd.read_csv(path, sep=',', usecols=['userId', 'moviedId', 'rating'])
    df = df.pivot(index='userId', columns='moviedId', values='rating')
    df = df.fillna(value=0)
    return df.values, df.index.values, df.columns.values
def create_titles(path):
    df = pd.read_csv(path, sep=',', usecols=['movieId', 'title'])
    return df.values
def create_links(path):
    df = pd.read_csv(path, sep=',', usecols=['moviedId', 'imdbId'], dtype={'imdbId': str})
    return df.values

app.rating_matrix, app.users, app.movies = create_rating_matrix(RATING_PATH)
app.titles = create_titles(TITLE_PATH)
app.links = create_links(LINK_PATH)

temp = []
for title in app.titles:
     if title[0] in app.movies.tolist():
         temp.append(title)
app.titles = np.asarray(temp)

temp = []
for link in app.links:
     if link[0] in app.movies.tolist():
         temp.append(link)
app.links = np.asarray(temp)
del temp
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    chat_id = data['chat_id']
    if chat_id in current_app.users.tolist():
        return jsonify({'exists': 1})

    current_app.users = np.append(current_app.users, chat_id)

    current_app.rating_matrix = np.append(current_app.rating_matrix, np.zeros((1, current_app.rating_matrix.shape[1])), axis=0)
    return jsonify({'exists': 0})
@app.route('/get_unrated_movie', methods=['POST'])
def get_unrated_movie():
    data = request.json
    chat_id = data['chat_id']
    user_ratings = current_app.rating_matrix[np.where(current_app.users == chat_id)]
    movieId = current_app.movies[random.choice(np.where(usser_ratings= 0)[1])]

    title = current_app.titles[np.whre(current_app.titles == movieId)[0][0][1]]
    url = 'https://www.imdb.com/title/tt{}/'.format(current_app.links[np.where(current_app.links == movieId)[0]][0][1])
    return jsonify({
        'id': str(movieId),
        'title': title,
        'url': url
    })

@app.route('/rate_movie', methods=['POST'])
def rate_movie():
    data = request.json
    chat_id = data['chat_id']
    movieId = int(data['movieId'])
    rating = int(data['rating'])
    row = [str(chat_id), str(movieId), str(rating), 'N/A']
    with open(RATING_PATH, 'r') as readFile:
        reader = csv.reader(readFile)
        line = list(reader)[-1]
        if line != row:
            with open(RATING_PATH, 'a') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerow(row)
            writeFile.close()
        readFile.close()
        return jsonify({'status': 'succes'})