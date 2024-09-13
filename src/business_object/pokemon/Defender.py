from abstractpokemon import AbstractPokemon


class Defender(AbstractPokemon):
    def get_pokemon_attack_coef(self):
        return 1 + (self.attack_current + self.defense_current) / 200
