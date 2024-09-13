from business_object.pokemon.abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def __init__(self, power, name=None, description=None):
        super().__init__(power, name=None, description=None)

    def compute_damage(APkm, APkm) -> int:
        return self.power
