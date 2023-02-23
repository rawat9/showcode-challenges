class Solution:
    def secret_value(self, SortedArray, SecretValue):
        return str(self.binary_search(SortedArray, SecretValue))

    def binary_search(self, SortedArray, SecretValue):
        i = 0
        j = len(SortedArray) - 1
        while i <= j:
            m = (i + j) // 2
            if SortedArray[m] == SecretValue:
                return m
            elif SortedArray[m] < SecretValue:
                i = m + 1
            else:
                j = m - 1
        return -1
