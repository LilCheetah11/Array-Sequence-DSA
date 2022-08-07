# def reverse(arr):
#     index_last_element=len(arr)-1
#     reverse_arr=[]
#      for num in 



def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    """
    
    words = []
    length = len(s)
    spaces = [' ']
    
    # Index Tracker
    i = 0
    
    # While index is less than length of string
    while i < length:
        
        # If element isn't a space
        if s[i] not in spaces:
            
            # The word starts at this index
            word_start = i
            
            while i < length and s[i] not in spaces:
                
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1
        
    # Join the reversed words
    return " ".join(words[::-1])

print(rev_word3('   Hello John    how are you   '))

"""MY Solution"""
# def rev_word3(s):

#     # Manually Splitting the words
    
#     # Start
#     words=[]
#     spaces=[" "]
#     length=len(s)

#     # index tracking
#     i=0

#     while i<length:
#         if s[i] not in spaces:
    
#             word_start=i
#             while i<length and s[i] not in spaces:
#                 i+=1
#             words.append(s[word_start:i])

#         i+=1

#     return " ".join(reversed(words))


# print(rev_word3('   Hello John    how are you   '))
