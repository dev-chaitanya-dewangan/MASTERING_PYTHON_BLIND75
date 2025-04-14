 def twoSum(self, nums: List[int], target: int) -> List[int]:

        # HASH TABLE COMPLEMENTARY NUMBERS AND THERE INDEX
        dictionary={} 


        for i in range(len(nums)): 

            #LOOP THOUGH ALL ELEMENTS AND CHECKING IF THERE IS 
            #ANY COMPLEMENTARY NUMBER PRESENT IN HASH MAP -> DICTIONARY  

            ##COMPLIMENT = REQUIRED VALUE TO THE THE TARGET NUMBER  
            compliment=target-nums[i] 
            # IF COMPLIMENT CONTAINS RETURN THE INDEX OF THOSE ELEMENTS
            if compliment in dictionary:
                return [dictionary[compliment],i]
            dictionary[nums[i]]=i
        

"""
TIME COMPLEXITY ->   O(N)
SPACE COMPLEXITY ->  O(N)
"""