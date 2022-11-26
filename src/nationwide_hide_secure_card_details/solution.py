import re


class Solution:
    def verify_card(self, length: int, prefix, message):
        possibilities = []

        if isinstance(prefix, tuple):
            for p in prefix:
                pattern = f"{p}[0-9]" + "{" + f"{length - len(p)}" + "}"
                found = re.findall(pattern, message)
                if found:
                    possibilities.append(found[0])

            return possibilities

        pattern = f"{prefix}[0-9]" + "{" + f"{length - len(prefix)}" + "}"
        return re.findall(pattern, message)

    def get_card_details(self, message):
        card_number = ""
        card_distributor = "NONE"

        isAmex = self.verify_card(15, ("34", "37"), message)
        isMasterCard = self.verify_card(16, ("51", "52", "53", "54", "55"), message)
        isVisa = self.verify_card(13, "4", message)

        if isAmex:
            card_number = isAmex[0]
            card_distributor = "AMEX"

        elif isMasterCard:
            card_number = isMasterCard[0]
            card_distributor = "MASTERCARD"

        elif isVisa:
            card_number = isVisa[0]
            card_distributor = "VISA"

        return [card_distributor, card_number]

    def get_card_distributor(self, message):
        return self.get_card_details(message)[0]

    def redact_card_details(self, message):
        return [self.get_card_distributor(message), self.get_encoded(message)]

    def get_encoded(self, message):
        card_number = self.get_card_details(message)[1]
        if not card_number:
            return message

        message = message.replace(card_number, "*" * len(card_number))
        return message
