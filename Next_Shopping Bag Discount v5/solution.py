class Solution:
    def __init__(self) -> None:
        self.items_dict = {}  # {item_code: [cost, quantity]}
        # self.populate()

    def get_item_code(self, item: str) -> str:
        return item[:3]

    def get_item_cost(self, item: str) -> int:
        return int(item[3:])

    def populate(self, items):
        for item in items:
            item_cost = self.get_item_cost(item)
            item_code = self.get_item_code(item)

            if item_code in self.items_dict:
                self.items_dict[item_code][0] += item_cost
                self.items_dict[item_code][1] += 1
            else:
                self.items_dict[item_code] = [item_cost, 1]

        return self.items_dict

    def calculate_bag_total(self, items, discounts):
        items_dict = {}  # {item_code: [cost, quantity]}

        for item in items:
            item_cost = self.get_item_cost(item)
            item_code = self.get_item_code(item)

            if item_code in items_dict:
                items_dict[item_code][0] += item_cost
                items_dict[item_code][1] += 1
            else:
                items_dict[item_code] = [item_cost, 1]

        return items_dict

    def is_qualified(self, item):
        return

    def __get_discount_category(self, discount_code):
        return discount_code[3]

    def __get_discount(self, item):
        pass


sol = Solution()
print(sol.calculate_bag_total(["ABC015", "DEF020", "ABC010"], ["ABC2P50", "DEF1C05"]))
