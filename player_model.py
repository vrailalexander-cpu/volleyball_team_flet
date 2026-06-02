import json
import os

from datetime import datetime
from typing import Optional

class PlayerModel:
    FILE_PATH = "storage/players.json"

    @classmethod
    def load_players(cls):
        try:
            if not os.path.exists(cls.FILE_PATH):
                with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
                    json.dump([], file)
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)

        except Exception as e:
            print(e)
            return []

    @classmethod
    def save_players(cls, players):
        try:
            with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(players, file, indent=4, ensure_ascii=False)

        except Exception as e:
            print(e)

    @classmethod
    def create_player(
        cls,
        name: str,
        number: str,
        position: Optional[str]
    ):

        players = cls.load_players()
        player = {
            "name": name,
            "number": number,
            "position": position,
            "created_at": datetime.now().strftime(
                "%d.%m.%Y %H:%M"
            )
        }
        players.append(player)
        cls.save_players(players)

    @classmethod
    def update_player(
        cls,
        index,
        new_data
    ):
        players = cls.load_players()
        if 0 <= index < len(players):
            players[index].update(new_data)
        cls.save_players(players)

    @classmethod
    def delete_player(cls, index):
        players = cls.load_players()
        if 0 <= index < len(players):
            players.pop(index)
        cls.save_players(players)