class FirstCircularBuffer:
    def __init__(self, size):
        self.size = size
        self.new = 0
        self.array = []

    def read(self):
        return self.array

    def write(self, value):
        if len(self.array) < self.size:
            self.array.append(value)
        else:
            self.array[self.new] = value
        self.new = self.new + 1
        if self.new > self.size - 1:
            self.new = 0

    def delete(self):
        self.array = []
        self.new = 0


class SecondCircularBuffer:
    def __init__(self, size):
        self.size = size
        self.new = 0
        self.old = 0
        self.array = []

    def read(self):
        return self.array

    def write(self, value):
        if len(self.array) < self.size:
            self.array.append(value)
        elif self.new == self.old:
            raise Exception("Circular buffer is full")
        else:
            self.array[self.new] = value
        self.new = self.new + 1
        if self.new > self.size - 1:
            self.new = 0

    def delete(self, number=1):
        if number > self.size:
            number = self.size
        for i in range(number):
            index = self.old + i
            if index > self.size - 1:
                index = index - self.size
            self.array[index] = None
        self.old = index + 1
        if self.old > self.size - 1:
            self.old = self.old - self.size
        if self.old == self.new:
            self.new = 0
            self.old = 0
            self.array = []
