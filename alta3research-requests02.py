#!/usr/bin/env python3
""" Final Project Flask Application """


import requests
from pprint import pprint


def main():
    print("Welcome to Aaron's Final Project!")
    test_pokemon_name_api()


def test_empty_path_api():
    # define our url
    URL = "http://127.0.0.1:2224/"
    # make api request to our endpoint
    resp = requests.get(URL).json()
    #display the results
    pprint(resp)


def test_pokemon_api():
    # endpoint of our pokemon api
    POKEMON_API = "http://127.0.0.1:2224/pokemon"
    # make a get request to our pokemon api
    pokemon_response = requests.get(POKEMON_API).json()
    # print the output of our request
    pprint(pokemon_response)


def test_pokemon_name_api():
    # endpoint of our pokemon api
    POKEMON_API_NAME = "http://127.0.0.1:2224/pokemon/squirtle"
    # make a get request to our pokemon api
    pokemon_name = requests.get(POKEMON_API_NAME).json()
    # print the output of our request
    # pprint(pokemon_name)

    #print(pokemon_name)
    name = pokemon_name["forms"][0]["name"]
    pokemon_name_type = pokemon_name["types"][0]["type"]["name"]
    print(f'Pokemon Name: {name}')
    print(f'Pokemon Type: {pokemon_name_type}')


if __name__ == "__main__":
    main()
