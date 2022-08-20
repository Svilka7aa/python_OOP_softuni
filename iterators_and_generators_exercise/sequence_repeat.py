class sequence_repeat:
    def __init__(self, sequence, count):
        self.sequence = sequence
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.count:
            raise StopIteration
        result = self.sequence[self.index % len(self.sequence)]
        self.index += 1
        return result


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
