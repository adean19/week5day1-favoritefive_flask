from app import app
from flask import render_template

@app.route("/")
def home_page():
    pages = ['Video Games', 'Travel Destinations']
    return render_template('index.html', pages = pages)

@app.route("/video-games")
def videogames_page():
    ps_favorites = ['Final Fantasy', 'Tekken', 'Gran Turismo']
    nin_favorites = ['Fire Emblem', 'Pokemon', 'Super Smash Bros', 'Mario Kart']
    return render_template('video-games.html', ps_favorites = ps_favorites, nin_favorites = nin_favorites)

# @app.route("/travel-destinations")
# def traveldestinations_page():
#     return {
#         'North America': ['New York', 'San Francisco', 'Seattle'],
#         'Europe' : ['London', 'Paris'],
#         'Asia' : ['Tokyo', 'Kyoto', 'Osaka']
#     }