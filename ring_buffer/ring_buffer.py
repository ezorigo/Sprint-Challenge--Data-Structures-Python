class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.position = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        
        elif len(self.data) == self.capacity:
            self.data[self.position] = item
            if self.position + 1 == self.capacity:
                self.position = 0
            else:
                self.position += 1



    def get(self):
        return self.data
