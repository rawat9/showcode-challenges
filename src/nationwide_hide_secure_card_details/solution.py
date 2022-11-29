import re


class Solution:
    def __init__(self):
        self.message = ""

    def verify_card(self, length: int, prefix):
        possibilities = []

        if isinstance(prefix, tuple):
            for p in prefix:
                pattern = f"{p}[0-9]" + "{" + f"{length - len(p)}" + "}"
                found = re.findall(pattern, self.message)
                if found:
                    possibilities += found

            self.message = self.update_message(possibilities, self.message)
            return possibilities

        pattern = f"{prefix}[0-9]" + "{" + f"{length - len(prefix)}" + "}"
        found = re.findall(pattern, self.message)
        if found:
            self.message = self.update_message(found, self.message)
            return found

        return []

    def get_card_details(self, message):
        self.message = message

        isMasterCard = self.verify_card(16, ("51", "52", "53", "54", "55"))
        isAmex = self.verify_card(15, ("34", "37"))
        isVisa = self.verify_card(13, "4")

        all_possibles = isMasterCard + isAmex + isVisa
        card_distributors = list(map(self.get_card_distributor, all_possibles))

        if not card_distributors:
            return ["NONE", self.message]

        return [*card_distributors, self.message]

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
        return self.get_card_details(message)

    def update_message(self, card_numbers, message):
        for card_number in card_numbers:
            message = message.replace(card_number, "*" * len(card_number))

        return message
