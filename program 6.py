def LcSubStr(A, B, c, d):

    LcSuffix = [[0 for k in range(d + 1)]for l in range(c + 1)]

    result = 0

    for i in range(c + 1):
        
        for j in range(d + 1):

            if(i == 0 or j == 0):

                LcSuffix[i][j] = 0
            
            elif (A[i - 1] == B[ j - 1]):

                LcSuffix[i][j] = LcSuffix[i - 1][j - 1] + 1

                result = max(result, LcSuffix[i][j])

            else:

                LcSuffix[i][j] = 0
    
    return result

A = "applepie"

B = "applepieces"

c = len(A)

d = len(B)

print("Length of Longest Common Substring is: ") 

print(LcSubStr(A, B, c, d))