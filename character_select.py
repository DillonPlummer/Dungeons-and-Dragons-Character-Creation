import sys
import os

# VARIABLES #
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# DISCLAIMER #
clear_screen()
# print('DISCLAIMER:\n'
#       'Wizards of the Coast, Dungeons & Dragons, D&D, and their logos are\n'
#       'trademarks of Wizards of the Coast LLC in the United States and other\n'
#       'countries. © 2019 Wizards. All Rights Reserved. I am not affiliated with,\n'
#       'endorsed, sponsored, or specifically approved by Wizards of the Coast LLC.\n'
#       'This is an open-source project and not for profit in any way.\n'
#       'More information can be found at: http://dnd.wizards.com/\n'
#       )
# print('#################################################################################\n')

# PROGRAM #
print('@!!!####################################################!!!@')
print('@!##### WELCOME, ADVENTURER, TO DUNGEONS & DRAGNONS! #####!@')
print('@!!!####################################################!!!@\n')

player_info = {'race': '',
               'subrace': '',
               'class': '',
               'background': '',
               }

player_stats = {'hp': 10,
                'ac': 0,
                'str': 0,
                'dex': 0,
                'con': 0,
                'int': 0,
                'wis': 0,
                'cha': 0,
                'languages': [
                    'common',
                ],
                'proficiencies': {
                    'weapons': [],
                    'skills': [],
                },
                'resistances_immunities': [],
                'special': [],
                }


# RACE MENU #
def race_menu():
    print('\nCHOOSE WISELY')
    print('\nRaces:')
    print('D - Dragonborn')
    print('W - Dwarf')
    print('E - Elf')
    print('G - Gnome')
    print('H - Half-Elf')
    print('R - Half-Orc')
    print('L - Halfling')
    print('M - Human')
    print('T - Tiefling')

# DRACONIC ANCESTRY MENU #
def ancestry_menu():
    print('\nCHOOSE WISELY')
    print('\nDraconic Ancestry:')
    print('B - Black Dragon')
    print('L - Blue Dragon')
    print('R - Brass Dragon')
    print('O - Bronze Dragon')
    print('C - Copper Dragon')
    print('G - Gold Dragon')
    print('E - Green Dragon')
    print('S - Silver Dragon')
    print('W - White Dragon')

# RACE INFO #
dragonborn_info = '\nTHE DRAGONBORN:\n'\
                  'Dragonborn look very much like dragons standing upright\n' \
                  'in humanoid form, though they lack wings or a tail. To any\n' \
                  'dragonborn, the clan is more important than life itself.\n' \
                  'Dragonborn owe their devotion and respect to their clan above\n' \
                  'all else, even the gods. Each dragonborn’s conduct reflects\n' \
                  'on the honor of his or her clan, and bringing dishonor to the\n' \
                  'clan can result in expulsion and exile. Each dragonborn knows\n' \
                  'his or her station and duties within the clan, and honor\n' \
                  'demands maintaining the bounds of that position.\n'

dwarf_info = '\nTHE DWARF:\n' \
             'Bold and hardy, dwarves are known as skilled warriors,\n' \
             'miners, and workers of stone and metal. Though they\n' \
             'stand well under 5 feet tall, dwarves are so broad and\n' \
             'compact that they can weigh as much as a human standing\n' \
             'nearly two feet taller. Their courage and endurance are\n' \
             'also easily a match for any of the larger folk.\n'

elf_info = '\nTHE ELF:\n' \
           'Elves are a magical people of otherworldly grace, living\n' \
           'in the world, but not entirely part of it. They live in\n' \
           'places of ethereal beauty, in the midst of ancient forests,\n' \
           'or in silvery spires glittering with faerie light, where\n' \
           'soft music drifts through the air and gentle fragrances waft\n' \
           'on the breeze. Elves love nature and magic, art and artistry,\n' \
           'music and poetry and the good things of the world.\n'

gnome_info = '\nTHE GNOME:\n' \
             'A constant hum of busy activity pervades the warrens and\n' \
             'neighborhoods where gnomes form their close-knit communities.\n' \
             'Louder sounds punctuate the hum: a crunch of grinding gears here,\n' \
             ' a minor explosion there, a yelp of surprise or triumph, and\n' \
             'especially bursts of laughter. Gnomes take delight in life,\n' \
             'enjoying every moment of invention, exploration, investigation,\n' \
             'creation, and play.\n'

