class GameCharacter:

    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        if not isinstance(new_health, int):
            raise TypeError('Health must be an integer.')
        if new_health < 0:
            new_health = 0
            print('Health capped at 0.')
        if new_health > 100:
            new_health = 100
            print('Health capped at 100.')
        self._health = new_health
    
    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if not isinstance(new_mana, int):
            raise TypeError('Mana must be an integer.')
        if new_mana < 0:
            new_mana = 0
            print('Mana capped at 0.')
        if new_mana > 50:
            new_mana = 50
            print('Mana capped at 50.')
        self._mana = new_mana

    @property
    def level(self):
        return self._level

    def __str__(self):
        name = f'Name: {self.name}\n'
        level = f'Level: {self.level}\n'
        health = f'Health: {self.health}\n'
        mana = f'Mana: {self.mana}'
        return name + level + health + mana

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f'{self.name} leveled up to {self.level}!')