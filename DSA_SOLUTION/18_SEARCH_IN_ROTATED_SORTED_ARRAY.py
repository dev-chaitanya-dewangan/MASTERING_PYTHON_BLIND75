def search(nums,target):
    l,r=0,len(nums)-1
    while l<=r:
        m=(l+r)//2
        if target==nums[m] :
            # RETURN THE INDEX OF WHICH IS TARGET
            return m
        if nums[l] <= nums[m]: #IT MEANS THIS SIDE IS SORTED
            # CHECK IF TARGET IS GREATER THAN MID OR LESSER THAN LEFT MOST POINTER-->
            # SHIFT LEFT POINTER TO THE RIGHT SIDE 
            if target > nums[m] or target < nums[l]:
                l = m +1 #THIS IS FOR RIGHT SIDE
            else:
                # SHIFT RIGHT POINTER TO THE LEFT SIDE 
                r=m-1 #THIS IS FOR LEFT  SIDE
        else:#IT MEANS THIS SIDE nums[l] > IS SORTED 
            if target < nums[m] or target > nums[r]:
                r=m-1
            else:
                l=m +1
    # RETURN -1 IF WE DONT FIND ANY VALUE IN ARRAY
    return -1


"""
TIME COMPLEXITY :O( LOG N )
"""

"""
METHOD TO SOLVE THIS 
EVERYTIME ITERATION TAKES HALF TIME 
FIRST PIVOT POINT FROM THE ARRAY IS SORTED (WHICH CAN BE DECIDE BY MID POINT AND CHECKING WHICH SIDE IS  LESS OR MORE THAN MID )
THEN ASIGN POINTERS ONE IN LEFT(STARTING) AND ANOTHER IN RIGHT (LAST)
EVERY TIME WE CHECK IF ITS TARGET IF NOT THEN GREATER OR LESSER THAN MID THEN ACCRODING TO THAT WE SHIFT LEFT AND RIGHT POINTER UNTIL WE FIND THE TARGET 
VALUE.

"""

