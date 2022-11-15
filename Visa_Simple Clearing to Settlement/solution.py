class Solution:
    def calculate_settlement(self, account, amount, merchantType, acquirer, issuer):
        banks = [0] * 64
        failures = []
        i = 0

        for acc, amt, mer, acq, iss in zip(
            account, amount, merchantType, acquirer, issuer
        ):
            if (
                not self.__validate_account_number(acc, mer)
                or not self.__validate_amount(amt)
                or not self.__validate_special_conditions(amt, iss, acq, mer)
                or not self.__validate_bank(iss, acq)
                or not self.__validate_merchantType(mer)
            ):
                failures.append(i)

            index = self.__generate_index(acq, iss)
            if index <= 63:
                banks[index] += amt
            i += 1

        return banks if len(failures) == 0 else failures

    def __generate_index(self, acquirer, issuer):
        return (issuer * 8) + acquirer

    def __validate_bank(self, iss, acq):
        return (0 <= iss <= 7) and (0 <= acq <= 7)

    def __validate_special_conditions(self, amt, iss, acq, mType):
        # Bank 2 is only an Issuer
        if acq == 2:
            return False

        # Bank 7 is only an Acquirer
        if iss == 7:
            return False

        # Bank 5 only accepts Supermarket, Travel, and Retail transactions
        if acq == 5 and mType not in (1, 2, 5):
            return False

        # Verification transactions always have an amount of `0`
        if mType == 0:
            if amt != 0:
                return False

        return True

    def __validate_amount(self, amount):
        """
        Validate amount
        """
        return amount >= 0

    def __validate_merchantType(self, merchantType):
        """
        Validate merchantType
        """
        return merchantType >= 0 and merchantType <= 7

    def __validate_account_number(self, account_number, mType):
        """
        Validate account_number
        """

        if len(str(account_number)) != 8:
            return False

        if account_number not in range(10000000, 100000000):
            return False

        # Corporate accounts do not accept gambling transactions
        if (account_number % 42) == 37:
            if mType == 4:
                return False

        if (account_number % 42) not in (17, 27, 37):
            return False

        return account_number >= 0
