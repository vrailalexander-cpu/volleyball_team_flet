from src.models.player_model import PlayerModel

class HomeController:
    @staticmethod
    def get_players():
        return PlayerModel.load_players()

    @staticmethod
    def create_player(
        name,
        number,
        position
    ):
        PlayerModel.create_player(
            name,
            number,
            position
        )

    @staticmethod
    def update_player(
        index,
        data
    ):

        PlayerModel.update_player(
            index,
            data
        )

    @staticmethod
    def delete_player(index):
        PlayerModel.delete_player(index)