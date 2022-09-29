#!/usr/bin/env python3


""" Final Project - Flask Application
    Aaron Williams
    September, 29, 2022 """


# import all our flask objects
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

import requests

# used to render templates
from flask import render_template

import json

app = Flask(__name__)

test_pokemon = {
        "name": "charmander",
        "id": 4,
        "type": "fire",
        "height": 6,
        "weight": 85,
        "moves": [
            "fire-punch",
            "thunder-punch",
            "scratch"
        ],
    }

# moves
# pokemon["moves"][0..n]["move"]["name"]


# root directory api
# if the user calls the root / path
# then we return an example pokemon object
@app.route("/")
def index():
    # with open('example_pokemon.json') as ex_pokemon_file:
    #     example_pokemon = json.load(ex_pokemon_file)
    #
    #     print(type(example_pokemon))
    #     print(example_pokemon)

    # jsonify returns JSON object
    # return our test pokemon JSON object
    return jsonify(test_pokemon)


@app.route("/pokemon")
def pokemon_api():
    # define our api base url for the pokeapi
    POKEURL = "http://pokeapi.co/api/v2/pokemon/"
    # call the pokeapi
    pokemon = requests.get(f"{POKEURL}?limit=10")
    # convert the json object into a python dictionary
    pokemon = pokemon.json()

    return jsonify(pokemon)


@app.route("/pokemon/<name>")
def pokemon_lookup(name):
    # define our api base url for the pokeapi
    URL = "http://pokeapi.co/api/v2/pokemon/" + name
    # call the pokemon api
    pokemon = requests.get(f"{URL}?limit=10")

    # extract pokemon info and add to a new dictionary
    pokemon_info = {}

    # if our pokemon object is not empty
    if pokemon:
        # convert the json object into a python dictionary
        pokemon = pokemon.json()

        # add name
        pokemon_info["name"] = pokemon["name"]
        pokemon_info["type"] = pokemon["types"][0]["type"]["name"]
        pokemon_info["id"] = pokemon["id"]
        pokemon_info["height"] = pokemon["height"]
        pokemon_info["weight"] = pokemon["weight"]
        pokemon_info["moves"] = pokemon["moves"]

    return jsonify(pokemon_info)


# render a dynamic webpage that displays your favorite pokemon
@app.route("/favorite/<pokemon_name>")
def favorite_pokemon(pokemon_name):
    # render the template and add the favorite pokemon name
    return render_template("favorite_pokemon.html", favorite_pokemon_name = pokemon_name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)