def topKFrequentElement(nums,k):
    # ->STORE THE VALUE OF NUMBER OF TIME THE NUMBER SEEN 
    count ={}
    # ->N+1 LENGTH EMPTY LISTS   
    freq=[[] for i in range(len(nums)+1)] 

    # ->IF SEEN CURRENT NUMBER THEN INCREMENTS ONE VALUE
    for n in nums: 
        count[n]=1+count.get(n,0)
    # ->THIS IS KEY VALUE PAIR WHERE KEY "n" IS "number" AND "c" IS COUNT OF NUMBER OF TIME SEEN
    # for example -> {12:1}(times) 
    for n,c in count.items():
        # CODE_VISUALIZE:print(":;APPEND->",n,"FREQ[C]->",c)
        freq[c].append(n) # IN FREQUENCY FOR EVERY COUNT (from the "c" which is count of number ) at index "c" IT APPENDS NUMBER "N"
    result=[]
    # IT APPENDS THE COUNTS OF NUMBER UNTIL IT IS EXACTLY SAME AS GIVEN NUMBERS 
    # BY LOOPING BACKWARDS
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            print("->",n,"FREQ[I]->",freq[i])
            result.append(n)
            if len(result)==k:
                return result


print(topKFrequentElement([1,5,2,3,7,3,8,0,7,12,12], 2))


"""
TIME COMPLEXITY  ->O(N)
SPACE COMPLEXITY ->O(N)
"""

"""

METHOD TO SOLVE THIS :
WE HAVE An LIST OF EMPTY LISTS (ex. freq=[[],[],....n]) ,
WHERE EVERY INDEX REPRESENTS COUNT(number of times seen) WHERE WE APPEND THE NUMBER,


---------------------------------------------------------------------------------------
PSUEDO CODE 
1.DEFINE COUNT DICTIONARY AND FREQUNCY LIST 
2.LOOP THORUGH "n" AND PUT AND CHECK IF IN DICT THE INCREMENT IF NOT ADD IT WITH VALUE OF int value-> "1"
3.FOR KEY AND VALUE IN DICT (count.items()) FOR EVERY "n" NUMBER APPEND AT INDEX "c" WHICH IS COUNT
4.LOOP BACKWARDS STARTING FROM HIGHEST COUNT FREQUENCY THEN RETURN K NUMBER OF ITEMS FROM LIST 

"""