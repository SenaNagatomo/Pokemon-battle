from typing import List #型ヒントのリストを使うときに必要
from models.move import Move
from services.pokeapi import get_pokemon_data
import random

class Pokemon:
    def __init__(self, name_or_id: str):
        data = get_pokemon_data(name_or_id)

        self.name: str = data['name']
        self.id: int = data['id']
        self.image: str = data['sprites']['front_default']
        self.types: List[str] = [t['type']['name'] for t in data['types']]
        
        stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}
        self.stats = stats
        self.hp = stats['hp']
        self.attack = stats['attack']
        self.defense = stats['defense']
        self.sp_atk = stats['special-attack']
        self.sp_def = stats['special-defense']
        self.speed = stats['speed']

        move_names = [m['move']['name'] for m in data['moves']]
        self.move_names: List[str] = random.sample(move_names, 4) if len(move_names) >= 4 else move_names

    def summary(self):
        print(f"{self.name} (タイプ: {', '.join(self.types)})")
        print(f"HP: {self.hp} A: {self.attack} B: {self.defense} C: {self.sp_atk} D: {self.sp_def} S: {self.speed}")
        print("技:", self.move_names)