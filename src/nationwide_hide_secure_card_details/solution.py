import re


class Solution:
    def __init__(self):
        self.numbers_in_message = 0

    def get_numbers(self, message):
        self.numbers_in_message = len(re.findall("[0-9]+", message))

    def verify_card(self, length: int, prefix, message):
        possibilities = []

        if isinstance(prefix, tuple):
            for p in prefix:
                pattern = f"{p}[0-9]" + "{" + f"{length - len(p)}" + "}"
                found = re.findall(pattern, message)
                if found and self.numbers_in_message > 0:
                    self.numbers_in_message -= len(found)
                    possibilities += found

            return possibilities

        pattern = f"{prefix}[0-9]" + "{" + f"{length - len(prefix)}" + "}"
        found = re.findall(pattern, message)
        if (
            found
            and self.numbers_in_message > 0
            and len(found) <= self.numbers_in_message
        ):
            self.numbers_in_message -= len(found)
            return found

        return []

    def get_card_details(self, message):
        self.get_numbers(message)
        isMasterCard = self.verify_card(16, ("51", "52", "53", "54", "55"), message)
        isAmex = self.verify_card(15, ("34", "37"), message)
        isVisa = self.verify_card(13, "4", message)

        all_possibles = isMasterCard + isAmex + isVisa
        card_distributors = list(map(self.get_card_distributor, all_possibles))

        if not card_distributors:
            return [["NONE"], all_possibles]

        return [card_distributors, all_possibles]

    def get_card_distributor(self, card_number: str):
        card_distributor = "NONE"

        if card_number.startswith(("34", "37")):
            card_distributor = "AMEX"

        elif card_number.startswith(("51", "52", "53", "54", "55")):
            card_distributor = "MASTERCARD"

        elif card_number.startswith("4"):
            card_distributor = "VISA"

        return card_distributor

    def redact_card_details(self, message):
        return self.get_card_details(message)[0] + [self.get_encoded(message)]

    def get_encoded(self, message):
        card_numbers = self.get_card_details(message)[1]
        if not card_numbers:
            return message

        for card_number in card_numbers:
            message = message.replace(card_number, "*" * len(card_number))

        return message
