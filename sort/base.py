from comparator.oracle import Oracle

class Sort:
    def __init__(self, comparator=Oracle()):
        self.compare = comparator.compare

    def sort(self, arr):
        raise NotImplementedError("You must implement the sort method")