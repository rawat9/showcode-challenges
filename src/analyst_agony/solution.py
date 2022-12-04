class Solution:
    def _get_open_price(self, trades: list[str]) -> str:
        return trades[0].split(",")[1]

    def _get_close_price(self, trades: list[str]) -> str:
        return trades[-1].split(",")[1]

    def _get_volume(self, trades: list[str]) -> str:
        return str(sum(map(lambda x: int(x.split(",")[2]), trades)))

    def _get_high_price(self, trades: list[str]):
        prices = list(map(lambda x: float(x.split(",")[1]), trades))
        return f"{max(prices):.4f}"

    def _get_low_price(self, trades: list[str]):
        prices = list(map(lambda x: float(x.split(",")[1]), trades))
        return f"{min(prices):.4f}"

    def split_by_hour(self, trades):
        next_hour = lambda n: n + (60 - n % 60)
        last_min = int(trades[-1].split(",")[0])
        groups = []
        start = 0

        for interval in range(start, next_hour(last_min) + 1, 60):
            a = []
            for trade in trades:
                mins = int(trade.split(",")[0])

                if mins <= interval:
                    a.append(trade)

            start += 60
            groups.append(a)

        return groups

    def aggregate_ohlcv(self, trades: list[str]) -> list[str]:
        data = [
            self._get_open_price(trades),
            self._get_high_price(trades),
            self._get_low_price(trades),
            self._get_close_price(trades),
            self._get_volume(trades),
        ]

        return [",".join(["0", *data])]


sol = Solution()
trades = [
    "0,12.5000,50",
    "25,10.2000,100",
    "45,14.8000,20",
    "59,13.1000,30",
    "60,14.2000,50",
    "75,14.3000,20",
    "100,14.1000,10",
    "118,13.9000,20",
]

print(sol.split_by_hour(trades))
t = [0, 25, 45, 59, 60, 75, 100, 118]
