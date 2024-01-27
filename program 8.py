string1 = "Heart"

string2 = "Earth"

string1 = string1.lower()

string2 = string2.lower()

if(len(string1) == len(string2)):

    sorted_string1 = sorted(string1)

    sorted_string2 = sorted(string2)

    if(sorted_string1 == sorted_string2):

        print(True)

    else:

        print(False)