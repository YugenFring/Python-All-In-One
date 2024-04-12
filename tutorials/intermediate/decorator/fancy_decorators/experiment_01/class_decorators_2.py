from decorators import timer

# Decorate a class.
@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([number**2 for number in range(self.max_num)])