import re


class SocialMediaSorter:
    def get_recipient(self, message, position):
        try:
            found = re.findall(r"@[_|-|a-z|A-Z|0-9]*", message)[position - 1]
            return found[1:]
        except IndexError:
            return ""
