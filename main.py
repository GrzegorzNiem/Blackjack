import random
import art
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw():
    drawing = random.choice(cards)
    return drawing
def ace(aced_score, hand):
    for i in range(len(hand)):
        if hand[i] == 11 and aced_score > 21:
            aced_score -= 10
            hand[i] = 1
    print(hand)
    return aced_score,hand
def pc_decision(pc_score,pc_cards):
    while pc_score < 17:
        new_card_pc = draw()
        pc_cards.append(new_card_pc)
        pc_score += new_card_pc
        pc_score, pc_cards = ace(pc_score,pc_cards)
        return pc_score, pc_cards
def game():
    human_cards = []
    pc_cards = []
    begin = input("Do you wanna play Blackjack game: 'y' or 'n' ")
    if begin == 'y':
        first_card_pc = draw()
        pc_cards.append(first_card_pc)
        second_card_pc = draw()
        pc_cards.append(second_card_pc)
        pc_score=sum(pc_cards)


        first_card = draw()
        human_cards.append(first_card)
        second_card = draw()
        human_cards.append(second_card)
        score = sum(human_cards)
        os.system('cls')
        print(art.logo)
        print(f"{human_cards}, current score: {score} ")
        print(f"Computer's first card: {first_card_pc}")
        over_21 = False
        while not over_21:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                new_card = draw()
                print(new_card)
                human_cards.append(new_card)
                score+=new_card
                score,human_cards = ace(score,human_cards)

                print(f"You drew {new_card}")
                print(f"{human_cards}, current score: {score} ")
                print(f"Computer's first card: {first_card_pc}")
                if score > 21:
                    print("Bust! \nYou lost!")
                    over_21 = True
                    game()
            if another_card == 'n':
                if not pc_score > 17:
                    pc_score, pc_cards = pc_decision(pc_score,pc_cards)
                print(f"{human_cards}, current score: {score} ")
                print(f"Computer's final hand: {pc_cards}, {pc_score}")
                if pc_score <= 21:
                    if score == pc_score:
                        print("draw")
                    elif score > pc_score:
                        print("You win!")
                    elif score < pc_score:
                        print("You lost!")
                    game()
                elif pc_score > 21:
                    print("You win!")
                    game()




game()



