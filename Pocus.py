
from Deck import Deck
import os
import random

class Row(object):
    def __init__(self, number, title):
        self.row = []
        self.number = number
        self.title = title

    def draw(self, deck):
        # The argument we are passing is a deck created from the deck class and we are withdrawing a card
        # using the deck method draw_card(). Then we are appending the returned value into the self.row[]
        self.row.append(Deck.draw_card(deck))
        # returning the instance object and allowing me to draw again
        return self

    def return_row(self):
        for card in self.row:
            # Showing each card the row has
            print(card.show_card())

    def return_cards(self):
        r_list = []
        for xcard in self.row:
            add = "{} of {}".format(xcard.value, xcard.suit)
            r_list.append(add)
        return r_list


def Results():
    print('')
    print('Row - 1')
    print(f'{Row1.show_row()}')
    print('')
    print('Row - 2')
    print(f'{Row2.show_row()}')
    print('')
    print('Row - 3')
    print(f'{Row3.show_row()}')


class hocuspocus(object):
    
    def __init__(self):
        self.count_check = 1
        self.start_check = False
    
        # Creating the deck
        f_deck = Deck()
        self.rows = []
        # Creating the player
        Row1 = Row(1, "first")
        Row2 = Row(2, "second")
        Row3 = Row(3, "third")
        row_1 = []
        row_2 = []
        row_3 = []
        # Drawing the cards from the deck
        Row1.draw(f_deck).draw(f_deck).draw(f_deck).draw(
            f_deck).draw(f_deck).draw(f_deck).draw(f_deck)
        Row2.draw(f_deck).draw(f_deck).draw(f_deck).draw(
            f_deck).draw(f_deck).draw(f_deck).draw(f_deck)
        Row3.draw(f_deck).draw(f_deck).draw(f_deck).draw(
            f_deck).draw(f_deck).draw(f_deck).draw(f_deck)

        # Get all 3 rows
        self.r1 = Row1.return_cards()
        self.r2 = Row2.return_cards()
        self.r3 = Row3.return_cards()

    def start_round(self):
        self.start_check = True
        os.system('cls')
        print('')
        print('')
        print('')
        print('')
        print('Select One Card; remember this card, only select the row your Card is in')
        print('')
        print('')
        print('')
        print('')
        print(f'Row 1: {self.r1}')
        print(f'Row 2: {self.r2}')
        print(f'Row 3: {self.r3}')
        print('  Select a row: 1, 2, 3')
        # take input from user
        input_a = input()
        self.rownum = int(input_a)


    def sort_rows(self):
        ran1 = random.randint(3, 9)
        ran2 = random.randint(3, 9)
        ran3 = random.randint(3, 9)
        if self.start_check == False:
            return 1
        self.rows = []
        if self.rownum == 1:
            if ran1 < 7:
                for cd in self.r2:
                    self.rows.append(cd)
                for cd in self.r1:
                   self.rows.append(cd)
                for cd in self.r3:
                    self.rows.append(cd)
            else:
                for cd in self.r3:
                    self.rows.append(cd)
                for cd in self.r1:
                    self.rows.append(cd)
                for cd in self.r2:
                    self.rows.append(cd)
        elif self.rownum == 2:
            if ran2 > 7:
                for cd in self.r1:
                    self.rows.append(cd)
                for cd in self.r2:
                    self.rows.append(cd)
                for cd in self.r3:
                    self.rows.append(cd)
            else:
                for cd in self.r3:
                    self.rows.append(cd)
                for cd in self.r2:
                    self.rows.append(cd)
                for cd in self.r1:
                    self.rows.append(cd)
        elif self.rownum == 3:
            if ran3 > 7:
                for cd in self.r1:
                    self.rows.append(cd)
                for cd in self.r3:
                    self.rows.append(cd)
                for cd in self.r2:
                    self.rows.append(cd)
            else:
                for cd in self.r2:
                    self.rows.append(cd)
                for cd in self.r3:
                    self.rows.append(cd)
                for cd in self.r1:
                    self.rows.append(cd)    
        r_row1 = []
        r_row2 = []
        r_row3 = []
        rc = len(self.rows)
        for x in range(0,rc,3):
            r_row1.append(self.rows[x])
        for x in range(1,rc,3):
            r_row2.append(self.rows[x])
        for x in range(2,rc,3):
            r_row3.append(self.rows[x])
        self.r1 = r_row1
        self.r2 = r_row2
        self.r3 = r_row3


    def ask_again(self):
        if self.start_check == False:
            return 1
        self.count_check = self.count_check + 1
        if self.count_check == 3: 
            final_message = 'and final round'
        else:
            final_message = ''
        os.system('cls')
        print('')
        print('')
        print(f'  Round {self.count_check} {final_message}')
        print('  Same as before...')
        print(' Find your selected card and input the Row the card is in  ')
        print('')
        print('')
        print('')
        print('')
        print(f'Row 1: {self.r1}')
        print(f'Row 2: {self.r2}')
        print(f'Row 3: {self.r3}')
        print('  Select a row: 1, 2, 3')
        # take input from user
        input_a = input()
        self.rownum = int(input_a)

    def hocuspocus(self):
        os.system('cls')
        print('')
        print('')
        print(f'   Hocuspocus - your card was: {self.rows[10]}')

