class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
       
        while hand:
            group = 0

            first = hand[0]
            # Try to form a group of size groupSize starting from 'first'
            for i in range(groupSize):
                card = first + i
                if card in hand:
                    hand.remove(card)
                else:
                    return False
        
        return True