def hasDuplicate(nums):
    frequency={} # This stores which have seen and how many time number from list accured
    for number in nums:
        if number in frequency: #Checks if number contains in frequency{dictionary} or not 
            return True
        frequency[number]=1
    return False

"""

TIME COMPLEXITY   -> O(N)
SPACE COMPLEXXITY -> O(N)
"""