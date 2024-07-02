import tkinter as tk
import random


def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]

    extension = "png" if tk.TkVersion >= 8.6 else "ppm"

    for suit in suits:
        for card in range(1, 11):
            name = f"cards/{str(card)}_{suit}.{extension}"
            image = tk.PhotoImage(file=name)
            card_images.append((card, image))

        for card in face_cards:
            name = f"cards/{str(card)}_{suit}.{extension}"
            image = tk.PhotoImage(file=name)
            card_images.append((10, image))


def deal_card(frame):
    next_card = deck.pop(0)
    deck.append(next_card)
    tk.Label(frame, image=next_card[1], relief="raised").pack(side="left", padx=5)
    return next_card


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("DRAW!")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif player_score == 21:
        result_text.set("Player Wins!")


def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    dealer_card_frame.destroy()
    dealer_card_frame = tk.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", padx=10, pady=10, rowspan=2)

    player_card_frame.destroy()
    player_card_frame = tk.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", padx=10, pady=10, rowspan=2)

    player_hand.clear()
    dealer_hand.clear()
    player_score_label.set(0)
    dealer_score_label.set(0)
    result_text.set("")
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def shuffle():
    random.shuffle(deck)


window = tk.Tk()

window.title("Black Jack")
window.geometry("640x480")
window.configure(background="green")

result_text = tk.StringVar()
result = tk.Label(window, textvariable=result_text, background="green", fg="white", font=("Helvetica", 24, "bold"))
result.grid(row=0, column=0, columnspan=3, pady=10)

card_frame = tk.Frame(window, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, columnspan=3, rowspan=2, pady=10, padx=10, sticky="ew")

dealer_score_label = tk.IntVar()
tk.Label(card_frame, text="Dealer", background="green", fg="white", font=("Helvetica", 16, "bold")).grid(row=0,
                                                                                                         column=0,
                                                                                                         padx=10)
tk.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white",
         font=("Helvetica", 16, "bold")).grid(row=1, column=0, padx=10)

dealer_card_frame = tk.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="ew")

player_score_label = tk.IntVar()
tk.Label(card_frame, text="Player", background="green", fg="white", font=("Helvetica", 16, "bold")).grid(row=2,
                                                                                                         column=0,
                                                                                                         padx=10)
tk.Label(card_frame, textvariable=player_score_label, background="green", fg="white",
         font=("Helvetica", 16, "bold")).grid(row=3, column=0, padx=10)

player_card_frame = tk.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, rowspan=2, padx=10, pady=10, sticky="ew")

button_frame = tk.Frame(window, background="green")
button_frame.grid(row=3, column=0, columnspan=3, pady=10, sticky="ew")

# Button styles
button_style = {
    "font": ("Helvetica", 14, "bold"),
    "bg": "#007bff",
    "activebackground": "#0056b3",
    "activeforeground": "white",
    "relief": "raised",
    "bd": 2,
    "highlightthickness": 0,
    "width": 10,
    "height": 2,
    "padx": 10,
    "pady": 10
}

dealer_button = tk.Button(button_frame, text="Dealer", command=deal_dealer, **button_style)
dealer_button.grid(row=0, column=0, padx=10)

player_button = tk.Button(button_frame, text="Player", command=deal_player, **button_style)
player_button.grid(row=0, column=1, padx=10)

new_game_button = tk.Button(button_frame, text="NEW GAME", command=new_game, **button_style)
new_game_button.grid(row=3, column=0, pady=5)

shuffle_button = tk.Button(button_frame, text="Shuffle", command=shuffle, **button_style)
shuffle_button.grid(row=3, column=1, pady=5)

cards = []
load_images(cards)

deck = list(cards)
shuffle()

dealer_hand = []
player_hand = []
new_game()

window.mainloop()
