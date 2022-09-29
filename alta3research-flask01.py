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

# used to import json objects into our program
import json

app = Flask(__name__)


# if the user calls the root / path
# then we return an example pokemon object
# we do this to show our program works if the pokemon api is down
@app.route("/")
def index():
    # open our json file and read it as a string
    with open('test_pokemon.json', 'r') as pokemon_file:
        pokemon_string = pokemon_file.read()

    # create a python dictionary from the string
    pokemon_dic = json.loads(pokemon_string)

    # convert the pokemon into a json object and return
    return jsonify(pokemon_dic)


# call the pokemon api url
# used to test the pokemon api mostly for troublshooting
@app.route("/pokemon")
def pokemon_api():
    # define our api base url for the pokeapi
    POKEURL = "http://pokeapi.co/api/v2/pokemon/"
    # call the pokeapi
    pokemon = requests.get(f"{POKEURL}?limit=10")
    # convert the json object into a python dictionary
    pokemon = pokemon.json()
    # convert into json and return
    return jsonify(pokemon)


# query the pokemon api with a given name
@app.route("/pokemon/<name>")
def pokemon_lookup(name):
    # define our api base url for the pokeapi
    URL = "http://pokeapi.co/api/v2/pokemon/" + name

    # call the pokemon api
    pokemon = requests.get(f"{URL}")

    # extract pokemon info and add to a new dictionary
    pokemon_info = {}

    # if our pokemon object is not empty
    if pokemon:
        # convert the json object into a python dictionary
        pokemon = pokemon.json()

        # add all the info we want to return to a dictionary
        pokemon_info["name"] = pokemon["name"]
        pokemon_info["type"] = pokemon["types"][0]["type"]["name"]
        pokemon_info["id"] = pokemon["id"]
        pokemon_info["height"] = pokemon["height"]
        pokemon_info["weight"] = pokemon["weight"]

        # grab the move names from our pokemon object and add it to a list
        # pokemon["moves"][0..n]["move"]["name"]
        moves = []
        for curr in pokemon["moves"]:
            move = curr["move"]["name"]
            moves.append(move)

        # if more than five moves than just add the first five
        if len(moves) > 5:
            # add first five moves
            pokemon_info["moves"] = moves[0:5]
        else:
            # otherwise add entire list of moves
            pokemon_info["moves"] = moves

    # return our pokemon info
    return jsonify(pokemon_info)


# Create a webpage that displays your favorite pokemon
@app.route("/favorite/<pokemon_name>")
def favorite_pokemon(pokemon_name):
    # render the template and add the favorite pokemon name
    return render_template("favorite_pokemon.html", favorite_pokemon_name = pokemon_name)


# main method
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)