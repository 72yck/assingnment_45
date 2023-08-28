from scene import Character
import random
def character_fight(type_1, type_2):
    character_1 = Character(type_1)
    character_2 = Character(type_2)
    coin_toss = random.randint(0, 1)
    if coin_toss == 0:
        first, second = [character_1, character_2]
    else:
        first, second = [character_2, character_1]

    while True:
        if attack_character(first, second):
            return str(first)
        if attack_character(second, first):
            return str(second)


def attack_character(first, second):
    damage = first.attack()
    second.take_damage(damage)
    if second.is_dead():
        return True
    return False

def main():
    char_1 = "fighter"
    char_1_win = 0
    char_2 = "thief"
    char_2_win = 0
    for _ in range(100):
        winner = character_fight(char_1, char_2)
        if winner == char_1:
            char_1_win += 1
        else:
            char_2_win += 1
    print("Results:")
    print(f"{char_1}: {char_1_win}")
    print(f"{char_2}: {char_2_win}")

if __name__ == "__main__":
    main()
