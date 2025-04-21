def minumWindowString(s,t):
    # THIS IS THE EDGING CASE WHERE NOTHING IS GIVEN 
    if t=="":
        return ""
    
    # THIS COUNT OF THE SEEN CHARACTERS IN GIVEN STRING AND MATCHES THE GIVEN "t"
    countT={}
    # THIS IS THE WINDOW OF WHICH PRESENT THE MATCHING CHARACTERS
    window={}
    for c in t:
        countT[c]=1+countT.get(c,0)
    # HAVE IS FOR HOW MANY CHRACTERS WE HAVE AND NEED IS FOR HOW MANY IS NEEDED
    have,need=0,len(t)
    # RES STORES THE WINDOW INDEX OF CHARACTERS &
    res,resLen=[-1,-1],float("infinity")
    # LEFT POINTER 
    l=0
    # RIGHT POINTER 
    for r in range(len(s)):
        # THIS IS CURRENT CHARACTER AT INDEX "r"(s[r]) IN GIVEN STRING "s"
        
        c=s[r]
        # print("current---->",c)
        # INCREMENT THE CHARACTER'S VALUE BY ONE 
        window[c]=1+window.get(c,0)
        # print("window[c]",window[c])
        # IF CHARACTER IS IN "c" AND "countT" & MATCHES IN BOTH DICT. "window" and "countT"
        # INCRMENT "have"
        if c in countT and window[c]==countT[c]:
            have+=1

        # DECREASE THE SIZE OF WINDOW UNTIL IT WE HAVE BOTH NEEDED CHARACTERS 
        while have==need:
            # THIS CONDITION CHECK WE HAVE THE MINIMUM WINDOW OF CHARACTERS
            if(r-l+1) <resLen:
                # TRACKS THE INDECIES REQUIRED FOR MINUM WINDOW
                res=[l,r]
                # THIS TRACKS THE WINDOW SIZE 
                resLen=r-l+1
            # DECREMENT LEFT POINTING CHRACTER'S VALUE BY ONE 
            window[s[l]] -=1
            # CHECKING BY DEREMENTING THE LEFT POINTER AND UNTIL REACHES THE LIMIT OF NECCESARY COUNT OF CHARACTERS
            if s[l] in countT and window[s[l]] <countT[s[l]]:
                # print("s[l] in countT and window[s[l]] <countT[s[l]]",s[l])
                have -=1
            l +=1
    # THIS ARE THE INDECIES OF THE CHRACTERS PRESENT IN GIVEN STRING "s"
    l,r=res
    # ONLY RETURN WHEN RESULT DONT HAVE INFINITY VALUE OR  "" 
    return s[l:r+1] if resLen != float('infinity ') else  ""

print(minumWindowString("WASUDEWANGAN",'SDU'))


"""

"""

"""
METHOD TO SOLVE THIS :
FIRST WE MOVE THROUGH THE RIGHT POINTER UNTIL WE GOT THE NEEDED COUNT OF CHARACTERS
THEN DECREMENT THE LEFT POINTER TO DECREASE AND GET THE MINIMUM WINDOW FOR THE MATCHING CHARACTERS
AND THEN RETURN THE INDECIES 

------------------------------------------------------------------------------------------------------------------
PSUEDO CODE 
------------------------------------------------------------------------------------------------------------------
1. MATCH THE EDING CONDITION FOR EMPTY STRING
2.DEFINE WINDOW AND COUNT-T DICT. FOR THE HASH MAP 
3.DEFINE HAVE AND NEED FOR COUNTS OF CHARACTERS SEEN AND NEEDED
4.DEFINE RES->FOR INDECIES AND RESLEN -> FOR THE RESULT LENGTH
5.DEFINE LEFT POINTER WITH STARTING VALUE OF ZERO 
6.LOOP THE RIGHT POINTER UNTIL REACHES THE END 
7.ADD THE SEEN CHARACTERS IN THE WINDOW DICT. AND IF CURRENT CHARACTER PRESENT IN THE COUNT-T AND WINDOW INCREASE HAVE BY ONE
8.ANOTHER LOOP FOR THE CHECKING THE CURRENT CHARACTER SATIFYS THE NEED OR NOT IF NOT THEN DECREASE THE THEN LEFT POINTER AND WINDOW SIZE
9.RETURN THE WINDOW
------------------------------------------------------------------------------------------------------------------

"""

