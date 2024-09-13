from business_object.pokemon.fixed_damage_attack import FixedDamageAttack


class TestFixedDamageAttack:
    def test_compute_damage(self):
        # GIVEN
        snorlax = FixedDamageAttack(power=5)

        # WHEN
        multiplier = snorlax.get_compute_damage()

        # THEN
        assert multiplier == 5


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
