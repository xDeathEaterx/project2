from tkinter import *
import pygame
import random
from PIL import Image, ImageTk
from tkinter import messagebox


root = Tk()
root.title(f'Blackjack - Card Game')
root.iconbitmap("C:/Users/xlDeathEaterlx/Desktop/BMTH.ico")
root.geometry("1200x800")
root.configure(background='green')

def hold():
    global ptotal, dtotal, pscore
    ptotal = 0
    dtotal = 0

    for score in dscore:
        dtotal = score
    for score in pscore:
        ptotal = score

    hit_button.config(state='disabled')
    hold_button.config(state='disabled')

    if dtotal >= 17:
        if dtotal > 21:
            messagebox.showinfo('Player wins!', f'Player Wins! Dealer: {dtotal} Player: {ptotal}')
        elif dtotal == ptotal:
            messagebox.showinfo('Tie! Player and Dealer win!')
        elif dtotal > ptotal:
            messagebox.showinfo('Dealer wins!', f'Dealer Wins! Dealer: {dtotal} Player: {ptotal}')
        else:
            messagebox.showinfo('Player wins!', f'Player Wins! Dealer: {dtotal} Player: {ptotal}')
    else:
        dhit()


def blackjack_shuffle(player):
    global ptotal, dtotal, pscore
    ptotal = 0
    dtotal = 0
    if player == "dealer":
        if len(dscore) == 2:
            if dscore[0] + dscore[1] == 21:
                bj_status['dealer'] = 'yes'

    if player == 'player':
        if len(pscore) == 2:
            if pscore[0] + pscore[1] == 21:
                bj_status['player'] = 'yes'
        else:
            for score in pscore:
                ptotal += score

            if ptotal == 21:
                bj_status['player'] = 'yes'
            elif ptotal > 21:
                for card_num, card in enumerate(pscore):
                    if card == 11:
                        pscore[card_num] = 1
                        ptotal = 0
                        for score in pscore:
                            ptotal = score
                        if ptotal > 21:
                            bj_status['player'] = 'bust'

                else:
                    if ptotal == 21:
                        bj_status['player'] = 'yes'
                    if ptotal > 21:
                        bj_status['player'] = 'bust'



    if len(dscore) == 2 and len(pscore) == 2:
        if bj_status['dealer'] == 'yes' and bj_status['player'] == 'yes':
            messagebox.showinfo('Push! Dealer and Player win!')
            hit_button.config(state='disabled')
            hold_button.config(state='disabled')
        elif bj_status['dealer'] == 'yes':
            messagebox.showinfo('Dealer wins! Blackjack!')
            hit_button.config(state='disabled')
            hold_button.config(state='disabled')
        elif bj_status['player'] == 'yes':
            messagebox.showinfo('Player wins! Blackjack!')
            hit_button.config(state='disabled')
            hold_button.config(state='disabled')
    else:
        if bj_status['dealer'] == 'yes' and bj_status['player'] == 'yes':
            messagebox.showinfo('Push! Dealer and Player win!')
            hit_button.config(state='disabled')
            hold_button.config(state='disabled')
        elif bj_status['dealer'] == 'yes':
            messagebox.showinfo('Dealer wins!')
            hit_button.config(state='disabled')
            hold_button.config(state='disabled')
        elif bj_status['player'] == 'yes':
            messagebox.showinfo('Player wins!')
            hit_button.config(state='disabled')
            hold_button.config(state='disabled')

    if bj_status['player'] == 'bust':
        messagebox.showinfo('Player busts!',f'Player loses! {ptotal}')
        hit_button.config(state='disabled')
        hold_button.config(state='disabled')


def resize_cards(card):
    card_img = Image.open(card)
    resize_img = card_img.resize((150, 218))
    global new_card_image
    new_card_image = ImageTk.PhotoImage(resize_img)
    return new_card_image


def shuffle():
    global bj_status, ptotal, dtotal
    ptotal = 0
    dtotal = 0
    bj_status = {'dealer':'no','player':'no'}


    hit_button.config(state='normal')
    hold_button.config(state='normal')
    # Clear out old cards from previous games
    dealer_label1.config(image='')
    dealer_label2.config(image='')
    dealer_label3.config(image='')
    dealer_label4.config(image='')
    dealer_label5.config(image='')

    player_label1.config(image='')
    player_label2.config(image='')
    player_label3.config(image='')
    player_label4.config(image='')
    player_label5.config(image='')

    suits = ['diamonds','clubs', 'hearts', 'spades']
    values = range(2, 15)

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    global dealer, player, dposition, pposition, dscore, pscore
    dealer = []
    player = []
    dscore = []
    pscore = []
    dposition = 0
    pposition = 0

    # Starting cards
    dhit()
    dhit()
    phit()
    phit()


