
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

class hocuspocus(object):
    
    def __init__(self):
        self.count_check = 1
        self.start_check = False
        self.cardid = ''
        self.card_num = 0
        self.confirmed_rownum = 0
        self.rownum = 0
    
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

    def start_round(self,skip_to_row :int= 0):
        self.start_check = True
        if skip_to_row >= 1:
            self.rownum = skip_to_row
            return
        os.system('cls')
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
        cardrow = self.return_rowfromcard(self.cardid)
        print(f'Recommeded: {self.cardid} -- Row {cardrow}')
        print('  Select a row: 1, 2, 3')
        # take input from user
        input_a = input()
        self.rownum = int(input_a)

    def sort_rows(self):
        ran1 = random.randint(3, 9)
        ran2 = random.randint(3, 9)
        ran3 = random.randint(3, 9)
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

        elif self.rownum == 0:
            for cd in self.r1:
                self.rows.append(cd)
            for cd in self.r2:
                self.rows.append(cd)
            for cd in self.r3:
                self.rows.append(cd)

        r_row1 = []
        r_row2 = []
        r_row3 = []
        rc = len(self.rows)
        for x in range(0,rc,3):
            r_row1.append(self.rows[x])
        for y in range(1,rc,3):
            r_row2.append(self.rows[y])
        for z in range(2,rc,3):
            r_row3.append(self.rows[z])
        self.r1 = r_row1
        self.r2 = r_row2
        self.r3 = r_row3

    def return_cardfromindex(self,number):
        return str(f'{self.rows[number]}')

    def return_rowfromcard(self,card_id):
        res_r1 = any(ele in card_id for ele in self.r1)
        res_r2 = any(ele in card_id for ele in self.r2)
        res_r3 = any(ele in card_id for ele in self.r3)
        if res_r1 == True:
            self.confirmed_rownum = 1
            return int(1)
        if res_r2 == True:
            self.confirmed_rownum = 2
            return int(2)
        if res_r3 == True:
            self.confirmed_rownum = 3
            return int(3)

    def select_card(self):
        self.card_num = random.randint(0,len(self.rows))
        if self.card_num > 1:
            self.card_num = self.card_num -1
        #print(f'card_num: {self.card_num}')
        self.cardid = str(f'{self.rows[self.card_num]}')
        return #print(f'card: {self.cardid}')
        

    def ask_again(self,skip_to_row:int = 0):
        if skip_to_row >= 1:
            self.rownum = skip_to_row
            return 0
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
        cardrow = self.return_rowfromcard(self.cardid)
        print(f'Recommeded: {self.cardid} -- Row {cardrow}')
        print('  Select a row: 1, 2, 3')
        # take input from user
        input_a = input()
        self.rownum = int(input_a)

    def hocuspocus(self,return_info = False):
        if return_info == True:
            if self.rows[10] == self.cardid:
                return print(f'{self.rows[10]},{self.cardid},Pass,{self.card_num}')
        os.system('cls')
        print('')
        print('')
        print(f'   Hocuspocus - your card was: {self.rows[10]}')
        if self.rows[10] == self.cardid:
            print(f' ---> on point {self.rows[10]} == {self.cardid}  ')

def test_Pocus():
    today = []
    today = hocuspocus()
    a_index = 0
    b_index = 0
    c_index = 0
    today.sort_rows()
    today.select_card()
    a_index = today.return_rowfromcard(today.cardid)
    today.start_round(skip_to_row=a_index)
    today.sort_rows()
    b_index = today.return_rowfromcard(today.cardid)
    today.ask_again(skip_to_row=b_index)
    today.sort_rows()
    c_index = today.return_rowfromcard(today.cardid)
    today.ask_again(skip_to_row=c_index)
    today.sort_rows()
    today.hocuspocus(return_info=True)

def person_Pocus():
    today = []
    today = hocuspocus()
    today.sort_rows()
    today.select_card()
    today.start_round()
    today.sort_rows()
    today.ask_again()
    today.sort_rows()
    today.ask_again()
    today.sort_rows()
    today.hocuspocus()

if __name__ == '__main__':
    person_Pocus()
    #test_Pocus()


