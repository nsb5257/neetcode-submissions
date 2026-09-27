class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if groupSize == 1:
            return True
        if n % groupSize != 0:
            return False
        
        count = Counter(hand)
        for card in sorted(count):
            if count[card] > 0:
                k = count[card]
                for i in range(card, card + groupSize):
                    if count[i] < k:
                        return False
                    count[i] -= k
        return True