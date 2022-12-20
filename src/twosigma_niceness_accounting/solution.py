from datetime import date


class NiceMigration:
    def __init__(self):
        self.niceness = 0
        self.children = {}

    def calculate_niceness(self, op, value):
        if op == "=":
            self.niceness = float(value)
        elif op == "+":
            self.niceness += float(value)
        elif op == "-":
            self.niceness -= float(value)
        elif op == "*":
            self.niceness *= float(value)
        elif op == "/":
            self.niceness /= float(value)
        elif op == "++":
            self.niceness += 1
        elif op == "--":
            self.niceness -= 1

        if self.niceness < 0:
            return -1

        return self.niceness

    def sorted_records(self, records):
        def transform(d):
            y, m, d = d[:4], d[4:6], d[6:]
            return y + "-" + m + "-" + d

        return sorted(
            records,
            key=lambda x: date(*map(int, transform(x.split()[0]).split("-"))),
        )

    def convert(self, old_format):
        result = []
        records = old_format.split("\n")
        sorted_record = self.sorted_records(records)

        for record in sorted_record:
            d, child_account, op, value = record.split()
            y, m, d = int(d[:4]), int(d[4:6]), int(d[6:])
            niceness_score = self.calculate_niceness(op, value)

            if niceness_score == -1:
                niceness_score = "?"
            else:
                niceness_score = f"{niceness_score:.2f}"

            res = f"{y}{m:02d}{d:02d} @{child_account.lstrip('#')} {niceness_score}"

            if child_account not in self.children:
                self.children[child_account] = [res]
            else:
                self.children[child_account].append(res)

        for child in self.children:
            result.extend(self.children[child])

        result.sort(key=lambda x: int(x.split()[1][1:]))
        return "\n".join(result)


solution = NiceMigration()
print(
    solution.convert(
        "20150602 #4516 + 20.02\n20150603 #4516 * 2\n20150605 #4516 / 2\n20150604 #4516 - 2"
    )
)
