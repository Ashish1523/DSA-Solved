class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(fruits)
        count=0
        visited=[False]*n

        for fruit in fruits:
            for j in range(n):
                if not visited[j] and baskets[j]>=fruit:
                    count+=1
                    visited[j]=True
                    break
        return n-count