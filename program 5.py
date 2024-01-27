def isPalindrome(s):

    return s == s[: : -1]

s = "RACECAR"

answer = isPalindrome(s)

if answer:

    print("True")

else:

    print("False")