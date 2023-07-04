class ReverseString:
    def __init__(self, string):
        self.__s = string

    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        if self.__i > len(self.__s) -1:
            raise StopIteration
        else:
            a = self.__s[-self.__i - 1]
            self.__i += 1
            return a


if __name__ == '__main__':
    s = ReverseString('hello')
    for c in s:
        print(c, end='')

# olleh
