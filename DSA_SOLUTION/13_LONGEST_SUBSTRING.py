def longestSubtring(s):
    # DEFINE CHARSET WHICH TRACKS THE CHRACTERS
    charSet=set()
    left=0
    result=0
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left+=1
        charSet.add(s[right])
        result=max(result,right-left+1)
    # return result
    # print(charSet,result,left,right,s[left],s[right])
longestSubtring("abccdasc")


"""
TIME COMPLEXITY  :O(N)
SPACE COMPLEXITY :O(M)
"""

"""
METHOD TO SOLVE THIS :
WE TRACK THE POINTERS OF LEFT AND RIGHT POINTING CHARACTERS AND IF RIGHT POINTING CHARCTER IS IN 
CHARACTER SET(which tracks only the novel character from given string) WE INCREMENT THGE LEFT AND CHECK FOWARD UNTIL END OF STRING
WHILE COMPARING THE RESULT AND THE RIGHT - LEFT - 1(which is the longest string we got)
--------------------------------------------------------------------------------------------------------------
PSUEDO CODE
1.DEFINE CHARSET,RESULT(with 0 value) LEFT & RIGHT POINTER 
2.LOOP UNTIL REACHES THE END OF STRING 
3.IF CURRENT CHRACTER IS SAME AS IN CHARSET THEN REMOVE THE CHARACTER(s[left]-> which is same as the right one) AND ALSO INCRMENT THE LEFT POINTER 
4.ADD THE CURRENT(s[right]) CHARACTER TO THE CHARACTER SET(charSet)
5.COMPARE CURRENT INDEX(which have the longest substring -> right -left -1) NAD THE RESULT AND UPDATE WHICH IS GREATER
6.RETURN THE RESULT 
--------------------------------------------------------------------------------------------------------------
"""