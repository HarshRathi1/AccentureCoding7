'''char*MoveHyphen(char str[],int n);
The function accepts a string “str” of length ‘n’, that contains alphabets and hyphens (-). Implement the function to move all hyphens(-) in the string to the front of the given string.
NOTE:- Return null if str is null.
Example :-
Input:
str.Move-Hyphens-to-Front
Output:
—MoveHyphenstoFront
Explanation:-
The string “Move-Hyphens -to-front” has 3 hyphens (-), which are moved to the front of the string, this output is “— MoveHyphen”'''
str="Move-Hyphens-To-Front"
n=len(str)
def charMoveHyphen(str,n):
    a = []
    if n<1:
        return "null"
    else:
        for i in str:
            if i == '-':
                a.append(i)
        for j in str:
            if j != '-':
                a.append(j)
        s = ''
        for i in a:
            s += i
    return s
print(charMoveHyphen(str,n))
