class RingBuffer:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.newest_index = 0

    def append(self, item):
        if self.newest_index == (len(self.storage)):
            self.newest_index = 0
            self.storage[self.newest_index] = item
            self.newest_index += 1
        else:
            self.storage[self.newest_index] = item
            self.newest_index += 1

    def get(self):
        return [item for item in self.storage if item is not None]

    def __len__(self):
        return len(self.storage)