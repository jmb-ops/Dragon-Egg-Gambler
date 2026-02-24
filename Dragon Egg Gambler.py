'''Dragon Egg Gambler
'''
import random

gold = 0
loot = []

def tbd():
    '''this function needs to provide the randomness for which
the egg either gives gold, if so how much? or it gives a special
item such as: armor, more gold, gems or other such treasures,
or deals death.'''
    global gold
    global loot
    #random number generated below to determine 1 of 3 possible
    #actions to take.
    tap_egg = random.randrange(100)
    #print(tap_egg)
    if 1 <= tap_egg <= 75:
        #give gold
        #print(tap_egg,'gold')
        amt = random.randrange(1, 13)
        print('tap! tap!!')
        print(f'You found + {amt} gold!')
        gold += amt
    elif 76 <= tap_egg <= 95:
        #give item
        #print(tap_egg, 'item')
        item = random.choice(['armor', 'pearls', 'diamonds', 'Crown of a Fallen King',
                       'Polished Coins', 'Glass Baubles',
                       'Shiny Buttons', 'Beads & Trinkets',
                       'Ember Eater Amulet (magic)',
                       'Fire Quenched Stone (magic)',
                       'Half Melted Knight Helmet', 'Silver Bracelets',
                       'Gem Shards',])
        print('tap! tap!!')
        print(f'You found + {item}!')
        loot.append(item)
    elif 96 <= tap_egg <= 100:
        #death option
        #print(tap_egg, 'death')
        print('tap! tap!!')
        print('A loud crack echoes as the egg breaks open.')
        if 'armor' in loot:
            loot.remove('armor')
            print('The dragon’s fire slams into your armor '
            '— it chars, and breaks, but saves your life.')
            main()
        elif 'Ember Eater Amulet (magic)' in loot:
            loot.remove('Ember Eater Amulet (magic)')
            print('Your Ember Eater Amulet drinks the flames '
            'greedily, then crumbles to ash. You survive.')
            main()
        elif 'Fire Quenched Stone (magic)' in loot:
            loot.remove('Fire Quenched Stone (magic)')
            print('Your Fire Quenched Stone cracks apart as it '
            'drinks the heat meant for you. You survive.')
            main()
        elif 'Half Melted Knight Helmet' in loot:
            loot.remove('Half Melted Knight Helmet')
            print('It’s ugly, it’s warped, but the knight’s '
            'helmet blocks the blast one last time. You survive.')
            main()
        else:
            print('The newborn’s fire engulfs you completely, '
            'melting you into nothing.')
            exit()
    
def main():
    #tbd()
    #print for debugging
    print('[T]ap egg or [C]ash out')
    player = input('Player 1: ')
    while player != 'q':
        if player == 't':
            #print('gold=', gold, 'loot=', loot)
            tbd()
        elif player == 'c':
            #write score to disk
            #print(f'Player 1 score: gold = {gold} \
            #loot = {loot}')
            with open('highscore.txt', 'w') as f:
                save_name = input('enter name for '
                'highscore: ')
                print(f'{save_name} escapes with {gold} '
                f'gold and {len(loot)} looted items: {loot}')
                saved = save_name, gold, loot
                f.write(str(saved))
                exit()
        elif player == 'i':
            print(f'Player 1 score: gold = {gold} '
            f'loot = {loot}')
        elif player == 'highscore':
            with open('highscore.txt', 'r') as f:
                data = f.read()
                print(data)
        elif player == '?':
            print('(press i for score & highscore'
                  ' to see the highscore, t to tap'
                ' the egg, c to cash out, q to quit.')
        print('[T]ap egg or [C]ash out')
        player = input('Player 1: ')
    
if __name__ == "__main__":
    print('Dragon nests are rare, dangerous, and '
          'overflowing with treasure. \nYou’ve found '
          'one... A massive egg resting atop a glittering '
          'hoard. \nEvery tap risks waking what guards it.'
          '\npress ? for more info.')
    main()
