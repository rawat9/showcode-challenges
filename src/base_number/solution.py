import numpy as np


class Solution:
    def convert_base_ten(self, input, targetBase):
        if targetBase == 10:
            return input

        if targetBase < 2 or targetBase > 36:
            return "INDETERMINATE"

        return np.base_repr(input, targetBase)
