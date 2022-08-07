def uni_char(s):
    # """Solution 1""""
    # return len(set(s))==len(s)

    """Solution 2"""
    # Checking Edge cases
    if len(s)==1:
        return True

    # set is a type array which is unordered, unchangeable ,unidexed and has unique elements.
    char=set()

    for letter in s:
        if letter in char:
            return False

        else:
            char.add(letter)    

    return True        

print(uni_char("ahg"))