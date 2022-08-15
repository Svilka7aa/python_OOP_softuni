class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current_value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value > self.end:
            raise StopIteration
        value_to_return = self.current_value
        self.current_value += 1
        return value_to_return


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
