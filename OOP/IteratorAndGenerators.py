class PowerOfTwo:
    def __init__(self, N):
        self.N = N

    def __iter__(self):
        self.current_n = 0
        return self

    def __next__(self):
        if self.current_n <= self.N:
            current_result = 2 ** self.current_n
            self.current_n += 1
            return current_result
        else:
            raise StopIteration


p = [power for power in PowerOfTwo(10)]
print(p)


def PowerOfTwoGenerator(N):
    currnet_n = 0
    while currnet_n <= N:
        yield 2 ** currnet_n
        currnet_n += 1


g = PowerOfTwoGenerator(10)
for i in g:
    print(i)