half_elf_info = '\nTHE HALF_ELF:\n' \
                'Walking in two worlds but truly belonging to neither, half-elves combine\n' \
                'what some say are the best qualities of their elf and human parents: human\n' \
                'curiosity, inventiveness, and ambition tempered by the refined senses, love of\n' \
                'nature, and artistic tastes of the elves. Some half-elves live among humans,\n' \
                'set apart by their emotional and physical differences, watching friends and loved\n' \
                'ones age while time barely touches them. Others live with the elves, growing\n' \
                'restless as they reach adulthood in the timeless elven realms, while their peers\n' \
                'continue to live as children. Many half-elves, unable to fit into either society,\n' \
                'choose lives of solitary wandering or join with other misfits and outcasts in the\n' \
                'adventuring life.\n'

halfling_info = '\nTHE HALFLING:\n' \
                'The comforts of home are the goals of most halflings’ lives: a place to settle in\n' \
                'peace and quiet, far from marauding monsters and clashing armies; a blazing fire and a\n' \
                'generous meal; fine drink and fine conversation. Though some halflings live out their\n' \
                'days in remote agricultural communities, others form nomadic bands that travel constantly,\n' \
                'lured by the open road and the wide horizon to discover the wonders of new lands and\n' \
                'peoples. But even these wanderers love peace, food, hearth, and home, though home might\n' \
                'be a wagon jostling along a dirt road or a raft floating downriver.\n'

half_orc_info = '\nTHE HALF-ORC:\n' \
                'Whether united under the leadership of a mighty warlock or having fought to a standstill\n' \
                'after years of conflict, orc and human tribes sometimes form alliances, joining forces\n' \
                'into a larger horde to the terror of civilized lands nearby. When these alliances are\n' \
                'sealed by marriages, half-orcs are born. Some half-orcs rise to become proud chiefs of\n' \
                'orc tribes, their human blood giving them an edge over their full-blooded orc rivals. Some\n' \
                'venture into the world to prove their worth among humans and other more civilized races.\n' \
                'Many of these become adventurers, achieving greatness for their mighty deeds and notoriety\n' \
                'for their barbaric customs and savage fury.\n'

human_info = '\nTHE HUMAN:\n' \
             'In the reckonings of most worlds, humans are the youngest of the common races, late to arrive\n' \
             'on the world scene and short-lived in comparison to dwarves, elves, and dragons. Perhaps it\n' \
             'is because of their shorter lives that they strive to achieve as much as they can in the years\n' \
             'they are given. Or maybe they feel they have something to prove to the elder races, and that’s\n' \
             'why they build their mighty empires on the foundation of conquest and trade. Whatever drives them,\n' \
             'humans are the innovators, the achievers, and the pioneers of the worlds.\n'

tiefling_info = '\nTHE TIEFLING:\n' \
                'To be greeted with stares and whispers, to suffer violence and insult on the street, to see\n' \
                'mistrust and fear in every eye: this is the lot of the tiefling. And to twist the knife,\n' \
                'tieflings know that this is because a pact struck generations ago infused the essence of\n' \
                'Asmodeus—overlord of the Nine Hells—into their bloodline. Their appearance and their nature are\n' \
                'not their fault but the result of an ancient sin, for which they and their children and their\n' \
                'children’s children will always be held accountable.\n'

clear_screen()
race_menu()
race_input = str(input('Select a race:\n'))

