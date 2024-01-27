def countDis(str):
    
    #Stores all distinct characters
    s = set(str)
    
    #Returns the size of the set
    return len(s)

if __name__ == "__main__":

    S = "Guvi Geeks Private"

    print("Number of unique characters are:")

    print(countDis(S))