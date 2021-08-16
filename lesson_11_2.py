class NullSituation:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f'Нельзя поделить на ноль')



div = NullSituation(10, 100)
print(NullSituation.divide_by_null(10, 0))
print(NullSituation.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
