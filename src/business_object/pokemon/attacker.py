from abstract_pokemon import AbstractPokemon

class Attacker extend AbstractPokemon:
    public function get_pokemon_attack_coef(self){
        return 1 + (self.speed_current + self.attack_current) / 200
    }
