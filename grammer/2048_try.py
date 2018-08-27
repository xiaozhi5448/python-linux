#!/usr/bin/python
# -*- coding:UTF-8 -*-
import curses
from random import randrange, choice
from collections import defaultdict


# define the action list
actions = ['Up', 'Left', 'Down', 'Right', 'Exit', 'Restart']
# map the key to action
key_codes = [ord(item) for item in 'wasdqrWASDQR']
action_dict = dict(zip(key_codes, actions*2))


# get user input
def get_user_action(keyboard):
    action = 'N'
    while action not in action_dict:
        action = keyboard.getch()
    return action_dict[action]


# transpose the matrix
def transpose(field):
    return [list(row) for row in zip(*field)]


#invert the matrix
def invert(field):
    return [row[::-1] for row in field]


# GameField class
class GameField(object):
    def __init__(self, height=4, width=4, win_value=2048):
        self.height = height
        self.width = width
        self.win_value = win_value
        self.score = 0
        self.highscore = 0
        self.reset()

    # produce a new number on the game field
    def spawn(self):
        new_element = 2 if randrange(100) > 89 else 4
        (i, j) = choice([(i, j) for i in range(self.height) for j in range(self.width) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    # reset the game field
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()
    
    # jurge whether we can move the gamefield
    def move_is_possible(self, direction):
        # jurge a row can be move left
        def row_is_left_movable(row):
            def change(i):
                if row[i]==0 and row[i+1]!=0:
                    return True
                elif row[i]!=0 and row[i]==row[i+1]:
                    return True
                else:
                    return False
            return any([change(i) for i in range(len(row)-1)])
        check={}
        check['Left'] = lambda field: any([row_is_left_movable(row) for row in field])
        check['Right'] = lambda field: check['Left'](invert(field))
        check['Up'] = lambda field: check['Left'](transpose(field))
        check['Down'] = lambda field: check['Right'](transpose(field))
        if direction in check:
            return check[direction](self.field)
        else:
            return False

    # move action
    def move(self, direction):
        def move_row_left(row):

            def tighten(row):
                new_row = [item for item in row if item != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                flags = False
                new_row = []

                for i in range(len(row)):
                    if flags:
                        new_row.append(2*row[i])
                        self.score += 2*row[i]
                        flags = False
                    else:
                        if i+1 < len(row) and row[i] == row[i+1]:
                            flags = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert(len(new_row) == len(row))
                return new_row
            return tighten(merge(tighten(row)))
        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Up'] = lambda field: transpose([move_row_left(row) for row in transpose(field)])
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))
        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(direction) for direction in actions)
    
    def draw(self, screen):
        help_str1 = 'W(Up) A(Left) S(Down) D(Right)'
        help_str2 = '     R(restart) Q(quit)'
        gameover_str = '      Game Over'
        win_str = '        you win'
        def cast(string):
            screen.addstr(string + '\n')

        def draw_seperator():
            line = '+' + ('+------' * self.width + '+')[1:]
            seperator = defaultdict(lambda :line)
            if not hasattr(draw_seperator, "counter"):
                draw_seperator.counter = 0
            cast(seperator[draw_seperator.counter])
            draw_seperator.counter += 1

        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num >0 else '|      ' for num in row)+'|')

        screen.clear()
        cast('Score:'+str(self.score))
        if self.highscore != 0:
            cast('HighScore:'+str(self.highscore))
        for row in self.field:
            draw_seperator()
            draw_row(row)
        draw_seperator()
        if self.is_win():
            cast(win_str)
        elif self.is_gameover():
            cast(gameover_str)
        else:
            cast(help_str1)
            cast(help_str2)

def main(stdscr):
    curses.use_default_colors()
    game_field = GameField(win_value=2048)
    def init():
        game_field.reset()
        return 'Game'

    def game():
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    def not_game(state):
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        responses = defaultdict(lambda : state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]
    state_action = {
        'Init':init,
        'Win':lambda : not_game('Win'),
        'Game':game,
        'Gameover':lambda : not_game('Gameover')
    }
    
    state = 'Init'
    while state != 'Exit':
        state = state_action[state]()

curses.wrapper(main)
