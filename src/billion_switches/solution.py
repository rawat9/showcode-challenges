class Solution:
    def billion_switches(self, input):
        return sum(
            map(
                lambda x: -x[1] if x[0] % 2 != 0 else x[1],
                enumerate(input),
            )
        )
