hero_damage = 100


def double_damage():
    global hero_damage
    hero_damage += hero_damage


def disarmed():
    global hero_damage
    hero_damage //= 10


def power_potion():
    global hero_damage
    hero_damage += 100
