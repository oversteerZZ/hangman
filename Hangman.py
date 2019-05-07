#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/22

def hangman(word):
    wrong = 0
    stages = ['',
              '__________       ',
              '|                ',
              '|        |       ',
              '|        o       ',
              '|       /|       ',
              '|       /        ',
              '|                ',
              ]
    rletters = list(word)
    board = ['__']*len(word)
    win = False
    print('Welcome to Hangman')

    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Guess a letter'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '__' not in board:
            print('You Win!')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lose! It was {}.'.format(word))

hangman('cat')