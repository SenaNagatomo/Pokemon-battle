from services.pokeapi import get_move_data

class Move:
    def __init__(self, name: str):
        data = get_move_data(name)

        self.name: str = data['name']
        self.type: str = data['type']['name']
        self.damage_class: str = data['damage_class']['name']
        self.power = data.get('power') or 0  #今のところ補助技はダメージ０として考える
        self.accuracy = data.get('accuracy', 100)

    def summary(self):
        print(f"{self.name} / タイプ: {self.type} / 区分: {self.damage_class} / 威力: {self.power} / 命中: {self.accuracy}")