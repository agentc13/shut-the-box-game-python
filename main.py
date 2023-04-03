import random
import os
import die_faces


play_again = True

while play_again:
    os.system('clear')
    best_score = 123456789
    score_list = []
    player_number = int(input('How many players?: '))
    for player in range(player_number):

        # Display numbers
        players_turn = True
        the_box = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Roll Dice
        while players_turn:
            current_player = player + 1
            print(the_box)
            tile_sum = 0
            for tile in the_box:
                tile_int = int(tile)
                tile_sum += tile_int
            if tile_sum == 0:
                os.system('clear')
            elif tile_sum < 7:
                die1 = random.randint(1, 6)
                print(die_faces.dice_art[die1 - 1])
            else:
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                print(die_faces.dice_art[die1 - 1] + die_faces.dice_art[die2 - 1])

            # Pick Numbers to "flip"
            flip_string = input('Which numbers do you wish to flip? (separate with ","). If you cannot remove/'
                                'anything type "none": ').replace(' ', '')
            if flip_string == 'none':
                # Display score.
                try:
                    score = int(''.join(the_box))
                    score_list.append(score)
                    os.system('clear')
                    print(f'Player {current_player} score is {score}')
                    players_turn = False
                except ValueError:
                    os.system('clear')
                    score = 0
                    score_list.append(score)
                    print(f'You shut the box!')
                    players_turn = False

            else:
                flip_list = flip_string.split(',')
                print(flip_list)
                # Display new list of numbers removing the "flipped" ones
                for i in flip_list:
                    try:
                        the_box.remove(i)
                    except ValueError:
                        pass
                os.system('clear')

    # Compare scores and declare the winner.
    print(score_list)
    for player_score in score_list:
        if player_score < best_score:
            best_score = player_score
    winner = score_list.index(best_score) + 1
    print(f'The winner is player {winner}, with a score of {best_score}!')
    response = input('Do you want to play again? (y/n): ')
    if response.lower() == 'y':
        play_again = True
    else:
        play_again = False
