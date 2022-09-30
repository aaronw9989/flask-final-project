#!/usr/bin/env python3


""" Final Project - Flask Application
    Aaron Williams
    September, 29, 2022 """


import requests
from pprint import pprint
import os

# main method to execute our program
def main():
    print("Welcome to Aaron's Final Project!")

    # test empty path endpoint
    # this call does NOT depend on an external api
    print('NOTE: This is an example of what our pokemon query should return')
    test_empty_path_api()

    # test our pokemon lookup api
    # this allows us to lookup a pokemon with a given name
    test_pokemon_lookup()

    # test favorite pokemon endpoint
    favorite_pokemon_api()

    # Things to do:
    # add menu
    # clone project to tmux and test


def test_empty_path_api():
    # define our url
    URL = "http://127.0.0.1:2224/"
    # make api request to our endpoint
    test_pokemon = requests.get(URL).json()
    # display our returned pokemon
    display_pokemon_info(test_pokemon)


def test_pokemon_api():
    # endpoint of our pokemon api
    POKEMON_API = "http://127.0.0.1:2224/pokemon"
    # make a get request to our pokemon api
    test_pokemon = requests.get(POKEMON_API).json()
    # print out our pokemon
    pprint(test_pokemon)


def test_pokemon_lookup(name="squirtle"):
    # endpoint of our pokemon api
    POKEMON_LOOKUP_ENDPOINT = "http://127.0.0.1:2224/pokemon/" + name

    # make a get request to our pokemon api
    # and convert to a python dictionary object
    ret_pokemon = requests.get(POKEMON_LOOKUP_ENDPOINT).json()

    # print out our pokemon
    display_pokemon_info(ret_pokemon)

def favorite_pokemon_api(name="charizard"):
    # endpoint of our pokemon api
    POKEMON_API = "http://127.0.0.1:2224/favorite/" + name

    # create a webpage to display our favorite pokemon name
    # call the endpoint with the curl command
    os.system("curl " + POKEMON_API + " -L")


def display_pokemon_info(pokemon):
    name = pokemon["name"]
    name = name.capitalize()
    pokemon_id = pokemon["id"]
    pokemon_type = pokemon["type"]
    pokemon_type = pokemon_type.capitalize()
    height = pokemon["height"]
    weight = pokemon["weight"]
    moves = pokemon["moves"]

    print('----- POKEMON INFO -----')
    print(f'Name: {name}')
    print(f'ID: {pokemon_id}')
    print(f'Type: {pokemon_type}')
    print(f'Height: {height}')
    print(f'Weight: {weight}')
    print(f'Moves: ')
    for move in moves:
        print(f'\t {move}')
    print('------------------------')


if __name__ == "__main__":
    main()
