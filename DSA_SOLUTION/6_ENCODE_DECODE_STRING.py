def encode(strs):
        res=''
        for word in strs:
            res +=str(len(word) )+ '#'+word
        return res
def decode(strs):
    res=[]
    i=0
    while i< len(s):
        j=i
        while s[j]!='#':
            j+=1
        length=int(s[i:j])
        word=s[j+1:j+1+length]
        res.append(word)
        i=j+1+length
    return res


"""
ENCODE :
TIME COMPLEXITY  :O(L) L stands for the total number of characters in the original, unencoded strings.
SPACE COMPLEXITY :O(L)
DECODE :
TIME COMPLEXITY  :O(L)
SPACE COMPLEXITY :O(L)
"""


"""
METHOD FOR THIS 
ENCODING GIVEN LIST OF STRINGS INTO THIS FORMAT ->"length#word" WHERE LENGHT IS WORD LENGTH THEN 
# SEPRATER THEN WE HAVE THE WORD

DECODING ->WHEN DECODING WE START LOOP THORUGH ALL CHARCTERS UNTIL WE GET THE # 
THEN  RETURN THE DECODED LIST 


--------------------------------------------------------------------
PSUEDO CODE :
ENCODE ->
1.ENOCDE THE STRING INTO "<lengthOFword>#<word>" FORMAT THEN RETURN BACK THE STRING
DECODE ->
1.LOOP THORUGH ALL CHARCTERS UNTIL WE GET #
2.DEFINE LENGTH WHICH SPLITS THE STRING INTO THE LENGTH OF THE WORD 
3.DEFINE WORD WHICH REPRESENTS THE WORDS BY GIVEN SPLITTING OF WORD FROM "encode string"
4.APPEND IT INTO RESULT 
5.INCREMENT THE LENGTH FROM CURRENT + LENGTH OF WORDS +1
6.RETURN THE RESULT
"""