def validParenthesis(s):
    # THIS TRACKS THE VALID PARENTHESIS 
    stack=[]
    # MATCHING REVERSE PARENTHESIS MAP
    closeToOpen={"]":"[","}":"{",")":"(",}
    # LOOP THORUGH ALL GIVEN PARENTHESIS
    for p in s:
        print("--------------stack",stack)
        # WHEN IT'S A CLOSING PARENTHESIS
        if p in closeToOpen:
            # IF CURRENT ONE MATCHES THE IN THE "stack" ---> THEN IT REMOVES IT FROM LAST
            if stack and stack[-1]==closeToOpen[p]:
                stack.pop()
            # ELSE IF DOESNT MATCH RETURN'S FALSE
            else:
                return False
        # IT APPENDS UNTIL ALL OPENINGS ARE ADDED
        else:
            stack.append(p)
        # RETURN TRUE WHEN STACK IS EMPTY MEANS ALL MATCHES AND ITS VAlID
    return True if not stack else False
validParenthesis('{[()]}')

"""
TIME  COMPLEXITY -->O(n)
SPACE COMPLEXITY -->O(n)
"""


"""
METHOD TO SOLVE :
ADD UNTIL ALL OPENINGS ARE ADDED IN IN STACK THEN IF CLOSING BRACKETS MATCHES THE MAP THEN START REMOVING FROM LAST
UNTIL IT'S EMPTY
"""

