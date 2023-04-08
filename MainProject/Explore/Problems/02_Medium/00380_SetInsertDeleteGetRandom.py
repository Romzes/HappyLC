# Medium 380. Insert Delete GetRandom O(1)
# Implement the RandomizedSet class:
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

import random

class RandomizedSet:
    def __init__(self):
        self.DICT, self.LIST = {}, []

    def insert(self, val):
        if val in self.DICT: return False
        self.DICT[val] = len(self.LIST)
        self.LIST.append(val)
        return True

    def remove(self, val):
        i = self.DICT.pop(val, None)
        if i is None: return False
        if i != len(self.LIST)-1:
            u = self.LIST[-1]
            self.LIST[i], self.DICT[u] = u, i
        self.LIST.pop()
        return True

    def getRandom(self): return random.choice(self.LIST)
    # def getRandom(self): return self.LIST[random.randint(0, len(self.LIST)-1)]

obj = RandomizedSet()
print(obj.insert(1))
print(obj.getRandom())
print(obj.insert(1))
print(obj.remove(2))
print(obj.remove(1))
# param_3 = obj.getRandom()