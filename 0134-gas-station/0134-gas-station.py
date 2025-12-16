class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        curr_gas = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_gas += diff
            curr_gas += diff

            if curr_gas < 0:
                start = i + 1
                curr_gas = 0

        return start if total_gas >= 0 else -1