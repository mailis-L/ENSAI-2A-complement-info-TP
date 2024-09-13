from business_object.pokemon.abstract_pokemon import AbstractPokemon


class Defender(AbstractPokemon):
    def __init__(self, stat_current, level=0, name=None):
        super().__init__(stat_current, level=0, name=None, type_pk="Défenseur")

    def get_pokemon_attack_coef(self):
        return 1 + (self.attack_current + self.defense_current) / 200
