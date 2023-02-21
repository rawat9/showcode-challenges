from itertools import zip_longest


class Bataille:
    def __init__(self):
        self.cards = "23456789TJQKA"
        self.player1_face_up_pile = []
        self.player2_face_up_pile = []

    def are_same_cards(self, card1: str, card2: str) -> bool:
        return card1 == card2

    def play(self, player1_deck: str, player2_deck: str) -> int:
        if len(player1_deck) == 0 and len(player2_deck) == 0:
            return 0

        if any(card not in self.cards for card in player1_deck):
            return 0

        if any(card not in self.cards for card in player2_deck):
            return 0

        return self.play_round(player1_deck, player2_deck)

    def play_round(self, player1_deck: str, player2_deck: str) -> int:
        for card1, card2 in zip_longest(player1_deck, player2_deck):
            if card1 is None:
                if len(self.player1_face_up_pile) == 0:
                    return 2
                face_up_pile = "".join(self.player1_face_up_pile)
                self.player1_face_up_pile = []
                return self.play_round(face_up_pile, player2_deck)

            if card2 is None:
                if len(self.player2_face_up_pile) == 0:
                    return 1
                face_up_pile = "".join(self.player2_face_up_pile)
                self.player2_face_up_pile = []
                return self.play_round(player1_deck, face_up_pile)

            if self.are_same_cards(card1, card2):
                continue

            if self.cards.index(card1) > self.cards.index(card2):
                self.player1_face_up_pile.append(card1)
                self.player1_face_up_pile.append(card2)
            else:
                self.player2_face_up_pile.append(card1)
                self.player2_face_up_pile.append(card2)

            player1_deck = player1_deck[1:]
            player2_deck = player2_deck[1:]

        return 0
