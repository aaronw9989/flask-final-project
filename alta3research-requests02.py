#!/usr/bin/env python3
""" Final Project Flask Application """


import requests
from pprint import pprint

URL= "http://127.0.0.1:2224/"

resp= requests.get(URL).json()

pprint(resp)


# endpoint of our pokemon api
POKEMON_API = "http://127.0.0.1:2224/pokemon"

# make a get request to our pokemon api
pokemon_response = requests.get(POKEMON_API).json()

# print the output of our request
pprint(pokemon_response)