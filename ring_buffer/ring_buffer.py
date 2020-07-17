class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data.pop(0)
            self.data.append(item)

    def get(self):
        return self.data