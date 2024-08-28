'''Given a string composed of lowercase alphabetic characters, each character in the string represents a personality trait. The alphabet can be mirrored such that the character 'a' is paired with 'z', 'b' with 'y', 'c' with 'x', and so on. A "mirror personality" is said to exist between two characters if one is the mirror image of the other according to this mapping.
#This code gives a function which count the total number of unique mirror personality pairs in the string. Note that pairs (i, j) and (j, i) are considered the same and should only be counted once.
#For example, given the string "abczyx", the mirror personality pairs are (a, z), (b, y), and (c, x), resulting in a total of 3 mirror personality pairs.'''
#Code
import string

def mirror_personality(people):
    a = string.ascii_lowercase #fetching all lowercase alphabets as a string
    b = a[::-1] 
    mirror = {a[i]:b[i] for i in range(len(a))}#mapping a:z; b:y; etc.
    count = 0
    seen = {}#maintains the count of each char as key value pair
    for char in people:
        mirror_char = reverse_map.get(char, '')
        if char in seen:
            seen[char]+=1 #increase the count associated with that character in seen
        else:
            seen[char] = 1
        if mirror_char in seen:
            count+=seen_chars[reverse_char]
    return count
people = input()
result = mirror_personality(people)
print(result)
