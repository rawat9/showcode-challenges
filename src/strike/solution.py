class PlayerFrames:
    def get_score(self, input):
        def rollScore(index):
            if input[index] == "X":
                return 10
            elif input[index] == "/":
                return 10 - int(input[index - 1])
            else:
                return int(input[index])

        frames = 10
        score = 0

        for roll_i, roll in enumerate(input):
            if frames <= 0:
                return score

            frames -= 0.5

            if roll == "X":
                score += 10 + rollScore(roll_i + 1) + rollScore(roll_i + 2)
                frames -= 0.5
            elif roll == "/":
                score += rollScore(roll_i) + rollScore(roll_i + 1)
            else:
                score += int(roll)

        return score if frames <= 0 else -1
