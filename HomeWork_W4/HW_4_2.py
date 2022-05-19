class ReverseIter(object):
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index = self.index - 1
        else:
            raise StopIteration
        return self.iterable[self.index]


my_list = ReverseIter([i for i in range(100, 200, 3) if i % 2 != 0])

for digit in my_list:
    print(digit)

# 2) Визначте клас ітератор ReverseIter, який приймає список та ітерується за ним у зворотному напрямку
