'''Dragon Egg Gambler
'''
import random
#game items.
gold = 0
loot = []
items = ['armor', 'pearls', 'diamonds',
                       'Crown of a Fallen King',
                       'Polished Coins', 'Glass Baubles',
                       'Shiny Buttons', 'Beads & Trinkets',
                       'Ember Eater Amulet (magic)',
                       'Fire Quenched Stone (magic)',
                       'Half Melted Knight Helmet', 'Silver Bracelets',
                       'Gem Shards',]

def end_game():
    '''this function is intended to ask the player
    to play again or end the game loop.'''
    global loot
    player_choice = input('Play Again? y/n: ')
    if player_choice == 'y':
        print('Dragon nests are rare, dangerous, and '
          'overflowing with treasure. \nYou’ve found '
          'one... A massive egg resting atop a glittering '
          'hoard. \nEvery tap risks waking what guards it.'
          '\npress ? for more info.')
        loot = []
        main()
    elif player_choice == 'n':
        exit()

def egg_tap():
    '''this function needs to provide the randomness for which
the egg either gives gold, if so how much? or it gives a special
item such as: armor, more gold, gems or other such treasures,
or deals death.'''
    global gold
    global loot
    global items

    tap_egg = random.choice(['gold', 'loot', 'lose'])
    if tap_egg == 'gold':
        #awards gold
        amt = random.randrange(1, 13)
        print('tap! tap!!')
        print(f'You found + {amt} gold!')
        gold += amt
    elif tap_egg == 'loot':
        #awards item
        item = random.choice(items)
        print('tap! tap!!')
        print(f'You found + {item}!')
        loot.append(item)
    elif tap_egg == 'lose':
        #triggers game loss.
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
            end_game()
    
def main():
    #this is the main game loop.
    print('[T]ap egg or [C]ash out')
    player = input('Player 1: ')
    while player != 'q':
        if player == 't':
            egg_tap()
        elif player == 'c':
            #write score to disk
            with open('highscore.txt', 'w') as f:
                save_name = input('enter name for '
                'highscore: ')
                print(f'{save_name} escapes with {gold} '
                    f'gold and {len(loot)} looted items: {loot}')
                saved = (save_name, 'gold=',gold, ' loot=', len(loot),
                loot)
                f.write(str(saved))
            end_game()
        elif player == 'i':
            print(f'Player 1 score: gold = {gold} '
            f'loot = {len(loot)}{loot}')
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
    exit()
    
if __name__ == "__main__":
    #game intro
    print('Dragon nests are rare, dangerous, and '
          'overflowing with treasure. \nYou’ve found '
          'one... A massive egg resting atop a glittering '
          'hoard. \nEvery tap risks waking what guards it.'
          '\npress ? for more info.')
    main()
