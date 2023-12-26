"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

"""

ransomNote = "aap"
magazine = "abdsagfdhdjpht"

if len(ransomNote) < len(magazine):
    t = True
    for i in range(len(ransomNote)):
        if magazine.find(str(ransomNote[i])) > -1:
            magazine = magazine[0:magazine.index(ransomNote[i])] + magazine[magazine.index(ransomNote[i]) + 1:]
        else:
            t = False
else:
    t = False

print(t)
