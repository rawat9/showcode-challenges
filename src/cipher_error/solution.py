from itertools import groupby


class Solution:
    def split_string_on_change(self, CipherString):
        return (
            " ,".join(list(map("".join, [list(g) for _, g in groupby(CipherString)])))
            + " "
        )
