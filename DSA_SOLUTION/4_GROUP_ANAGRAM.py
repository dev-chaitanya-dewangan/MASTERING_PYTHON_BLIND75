def groupAnagram(strs):
    # STORE THE KEY OF COMBINATION OF CHARCTERS AND COUNT OF THERE CHARACTERS
    # RESULT={
    #     key:list of of all matching words 
    #        }
    result={} 
    
    # ->FOR EVERY WORD IN "strs" CHECKING IF THIS MATCHING 
    for word in strs: 
        # ->"count" IT IS LIST OF ZEROS FOR A-Z CHARACTERS
        count=[0]*26 
        # ->IT CHECKS THE CHARCTER IN CURRENT WORD AND COUNTS THEM
        for c in word: 
            # ->IT CONVERTS CHARACTER INTO ASCII VALUE AND SUBTRACT WITH THE ASCII VALUE OF a
            index=ord(c)-ord('a') 
            count[index] +=1
        # ->KEY IS CONVERTING INTO TUPLE AND FOR RESULT 
        key =tuple(count)
       # -> IF KEY NOT PRESENT IN RESULT THEN ADDS EMPTY LIST
        if key not in result:
            result[key]=[]
        # -> IF RESULT HAVE MATCHING KEY THEN APPEND IT THAT MATCHING KEY 
        result[key].append(word)
    # RETURNS ALL VALUES FROM RESULT WHICH IS LIST OF THE GORUP ANAGRAM WORDS 
    return list(result.values()) 




"""
---------------------------------------------------------------------

MEHTOD FOR SOLVING THIS :
We are craeting key for words 
RESULT = {KEY:[LIST OF WORD]}
THEN IF THE WORDS WORD IS MATCHING THE KEY ADD IT TO THE LIST

---------------------------------------------------------------------
PSUEDO CODE :
1.DEFINE RESULT DICTIONARY ,WHICH STORES KEYS AND MATCHING WORDS
2.LOOP THROUGH ALL THE WORDS IN GIVEN LIST 
3.INSIDE THE LOOP OF WORDS CHECK EVERY CHARACTER AND ADD IT TO THE "count" WHICH IS LIST OF 26 ZEROS
4.DEFINE KEY WHICH IS IS TUPLE OF "count" 
5.CHECK IF KEY EXIST THEN ADD THE CURRENT WORD IF NOT THEN CREATE A NEW KEY WITH VALUE OF EMPTY LIST THEN ADD IT 
6.RETURN ALL THE VALUE OF RESULT(dictionary)
"""
