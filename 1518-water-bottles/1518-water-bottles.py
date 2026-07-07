class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        ans=numBottles
        while(numBottles>=numExchange):
            full=numBottles//numExchange
            ans=full+ans
            numBottles=full+(numBottles%numExchange)
        return ans