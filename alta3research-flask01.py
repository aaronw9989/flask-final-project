#!/usr/bin/env python3
"""DEMO: receiving JSON"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

import requests

app= Flask(__name__)

herodata= [{
    "name": "Spider-Man",
    "realName": "Peter Parker",
    "since": 1962,
    "powers": [
        "wall crawling",
        "web shooters",
        "spider senses",
        "super human strength & agility"
              ]
             }]

@app.route("/")
def index():
    # jsonify returns legal JSON
    return jsonify(herodata)

@app.route("/pokemon")
def pokemon_api():
    # define our api base url for the pokeapi
    POKEURL = "http://pokeapi.co/api/v2/pokemon/"

    # call the pokeapi
    pokemon = requests.get(f"{POKEURL}?limit=10")
    # convert the json object into a python dictionary
    pokemon = pokemon.json()

    print(pokemon)
    return pokemon


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)