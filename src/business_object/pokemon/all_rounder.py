from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AllRounder(AbstractPokemon):
    def __init__(self, stat_current, level=0, name=None):
        super().__init__(stat_current, level=0, name=None, type_pk="Polyvalent")

    def get_pokemon_attack_coef(self):
        return 1 + (self.sp_atk_current + self.sp_def_current) / 200
