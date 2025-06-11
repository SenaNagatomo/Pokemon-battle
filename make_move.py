# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

import requests
x = 25
url = f"https://pokeapi.co/api/v2/pokemon/{x}/"

r = requests.get(url, timeout=5)
r = r.json()

name = r['name']
id = r['id']
image = r['sprites']['front_default']
types = r['types'][0]['type']['name']
stats = r['stats']
H = r['stats'][0]['base_stat']
A = r['stats'][1]['base_stat']
B = r['stats'][2]['base_stat']
C = r['stats'][3]['base_stat']
D = r['stats'][4]['base_stat']
S = r['stats'][5]['base_stat']
Stats = [H, A, B, C, D, S]

print(r['moves'][1]['move']['url'])
move_url = r['moves'][1]['move']['url']
s = requests.get(move_url, timeout=5)
s = s.json()

print(s)