'''
    sr_row1 = []
    sr_row2 = []
    sr_row3 = []
    rc2 = len(rows)
    for x in range(0,rc2,3):
        sr_row1.append(rows[x])
    for x in range(1,rc2,3):
        sr_row2.append(rows[x])
    for x in range(2,rc2,3):
        sr_row3.append(rows[x])
    print(f'Row 1: {sr_row1}')
    print(f'Row 2: {sr_row2}')
    print(f'Row 3: {sr_row3}')
    print('  Select a row: 1, 2, 3')
    # take input from user
    input_b = input()
    rownum = int(input_b)
    rows = []
    if rownum == 1:
        for cd in sr_row2:
            rows.append(cd)
        for cd in sr_row1:
            rows.append(cd)
        for cd in sr_row3:
            rows.append(cd)
    elif rownum == 2:
        for cd in sr_row3:
            rows.append(cd)
        for cd in r2:
            rows.append(cd)
        for cd in sr_row1:
            rows.append(cd)
    elif rownum == 3:
        for cd in sr_row1:
            rows.append(cd)
        for cd in sr_row3:
            rows.append(cd)
        for cd in sr_row2:
            rows.append(cd)
    tr_row1 = []
    tr_row2 = []
    tr_row3 = []
    rc3 = len(rows)
    for x in range(0,rc3,3):
        tr_row1.append(rows[x])
    for x in range(1,rc3,3):
        tr_row2.append(rows[x])
    for x in range(2,rc3,3):
        tr_row3.append(rows[x])
    print(f'Row 1: {tr_row1}')
    print(f'Row 2: {tr_row2}')
    print(f'Row 3: {tr_row3}')
    print('  Select a row: 1, 2, 3')
    input_c = input()
    rownum = 0
    rownum = int(input_c)
    rows = []
    if rownum == 1:
        for cd in tr_row2:
            rows.append(cd)
        for cd in tr_row1:
            rows.append(cd)
        for cd in tr_row3:
            rows.append(cd)
    elif rownum == 2:
        for cd in tr_row3:
            rows.append(cd)
        for cd in tr_row2:
            rows.append(cd)
        for cd in tr_row1:
            rows.append(cd)
    elif rownum == 3:
        for cd in tr_row1:
            rows.append(cd)
        for cd in tr_row3:
            rows.append(cd)
        for cd in tr_row2:
            rows.append(cd)

'''
today = []
today = hocuspocus()
today.start_round()
today.sort_rows()
today.ask_again()
today.sort_rows()
today.ask_again()
today.sort_rows()
today.hocuspocus()