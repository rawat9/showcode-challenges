class Solution:
    def __init__(self):
        self.items_dict = {}  # {item_code: [cost, quantity]}
        self.discounts_dict = {}

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

    def calculate_bag_total(self, items, discounts):
        self.populate(items)
        total_amount = 0

        for discount_code in discounts:
            item_code = self.get_item_code(discount_code)
            min_count = int(discount_code[3])

            if self.items_dict[item_code][1] > min_count:
                continue

            discount = self.__get_discount(item_code, discount_code)
            total_amount += self.items_dict[item_code][0] - discount

        return total_amount

    def __get_discount_category(self, discount_code):
        return discount_code[4]

    def __get_discount(self, item_code, discount_code):
        discount_category = self.__get_discount_category(discount_code)
        item_discount = int(discount_code[5:])

        if discount_category == "P":
            return self.items_dict[item_code][0] * (item_discount / 100)
        else:
            return item_discount


sol = Solution()
print(sol.calculate_bag_total(["ABC010", "DEF020", "ABC010"], ["ABC1P50", "DEF1C05"]))
