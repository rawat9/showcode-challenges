from typing import List


class Solution:
    def __reverseDigits(self, num: int):
        return int(str(num)[::-1])

    def verifypr(self, PR: List[str]):
        stack = []

        for commit in PR:
            sequenceNumber, commitMessage, fileValue, hashValue = commit.split(",")

            # 1st check
            if stack:
                prev = stack.pop()
                if int(sequenceNumber, 16) != int(prev, 16) + 1:
                    return False

            stack.append(sequenceNumber)

            # 2nd check
            ticket_number, type_change, description = commitMessage.split("-")

            if len(ticket_number) != 4:
                return False

            if type_change not in ("fix", "feat", "chore", "refactor"):
                return False

            if description == "":
                return False

            remainder = int(fileValue) % 151
            calculated_hashValue = self.__reverseDigits(remainder)

            if calculated_hashValue != int(hashValue):
                return False

        return True
