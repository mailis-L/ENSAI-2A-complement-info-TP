from business_object.pokemon.all_rounder import AllRounder
from business_object.statistic import Statistic


class TestAllRounderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = AllRounder(stat_current=Statistic(attack=100, defense=100))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 1


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
