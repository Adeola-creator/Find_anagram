# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    if len(word) == len(anagram):
        for letter in word:
            if letter not in anagram:
                return False
        else:
            return True 
    else:
        return False                                
print(find_anagram("below", "elbow"))
print(find_anagram("hello","check"))
    

