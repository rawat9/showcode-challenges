## Bataille

Bataille, or War, is a card game generally played with two players. Each player normally begins with a face down deck. Then, both players reveal the top card of the deck. The player with the highest value card takes both cards and places them in a face-up pile. If the cards have the same value, the next card is placed face down (for mystery!) on top of the revealed card by each player and then the card after is revealed. The winner takes all the cards as before. If there is a draw again, then the process repeats until there is a winner who takes all the cards. If a player runs out of cards, they flip their face-up deck upside down. If they do not have any cards in that deck, they lose the game.

You will be given two strings which represent the starting deck of each player from top to bottom. Each character in the string is a card and is one of the following, from least value to highest value:

`2 3 4 5 6 7 8 9 T J Q K A`

Return `1` if player 1 will win, `2` if player 2 will win and `0` in all other circumstances. You can assume that the winner takes cards in the order that they are, starting with all his own, e.g. a play with `K 2 A` against `K 5 6` is a win for player 1, who puts them on the face-up deck in the order `K 2 A K 5 6` from bottom to top.