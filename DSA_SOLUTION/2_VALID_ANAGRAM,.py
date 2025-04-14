# Here we are using the hash table which tracks the characters  
def isAnagram(s,t):
    if len(s)!=len(t): # Instantly return false when both strings length doesnt match
        return False
    count={} #stores characters of "s" 
    for char in s:
        count[char]=count.get(char,0)+1 #counts the character seen 
    for char in t:
        if char not in count: #Returns False if character doesn't match
            return False
        count[char]-=1 # removes the seen character count 
        if count[char]==0: 
            del count[char] # remove the character key from "count" dictionary if character count decreased to zero 
    return not count # if count have nothing left then TRUE or FAlSE then.

"""
TIME COMPLEXITY  -> O(N)
SPACE COMPLEXITY -> O(1)
"""