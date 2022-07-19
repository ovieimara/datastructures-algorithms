# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def calculate_damage():
    player_id = '23456'
    damage = 0
    hit_points_attacker = 10
    hit_points_defender = 12
    attack = 70
    attack_loss = math.ceil(hit_points_attacker/100 * attack)
    hit_points_loss = math.ceil(hit_points_attacker / 100 * hit_points_defender)
    #damage_val = math.ceil(attack / hit_points)
    attack_value = attack - attack_loss
    hit_points_after_damage = hit_points_defender - hit_points_loss
    min_damage = 0.5 * attack
    attack_value_after_damage = attack_value if attack_value >= min_damage else min_damage

    print(f'DEFENDER({player_id}) --> attack_value: {attack_value_after_damage}, hit_points : {hit_points_after_damage}')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    calculate_damage()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
