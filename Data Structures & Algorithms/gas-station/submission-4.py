class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        def f(i):
            if cost[i] > gas[i]:
                return False
            og = i
            gas_rem = gas[i]-cost[i]
            i+=1
            if i == n:
                i = 0
            while gas_rem>0 and i != og:
                gas_rem+=gas[i]-cost[i]
                if i == n-1:
                    i = 0
                else:
                    i+=1
            if i == og:
                    return True
            return False

        for i in range(n):
            if f(i):
                return i


        return -1