def dhit():
    global dposition
    if dposition < 5:
        try:
            dealer_card = random.choice(deck)
            deck.remove(dealer_card)
            player.append(dealer_card)

            # Dealer score and convert face cards
            dcard = int(dealer_card.split('_', 1)[0])
            if dcard == 14:
                dscore.append(11)
            elif dcard == 11 or dcard == 12 or dcard == 13:
                dscore.append(10)
            else:
                dscore.append(dcard)

            global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5

            if dposition == 0:
                dealer_image1 = resize_cards(f'C:/Users/xlDeathEaterlx/Desktop/Cards/{dealer_card}.png')
                dealer_label1.config(image=dealer_image1)
                dposition += 1
            elif dposition == 1:
                dealer_image2 = resize_cards(f'C:/Users/xlDeathEaterlx/Desktop/Cards/{dealer_card}.png')
                dealer_label2.config(image=dealer_image2)
                dposition += 1
            elif dposition == 2:
                dealer_image3 = resize_cards(f'C:/Users/xlDeathEaterlx/Desktop/Cards/{dealer_card}.png')
                dealer_label3.config(image=dealer_image3)
                dposition += 1
            elif dposition == 3:
                dealer_image4 = resize_cards(f'C:/Users/xlDeathEaterlx/Desktop/Cards/{dealer_card}.png')
                dealer_label4.config(image=dealer_image4)
                dposition += 1
            elif dposition == 4:
                dealer_image5 = resize_cards(f'C:/Users/xlDeathEaterlx/Desktop/Cards/{dealer_card}.png')
                dealer_label5.config(image=dealer_image5)
                dposition += 1

            root.title(f'Blackjack - {len(deck)} Cards Left')

        except:
            root.title(f'Round Complete - No Cards in Deck')

        blackjack_shuffle('dealer')


def phit():
    global pposition
    if pposition < 5:
        try:
            player_card = random.choice(deck)
            deck.remove(player_card)
            player.append(player_card)

            pcard = int(player_card.split('_', 1)[0])
            if pcard == 14:
                pscore.append(11)
            elif pcard == 11 or pcard == 12 or pcard == 13:
                pscore.append(10)
            else:
                pscore.append(pcard)

            global player_image1, player_image2, player_image3, player_image4, player_image5

            if pposition == 0:
                player_image1 = resize_cards(f'C:/Users/xlDeathEaterlx/Desktop/Cards/{player_card}.png')
                player_label1.config(image=player_image1)
                pposition += 1
            elif pposition == 1:
                player_image2 = resize_cards(f'C:/Users/xlDeathEaterlx/Desktop/Cards/{player_card}.png')
                player_label2.config(image=player_image2)
                pposition += 1
            elif pposition == 2:
                player_image3 = resize_cards(f'C:/Users/xlDeathEaterlx/Desktop/Cards/{player_card}.png')
                player_label3.config(image=player_image3)
                pposition += 1
            elif pposition == 3:
                player_image4 = resize_cards(f'C:/Users/xlDeathEaterlx/Desktop/Cards/{player_card}.png')
                player_label4.config(image=player_image4)
                pposition += 1
            elif pposition == 4:
                player_image5 = resize_cards(f'C:/Users/xlDeathEaterlx/Desktop/Cards/{player_card}.png')
                player_label5.config(image=player_image5)
                pposition += 1

            root.title(f'Blackjack - {len(deck)} Cards Left')

        except:
            root.title(f'Round Complete - No Cards in Deck')

        blackjack_shuffle('player')

mainframe = Frame(root, bg='green')
mainframe.pack(pady=20)

# Card frames
dealer_frame = LabelFrame(mainframe, text='Dealer', bd=0)
dealer_frame.pack(padx=20, ipadx=20)
player_frame = LabelFrame(mainframe, text='Player', bd=0)
player_frame.pack(ipadx=20, pady=10)

# Dealer cards
dealer_label1 = Label(dealer_frame, text='')
dealer_label1.grid(row=0, column=0, pady=20, padx=20)

dealer_label2 = Label(dealer_frame, text='')
dealer_label2.grid(row=0, column=1, pady=20, padx=20)

dealer_label3 = Label(dealer_frame, text='')
dealer_label3.grid(row=0, column=2, pady=20, padx=20)

dealer_label4 = Label(dealer_frame, text='')
dealer_label4.grid(row=0, column=3, pady=20, padx=20)

dealer_label5 = Label(dealer_frame, text='')
dealer_label5.grid(row=0, column=4, pady=20, padx=20)

# Player cards
player_label1 = Label(player_frame, text='')
player_label1.grid(row=1, column=0, pady=20, padx=20)

player_label2 = Label(player_frame, text='')
player_label2.grid(row=1, column=1, pady=20, padx=20)

player_label3 = Label(player_frame, text='')
player_label3.grid(row=1, column=2, pady=20, padx=20)

player_label4 = Label(player_frame, text='')
player_label4.grid(row=1, column=3, pady=20, padx=20)

player_label5 = Label(player_frame, text='')
player_label5.grid(row=1, column=4, pady=20, padx=20)

# Button Frame
button_frame = Frame(root, bg='green')
button_frame.pack(pady=20)

# Buttons
shuffle_button = Button(button_frame, text='Shuffle Deck', font=('Helvetica', 14), command=shuffle)
shuffle_button.grid(row=0, column=0)

hit_button = Button(button_frame, text='Hit', font=('Helvetica', 14), command=phit)
hit_button.grid(row=0, column=1, padx=10)

hold_button = Button(button_frame, text='Hold', font=('Helvetica', 14), command=hold)
hold_button.grid(row=0, column=2)

shuffle()


root.mainloop()

