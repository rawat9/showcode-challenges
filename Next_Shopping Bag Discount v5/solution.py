class Solution:
    def get_item_code(self, item: str) -> str:
        return item[:3]

    def get_item_cost(self, item: str) -> int:
        return int(item[3:])

    def calculate_bag_total(self, items, discounts) -> int:
        for discount_code in discounts:
            pass

        # for item in items:
        #     item_code = self.get_item_code(item)
        #     item_cost = self.get_item_cost(item)

    def is_qualified(self, item):
        return

    def __get_discount_category(self, discount_code):
        return discount_code[3]

    def __get_discount(self, item):
        pass

    def is_valid(self) -> int:
        '''
        Is the discount valid?
        '''
