
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count = defaultdict(int)
        left = max_fruits = 0

        for right, fruit in enumerate(fruits):
            count[fruit] += 1

            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                if count[left_fruit] == 0:
                    del count[left_fruit]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
