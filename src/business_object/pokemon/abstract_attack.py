from abc import ABC, abstractmethod

from business_object.statistic import Statistic


class AbstractAttack(ABC):
    "An attack possible for a pokemon"

    def __init__(self, power, name, description):
        self.power: int = power
        self.name: str = name
        self.description: str = description

    @abstractmethod
    def compute_damage(APkm, APkm) -> int:
        pass
