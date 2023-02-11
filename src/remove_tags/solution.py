import re


class Solution:
    def remove_tags(self, input):
        html_tags = re.findall("<[^>]*>", input)
        for tag in html_tags:
            input = input.replace(tag, "")

        return input
