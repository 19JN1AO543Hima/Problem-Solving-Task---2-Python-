string = "Hello World! I am Hima Sai Varshitha"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

result = " "

for i in range(len(string)):

    if string[i] not in vowels:

        result = result + string[i]

print("After removing Vowels: ")

print(result)