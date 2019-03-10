import sys
# DISCLAIMER #
# print('DISCLAIMER:\n'
#       'Wizards of the Coast, Dungeons & Dragons, D&D, and their logos are\n'
#       'trademarks of Wizards of the Coast LLC in the United States and other\n'
#       'countries. © 2019 Wizards. All Rights Reserved. I am not affiliated with,\n'
#       'endorsed, sponsored, or specifically approved by Wizards of the Coast LLC.\n'
#       'This is an open-source project and not for profit in any way.\n'
#       'More information can be found at: http://dnd.wizards.com/\n'
#       )
# print('#################################################################################\n')
print('\nWelcome, adventurer, to Dungeons & Dragons!\n')

player_info = {'race': 'human',
               'class': 'fighter',
               'background': 'folk hero'
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
                    'common'
                ],
                'proficiencies': {
                    'weapons': [],
                    'skills': [],
                },
                'resistances_immunities': [],
                'special': []
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



race_menu()
race_input = str(input('Select a race:\n'))

# RACE ASSIGNMENT #
while True:

    # dragonborn
    if race_input == 'd' or race_input == 'D':
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Dragonborn selected!')
            player_info['race'] = 'dragonborn'
            print(player_info)
            break
        else:
            print('Please select B or S.')

    # dwarf
    if race_input == 'w' or race_input == 'W':
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Dwarf selected!')
            player_info['race'] = 'dwarf'
            print(player_info)
            break
        else:
            print('Please select B or S.')

    # elf
    if race_input == 'e' or race_input == 'E':
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Elf selected!')
            player_info['race'] = 'elf'
            print(player_info)
            break
        else:
            print('Please select B or S.')

    # gnome
    if race_input == 'g' or race_input == 'G':
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Gnome selected!')
            player_info['race'] = 'gnome'
            print(player_info)
            break
        else:
            print('Please select B or S.')

    # half-elf
    if race_input == 'h' or race_input == 'H':
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Half-Elf selected!')
            player_info['race'] = 'half-elf'
            print(player_info)
            break
        else:
            print('Please select B or S.')

    # half-orc
    if race_input == 'r' or race_input == 'R':
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Half-Orc selected!')
            player_info['race'] = 'half-orc'
            print(player_info)
            break
        else:
            print('Please select B or S.')

    # halfling
    if race_input == 'l' or race_input == 'L':
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Halfling selected!')
            player_info['race'] = 'halfling'
            print(player_info)
            break
        else:
            print('Please select B or S.')

    # human
    if race_input == 'm' or race_input == 'M':
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Human selected!')
            player_info['race'] = 'human'
            print(player_info)
            break
        else:
            print('Please select B or S.')

    # tiefling
    if race_input == 't' or race_input == 'T':
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            race_menu()
            race_input = str(input('Select a race for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Tiefling selected!')
            player_info['race'] = 'tiefling'
            print(player_info)
            break
        else:
            print('Please select B or S.')


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
            class_menu()
            class_input = str(input('Select a class for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Fighter selected!')
            player_info['class'] = 'fighter'
            break
        else:
            print('Please select B or S.')

    # WIZARD
    elif class_input == 'w' or class_input == 'W':
        print(wizard_info)
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            class_menu()
            class_input = str(input('Select a class for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Wizard selected!')
            player_info['class'] = 'wizard'
            break
        else:
            print('Please select B or S.')

    # CLERIC
    elif class_input == 'c' or class_input == 'C':
        print(cleric_info)
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            class_menu()
            class_input = str(input('Select a class for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Cleric selected!')
            player_info['class'] = 'cleric'
            break
        else:
            print('Please select B or S.')

    # ROGUE
    elif class_input == 'r' or class_input == 'R':
        print(rogue_info)
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            class_menu()
            class_input = str(input('Select a class for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Rogue selected!')
            player_info['class'] = 'rogue'
            break
        else:
            print('Please select B or S.')

    # RANGER
    elif class_input == 'a' or class_input == 'A':
        print(ranger_info)
        back_or_select = str(input('Type B to go back or S to select this class:\n'))
        if back_or_select == 'b' or back_or_select == 'B':
            class_menu()
            class_input = str(input('Select a class for more information:\n'))
        elif back_or_select == 's' or back_or_select == 'S':
            print('Ranger selected!')
            player_info['class'] = 'ranger'
            break
        else:
            print('Please select B or S.')
    elif class_input == 'q' or class_input == 'Q':
        sys.exit()
    else:
        print('\nPlease select from the options below.\n')
        class_menu()
        class_input = str(input('Select a class for more information:\n'))

# CALCULATIONS #
# dragonborn
if player_info['race'] == 'dragonborn':
    player_stats['str'] += 2
    player_stats['cha'] += 1
    player_stats['languages'].append('draconic')

# dwarf
if player_info['race'] == 'dwarf':
    player_stats['con'] += 2
    player_stats['special'].append('darkvision')
    player_stats['resistances_immunities'].append('poison resist')
    player_stats['proficiencies'].append('poison resist')
    player_stats['languages'].append('dwarvish')

# elf
if player_info['race'] == 'elf':
    player_stats['dex'] += 2
    player_stats['special'].append('darkvision')
    player_stats['resistances_immunities'].append('sleep immunity')
    player_stats['proficiencies'].append('perception')

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
    player_stats['proficiencies'].append('intimidation')

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

print(player_stats)

# to add:
# draconic ancestry
