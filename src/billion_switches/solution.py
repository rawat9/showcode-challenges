from more_itertools import map_reduce, map_if


class Solution:
    def billion_switches(self, input):
        return sum(
            map(
                lambda x: -x[1] if x[0] % 2 != 0 else x[1],
                enumerate(input),
            )
        )


sol = Solution()
print(sol.billion_switches([100, 100, 99]))
