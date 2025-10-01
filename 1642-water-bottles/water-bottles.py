class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty=0
        while numBottles>=numExchange:
            empty+=numExchange
            numBottles-=numExchange
            numBottles+=1
        return empty+numBottles