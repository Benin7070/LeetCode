class RandomizedSet:

    def __init__(self):
        self.li=[]

    def insert(self, val: int) -> bool:
        if val not in self.li:
            self.li.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.li:
            self.li.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        if not self.li:
            return "null"
        else:
            res=random.choice(self.li)
            return res


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
