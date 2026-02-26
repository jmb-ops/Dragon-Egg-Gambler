'''Dragon Egg Gambler
'''
import random
#game items.
i = 0
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
    global gold
    player_choice = input('Play Again? y/n: ')
    while player_choice != 'y' or player_choice != 'n':
        if player_choice == 'y':
            print('Dragon nests are rare, dangerous, and '
              'overflowing with treasure. \nYou’ve found '
              'one... A massive egg resting atop a glittering '
              'hoard. \nEvery tap risks waking what guards it.'
              '\npress ? for more info.')
            #reset player stats 
            gold = 0
            loot = []
            main()
        elif player_choice == 'n':
            exit()
        player_choice = input('Play Again? y/n: ')

def egg_tap():
    '''this function needs to provide the randomness for which
the egg either gives gold, if so how much? or it gives a special
item such as: armor, more gold, gems or other such treasures,
or deals death.'''
    global gold
    global loot
    global items
    global i
    #this should incriment for the first 3 uses
    

    tap_egg = random.choice(['gold', 'loot', 'lose', 'gold', 'gold'])
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
        #triggers game loss. Also, players should not die on the first
        #play, ideally not until they at least have a chance to get 1
        #loot item.
        i += 1
        while i <= 1:
            loot.append('armor')
            print('tap! tap!!')
            print(f'You found + armor!')
            main()
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
    '''this is the main game loop.
'''
    print('[T]ap egg or [C]ash out')
    player = input('Player 1: ')
    while player != 'q':
        if player == 't':
            egg_tap()
        elif player == 'c':
            #write score to disk
            try:
                with open('highscore.txt', 'w', encoding="utf-8") as f:
                    save_name = input('enter name for '
                    'highscore: ')
                    print(f'{save_name} escapes with {gold} '
                        f'gold and {len(loot)} looted items: {loot}')
                    saved = (save_name, 'gold=',gold, ' loot=', len(loot),
                    loot)
                    f.write(str(saved))
                end_game()
            except:
                print('cannot save game at this time.')
                print('running from the command line will fix'
                      ' the issue.')
                user = input('exit? y/n: ')
                if user == 'y':
                    exit()
                exit()
        elif player == 'i':
            print(f'Player 1 score: gold = {gold} '
            f'loot = {len(loot)}{loot}')
        elif player == 'highscore':
            try:
                with open('highscore.txt', 'r') as f:
                    data = f.read()
                print(data)
            except:
                print('No highscore found!')
        elif player == '?':
            print('(press i for score & highscore'
                  ' to see the highscore, t to tap'
                ' the egg, c to cash out, q to quit.\n'
                  'post your high score at r/DragonEggGambler\n'
                  'or just say hi and make some friends!)')
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
