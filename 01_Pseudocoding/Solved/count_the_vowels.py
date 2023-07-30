def count_the_vowels(str):
    ## initialize a counter variable to 0
    num_vowels = 0
    ## loop through each character in the string
    for char in str:
        ## if the char matches one of the vowels in uppercase or lowercase
        if char in "aeiouAEIOU":
            ## increment counter by one
            num_vowels = num_vowels + 1

    ## return  the  counter
    return num_vowels
