class MortgageCalculator:
    def get_repay_amt(self, mortgage, rate=0.05, year=20):
        return (rate * mortgage) / (1 - pow(1 + rate, -year))

    def is_eligible(self, mortgage, deposit) -> bool:
        return ((mortgage * 10) / 100) <= deposit

    def calculate_mortgage(self, salary1: int, salary2: int) -> int:
        return 5 * (salary1 + salary2)

    def get_totalrepay_amt(self, repay_amt, year=20):
        return year * repay_amt

    def get_total_time(self, annual_overpayment, repay_amt, year=20):
        total_cost = (year - 1) * annual_overpayment
        delta = self.get_totalrepay_amt(repay_amt) - total_cost
        return int(delta // repay_amt)

    def calculate_eligibility(
        self, number_of_people_on_mortgage, deposit, salary1, salary2, annual_overpayment
    ) -> list:
        if 0 > number_of_people_on_mortgage >= 2:
            return [0, 0, 0, 0]

        mortgage = self.calculate_mortgage(salary1, salary2)

        if not self.is_eligible(mortgage, deposit):
            return [0, 0, 0, 0]

        p = self.get_repay_amt(mortgage)
        total_repay = self.get_totalrepay_amt(p)
        total_time = self.get_total_time(annual_overpayment, p)

        return [mortgage, round(p, 2), round(total_repay, 2), total_time]
