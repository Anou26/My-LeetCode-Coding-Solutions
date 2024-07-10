import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val):
        """
        Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        """
        Removes an item val from the set if present. Returns true if the item was present, false otherwise.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        # Move the last element to the place idx of the element to delete
        last_element = self.list[-1]
        idx = self.dict[val]
        self.list[idx] = last_element
        self.dict[last_element] = idx
        # Remove the last element
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self):
        """
        Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called).
        Each element must have the same probability of being returned.
        :rtype: int
        """
        return random.choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
