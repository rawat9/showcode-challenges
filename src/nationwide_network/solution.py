class NationwideAnalysis:
    def find_largest_payers(self, transactions):
        payers = {}
        amt = 0

        for transation in transactions:
            identifier1, paidOrReceived, amount, _, identifier2 = transation.split()
            amt = int(float(amount[1:]))

            if identifier1 not in payers:
                payers[identifier1] = 0

            if identifier2 not in payers:
                payers[identifier2] = 0

            if paidOrReceived == "paid":
                payers[identifier1] += 1

            if paidOrReceived == "received":
                payers[identifier2] += 1

        return list(
            map(
                lambda x: x[0],
                filter(
                    lambda x: x[1] != 0 and amt != 0,
                    sorted(payers.items(), key=lambda x: x[1], reverse=True),
                ),
            )
        )