# RACE ASSIGNMENT #
while True:

    # dragonborn
    if race_input == 'd' or race_input == 'D':
        print(dragonborn_info)
        back_or_select = str(input('Type B to go back or S to select this race:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            player_info['race'] = 'dragonborn'
            print('Dragonborn selected!')

            # DRACONIC ANCESTRY MENU #
            ancestry_menu()
            ancestry_input = str(input('Select an ancestry:\n'))
            while True:

                # black
                if ancestry_input == 'b' or ancestry_input == 'B':
                    back_or_select = str(input('Type B to go back or S to select this ancestry:\n'))
                    if back_or_select == 'b' or back_or_select == 'B':
                        clear_screen()
                        ancestry_menu()
                        ancestry_input = str(input('Select a ancestry for more information:\n'))
                    elif back_or_select == 's' or back_or_select == 'S':
                        clear_screen()
                        print('Black dragon ancestry selected!')
                        player_info['subrace'] = 'black dragon'
                        break

                # blue
                elif ancestry_input == 'l' or ancestry_input == 'L':
                    back_or_select = str(input('Type B to go back or S to select this ancestry:\n'))
                    if back_or_select == 'b' or back_or_select == 'B':
                        clear_screen()
                        ancestry_menu()
                        ancestry_input = str(input('Select a ancestry for more information:\n'))
                    elif back_or_select == 's' or back_or_select == 'S':
                        clear_screen()
                        print('Blue dragon ancestry selected!')
                        player_info['subrace'] = 'blue dragon'
                        break

                # brass
                elif ancestry_input == 'r' or ancestry_input == 'R':
                    back_or_select = str(input('Type B to go back or S to select this ancestry:\n'))
                    if back_or_select == 'b' or back_or_select == 'B':
                        clear_screen()
                        ancestry_menu()
                        ancestry_input = str(input('Select a ancestry for more information:\n'))
                    elif back_or_select == 's' or back_or_select == 'S':
                        clear_screen()
                        print('Brass dragon ancestry selected!')
                        player_info['subrace'] = 'brass dragon'
                        break

                # bronze
                elif ancestry_input == 'o' or ancestry_input == 'O':
                    back_or_select = str(input('Type B to go back or S to select this ancestry:\n'))
                    if back_or_select == 'b' or back_or_select == 'B':
                        clear_screen()
                        ancestry_menu()
                        ancestry_input = str(input('Select a ancestry for more information:\n'))
                    elif back_or_select == 's' or back_or_select == 'S':
                        clear_screen()
                        print('Bronze dragon ancestry selected!')
                        player_info['subrace'] = 'bronze dragon'
                        break

                # copper
                elif ancestry_input == 'c' or ancestry_input == 'C':
                    back_or_select = str(input('Type B to go back or S to select this ancestry:\n'))
                    if back_or_select == 'b' or back_or_select == 'B':
                        clear_screen()
                        ancestry_menu()
                        ancestry_input = str(input('Select a ancestry for more information:\n'))
                    elif back_or_select == 's' or back_or_select == 'S':
                        clear_screen()
                        print('Copper dragon ancestry selected!')
                        player_info['subrace'] = 'copper dragon'
                        break

                # gold
                elif ancestry_input == 'g' or ancestry_input == 'G':
                    back_or_select = str(input('Type B to go back or S to select this ancestry:\n'))
                    if back_or_select == 'b' or back_or_select == 'B':
                        clear_screen()
                        ancestry_menu()
                        ancestry_input = str(input('Select a ancestry for more information:\n'))
                    elif back_or_select == 's' or back_or_select == 'S':
                        clear_screen()
                        print('Gold dragon ancestry selected!')
                        player_info['subrace'] = 'gold dragon'
                        break

                # green
                elif ancestry_input == 'e' or ancestry_input == 'E':
                    back_or_select = str(input('Type B to go back or S to select this ancestry:\n'))
                    if back_or_select == 'b' or back_or_select == 'B':
                        clear_screen()
                        ancestry_menu()
                        ancestry_input = str(input('Select a ancestry for more information:\n'))
                    elif back_or_select == 's' or back_or_select == 'S':
                        clear_screen()
                        print('Green dragon ancestry selected!')
                        player_info['subrace'] = 'green dragon'
                        break

                # silver
                elif ancestry_input == 's' or ancestry_input == 'S':
                    back_or_select = str(input('Type B to go back or S to select this ancestry:\n'))
                    if back_or_select == 'b' or back_or_select == 'B':
                        clear_screen()
                        ancestry_menu()
                        ancestry_input = str(input('Select a ancestry for more information:\n'))
                    elif back_or_select == 's' or back_or_select == 'S':
                        clear_screen()
                        print('Silver dragon ancestry selected!')
                        player_info['subrace'] = 'silver dragon'
                        break

                # white
                elif ancestry_input == 'w' or ancestry_input == 'W':
                    back_or_select = str(input('Type B to go back or S to select this ancestry:\n'))
                    if back_or_select == 'b' or back_or_select == 'B':
                        clear_screen()
                        ancestry_menu()
                        ancestry_input = str(input('Select a ancestry for more information:\n'))
                    elif back_or_select == 's' or back_or_select == 'S':
                        clear_screen()
                        print('White dragon ancestry selected!')
                        player_info['subrace'] = 'white dragon'
                        break
                else:
                    clear_screen()
                    print('\nPlease select from the options below.\n')
                    ancestry_menu()
                    ancestry_input = str(input('Select an ancestry for more information:\n'))
        else:
            clear_screen()
            print('Please select B or S.')
        break

    # dwarf
    if race_input == 'w' or race_input == 'W':
        print(dwarf_info)
        back_or_select = str(input('Type B to go back or S to select this race:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Dwarf selected!')
            player_info['race'] = 'dwarf'
            break
        else:
            clear_screen()
            print('Please select B or S.')

    # elf
    if race_input == 'e' or race_input == 'E':
        print(elf_info)
        back_or_select = str(input('Type B to go back or S to select this race:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Elf selected!')
            player_info['race'] = 'elf'
            break
        else:
            clear_screen()
            print('Please select B or S.')

    # gnome
    if race_input == 'g' or race_input == 'G':
        print(gnome_info)
        back_or_select = str(input('Type B to go back or S to select this race:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Gnome selected!')
            player_info['race'] = 'gnome'
            break
        else:
            clear_screen()
            print('Please select B or S.')

    # half-elf
    if race_input == 'h' or race_input == 'H':
        print(half_elf_info)
        back_or_select = str(input('Type B to go back or S to select this race:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Half-Elf selected!')
            player_info['race'] = 'half-elf'
            break
        else:
            clear_screen()
            print('Please select B or S.')

    # half-orc
    if race_input == 'r' or race_input == 'R':
        print(half_orc_info)
        back_or_select = str(input('Type B to go back or S to select this race:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Half-Orc selected!')
            player_info['race'] = 'half-orc'
            break
        else:
            clear_screen()
            print('Please select B or S.')

    # halfling
    if race_input == 'l' or race_input == 'L':
        print(halfling_info)
        back_or_select = str(input('Type B to go back or S to select this race:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Halfling selected!')
            player_info['race'] = 'halfling'
            break
        else:
            clear_screen()
            print('Please select B or S.')

    # human
    if race_input == 'm' or race_input == 'M':
        print(human_info)
        back_or_select = str(input('Type B to go back or S to select this race:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Human selected!')
            player_info['race'] = 'human'
            break
        else:
            clear_screen()
            print('Please select B or S.')

    # tiefling
    if race_input == 't' or race_input == 'T':
        print(tiefling_info)
        back_or_select = str(input('Type B to go back or S to select this race:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Tiefling selected!')
            player_info['race'] = 'tiefling'
            break
        else:
            clear_screen()
            print('Please select B or S.')
    else:
        clear_screen()
        print('\nPlease select from the options below.\n')
        race_menu()
        race_input = str(input('Select a race for more information:\n'))


# CLASS INFO #
fighter_info = '\nTHE FIGHTER:\n' \
               'Questing knights, conquering overlords, royal champions,\n' \
               'elite foot soldiers, hardened mercenaries, and bandit kings—-as\n' \
               'fighters, they all share an unparalleled mastery with weapons\n' \
               'and armor, and a thorough knowledge of the skills of combat.\n'

wizard_info = '\nTHE WIZARD:\n' \
              'Drawing on the subtle weave of magic that permeates the cosmos,\n' \
              'wizards cast spells of explosive fire, arcing lightning, subtle\n' \
              'deception, and brute-force mind control.\n'

cleric_info = '\nTHE CLERIC:\n' \
              'Clerics are intermediaries between the mortal world and the\n' \
              'distant planes of the gods. As varied as the gods they serve,\n' \
              'they strive to embody the handiwork of their deities.\n'

rogue_info = '\nTHE ROGUE:\n' \
             'Rogues rely on skill, stealth, and their foes’ vulnerabilities\n' \
             'to get the upper hand in any situation. They have a knack for\n' \
             'finding the solution to just about any problem, bringing\n' \
             'resourcefulness and versatility to their adventuring parties.\n'

ranger_info = '\nTHE RANGER:\n' \
              'Far from the bustle of cities and towns, amid the dense-packed\n' \
              'trees of trackless forests and across wide and empty plains,\n' \
              'rangers keep their unending watch.\n'


# CLASS MENU #
def class_menu():
    print('\nCHOOSE WISELY')
    print('\nClasses:')
    print('F - fighter')
    print('W - wizard')
    print('C - cleric')
    print('R - rogue')
    print('A - ranger')
    print('Q - quit\n')


class_menu()
class_input = str(input('Select a class for more information:\n'))

# CLASS ASSIGNMENT #
while True:

    # FIGHTER
    if class_input == 'f':
        print(fighter_info)
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            class_menu()
            class_input = str(input('Select a class for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Fighter selected!')
            player_info['class'] = 'fighter'
            break
        else:
            clear_screen()
            print('Please select B or S.')

    # WIZARD
    elif class_input == 'w' or class_input == 'W':
        print(wizard_info)
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            class_menu()
            class_input = str(input('Select a class for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Wizard selected!')
            player_info['class'] = 'wizard'
            break
        else:
            clear_screen()
            print('Please select B or S.')

    # CLERIC
    elif class_input == 'c' or class_input == 'C':
        print(cleric_info)
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            class_menu()
            class_input = str(input('Select a class for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Cleric selected!')
            player_info['class'] = 'cleric'
            break
        else:
            clear_screen()
            print('Please select B or S.')

    # ROGUE
    elif class_input == 'r' or class_input == 'R':
        print(rogue_info)
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            class_menu()
            class_input = str(input('Select a class for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Rogue selected!')
            player_info['class'] = 'rogue'
            break
        else:
            clear_screen()
            print('Please select B or S.')

    # RANGER
    elif class_input == 'a' or class_input == 'A':
        print(ranger_info)
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            clear_screen()
            class_menu()
            class_input = str(input('Select a class for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            clear_screen()
            print('Ranger selected!')
            player_info['class'] = 'ranger'
            break
        else:
            clear_screen()
            print('Please select B or S.')

    # QUIT
    elif class_input == 'q' or class_input == 'Q':
        sys.exit()

    else:
        clear_screen()
        print('\nPlease select from the options below.\n')
        class_menu()
        class_input = str(input('Select a class for more information:\n'))


# CALCULATIONS #
# dragonborn
if player_info['race'] == 'dragonborn':
    player_stats['str'] += 2
    player_stats['cha'] += 1
    player_stats['special'].append('breath weapon')
    player_stats['languages'].append('draconic')

# dwarf
if player_info['race'] == 'dwarf':
    player_stats['con'] += 2
    player_stats['special'].append('darkvision')
    player_stats['resistances_immunities'].append('poison resist')
    player_stats['languages'].append('dwarvish')

# elf
if player_info['race'] == 'elf':
    player_stats['dex'] += 2
    player_stats['special'].append('darkvision')
    player_stats['resistances_immunities'].append('sleep immunity')
    player_stats['proficiencies']['skills'].append('perception')

# gnome
if player_info['race'] == 'gnome':
    player_stats['int'] += 2
    player_stats['special'].append('darkvision')

# half-elf
if player_info['race'] == 'half-elf':
    player_stats['cha'] += 2
    player_stats['special'].append('darkvision')

# half-orc
if player_info['race'] == 'half-orc':
    player_stats['str'] += 2
    player_stats['con'] += 1
    player_stats['special'].append('darkvision')
    player_stats['proficiencies']['skills'].append('intimidation')

# human = N/A
if player_info['race'] == 'human':
    player_stats['str'] += 1
    player_stats['dex'] += 1
    player_stats['con'] += 1
    player_stats['int'] += 1
    player_stats['wis'] += 1
    player_stats['cha'] += 1

# halfling
if player_info['race'] == 'halfling':
    player_stats['dex'] += 2

# tiefling
if player_info['race'] == 'tiefling':
    player_stats['int'] += 1
    player_stats['cha'] += 2
    player_stats['special'].append('darkvision')
    player_stats['resistances_immunities'].append('fire resist')

print('\n')
for key, value in player_info.items():
    print(key, ':', value, '\n', end='')



######################################################################################
#################################### TO DO LIST ######################################
######################################################################################
# FIX - looping back to race menu after re-selecting same race - #
# i.e., select dragonborn, press B, select dragonborn again, and
# it re- displays the race select menu and prompts you to "select
# from the options below" -- maybe a problem with the break statement?

# add subraces
# add abilities/stats of subraces
