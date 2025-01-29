class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water = capacity
        result = 0
        for i, num in enumerate(plants):
            if water >= num:
                water -= num
                result += 1
            else:
                water = capacity
                result += i*2
                water -= num
                result += 1
        
        return result
                
            