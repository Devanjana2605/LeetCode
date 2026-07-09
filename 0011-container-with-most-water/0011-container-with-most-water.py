'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l1=[]
        for i in range(len(height)):
            for j in  range(i+1,len(height)):
                a=min(height[i],height[j])
                num = a*(j-i)
                l1.append(num)
        return max(l1)
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        maxArea=0
        i=0
        j=n-1
       
        while (i<j):
            
            area=(j-i)*min(height[i],height[j])
            maxArea=max(area,maxArea)
        
            if height[i]<height[j]:
                i+=1

            else:
                j-=1

        return maxArea