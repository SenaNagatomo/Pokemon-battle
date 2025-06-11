#ポケモンを作る
#ポケモンの名前、レベル、タイプ、実数値をクラスにまとめる
import random
import requests

class Make_pokemon:
    def __init__(self, x):
        self.x = x
        url = f"https://pokeapi.co/api/v2/pokemon/{x}/"
        r = requests.get(url, timeout=5)
        r = r.json()

        self.name = r['name']
        self.id = r['id']
        self.image = r['sprites']['front_default']
        self.type = r['types'][0]['type']['name']
        self.stats = r['stats']
        self.H = r['stats'][0]['base_stat']
        self.A = r['stats'][1]['base_stat']
        self.B = r['stats'][2]['base_stat']
        self.C = r['stats'][3]['base_stat']
        self.D = r['stats'][4]['base_stat']
        self.S = r['stats'][5]['base_stat']
        self.Stats = [self.H, self.A, self.B, self.C, self.D, self.S]
        self.moves = [None]
        for move_info in r["moves"]:
            move = move_info["move"]
            self.moves.append(move["name"])
        
        self.move_list = None
        

    def status(self):
        print("名前:", self.name, "タイプ:", self.type)
        print("HP:", self.H, "こうげき:", self.A, "ぼうぎょ:", self.B, "とくこう:", self.C, "とくぼう:", self.D, "すばやさ:", self.S)
        if self.move_list != None:
            print("技:", self.move_list[0].name, self.move_list[1].name, self.move_list[2].name, self.move_list[3].name)
        print(self.moves)

    def learning_move(self, move1, move2, move3, move4):
        self.move_list = [move1, move2, move3, move4]

#技を作る
class Make_move:
    def __init__(self, y):
        self.y = y
        url = f"https://pokeapi.co/api/v2/move/{y}/"
        r = requests.get(url, timeout=5)
        r = r.json()

        self.name = name
        self.type = type
        self.group = group
        self.power = power
        self.accuracy = accuracy

pikachu = Make_pokemon(25)
# none_move = Make_move("-", "-", "-", 0, 0)
# hinoko = Make_move("ひのこ", "ほのお", "とくしゅ", 40, 100)
# pikachu.learning_move(hinoko, none_move, none_move, none_move)
pikachu.status()