def isPalindrome(s):
    # TRACKS THE POINTER "left" and "right"
    left,right=0,len(s)-1
    # LOOP UNTIL LEFT AND RIGHT MEET AT CENTER
    while left<right:
        # INCREMENT LEFT IF CURRENT(RIGHTS POINTER'S CHARACTER )  IS ALPHANUMERIC
        while left<right and s[left].isalnum():
            # print("s[left].isalnum():",s[left])
            left +=1
        # DECREMENT RIGHT("right") IF CURRENT(RIGHTS POINTER'S CHARACTER ) IS ALPHANUMERIC
        while left<right and s[right].isalnum():
            # print("s[right].isalnum():",s[right])
            right -=1 
        
        # CHECK IF EVEN IN LOWERCASE BOTH SIDES DOENST MATCH RETURN FALSE
        if s[left].lower() ==s[right].lower():
            return False
    return True

isPalindrome("A man, a plan, a canal: Panama")
"""
TIME COMPLEXITY   : O(N)
SPACE COMPLEXITY  : O(1)
"""
# ----------------------------------------------------------------------------

"""
----------------------------------------------------------------------------

METHOD TO SOLVE THIS 
TWO POINTER method->
STARTS WITH TWO POINTER FIRST AT START OF STRING AND SECOND AT LAST 
EVERY TIME WE LOOP THORUGH EACH CHARACT(WHICH IS ALPHANUMERIC) 
WE INCREMENT LEFT AND DECREMENT RIGHT POINTER UNTIL WE REACH THE CENTER 
->THEN CHECK IF EVEN IN LOWERCASE DOES NOT MATCH RETURN FALSE
WHEN WHOLE LOOP RUNS THROUGH ALL CHARACTERS THEN IT FUNTION WILL RETURN TRUE


----------------------------------------------------------------------------
PSUEDO CODE
1.DEFINE TWO POINTERS (left,right) FIRST STARTS WITH VALUE 0 AND SECOND STARTS WITH LAST INDEX OF GIVEN STRING
2.LOOP THOUGH POINTER UNTIL WE MEET AT CENTER 
3.BOTH FOR LEFT AND RIGHT CHECK IF CURRENT POINTING CHARACTER IS ALPHANUMERIC
-> THEN INCREMENT AND DECREMENT RESPECTIVE TO LEFT(left +=1) AND RIGHT(rigth -=1 ) 
4.CHECK IF IN LOWERCASE DOES LEFT AND RIGHT CHRACTER MATCHES OR NOT IF NOT THEN RETURN FALSE
5.RETURN TRUE AT LAST OF FUNTION (cause if previous if statement doesnt return false then this will trigger and return true)
"""