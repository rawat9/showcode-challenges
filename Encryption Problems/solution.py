class Solution:
    def __transform(self, string, func):
        # apply function func to string
        return "".join(list(map(func, string)))

    def handle_file(self, fileName):
        i = 0
        res = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        while i < len(fileName):
            # case 1
            if fileName[i] == "(":
                # find the index of closing bracket of the corresponding open bracket
                closing_index = fileName.find(")", i)

                # text between the brackets
                to_convert = fileName[i + 1 : closing_index]

                def goDownBy7(to_convert):
                    ans = ""
                    for char in to_convert:
                        ans += alphabet[alphabet.index(char) - 7]
                    return ans

                res += self.__transform(to_convert, goDownBy7)
                i += closing_index - i + 1

            # case 2
            elif fileName[i] == "<":
                # find the index of closing bracket
                closing_index = fileName.find(">", i)

                # text between the brackets
                to_convert = fileName[i + 1 : closing_index]

                def goUpBy2(to_convert):
                    ans = ""
                    for char in to_convert:
                        ans += alphabet[alphabet.index(char) + 2]
                    return ans

                res += self.__transform(to_convert, goUpBy2)
                i += closing_index - i + 1

            # case 3
            elif fileName[i] == "{":
                closing_index = fileName.find("}", i)
                to_convert = fileName[i + 1 : closing_index]

                # reverse to_convert
                res += to_convert[::-1]
                i += closing_index - i + 1
            else:

                # for anything else other than ( , < , {
                res += fileName[i]
                i += 1

        return res
