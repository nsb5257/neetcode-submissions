class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        ans = 0
        gas_rem=0
        i=0
        while i<n:
            gas_rem += gas[i]
            if gas_rem < cost[i]:
                ans = i+1
                gas_rem = 0
            else:
                gas_rem -= cost[i]
            i+=1

        return ans if ans < n else -1