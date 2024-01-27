test_str = "Gentler"

print("The given string is: " + test_str)

all_freq = {}

for i in test_str:

    if i in all_freq:

     all_freq[i] += 1

    else:
       
     all_freq[i] = 1

result = max(all_freq, key = all_freq.get)

print("The most frequent of all characters in Gentler is: " + str(result))