FIGHTER = {"health": 5, "attack": 3, "dodge": 2}
THIEF = {"health": 3, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}


TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}

import random
class Character:
    _health = 0
    _attack = 0
    _dodge = 0

    def __init__(self, char_type):
        self._char_type = char_type
        self._assign_attributes()

    def __str__(self):
        return self._char_type

    def _assign_attributes(self):
        type_dict = TYPES[self._char_type]
        self._health = type_dict["health"]
        self._attack = type_dict["attack"]
        self._dodge = type_dict["dodge"]

    def attack(self):
        return self._attack

    def take_damage(self, damage):
        if self._dodge_success():
            return "Missed!"
        self._health -= damage
        return f"{self._char_type} took {damage} damage."

    def _dodge_success(self):
        # Every point in dodge is 5% chance to dodge
        dodge_chance = self._dodge * 5
        dodge_roll = random.randint(1, 100)
        if dodge_roll <= dodge_chance:
            return True
        return False

    def is_dead(self):
        return self._health <= 0
