from typing import List

def reverseWords(s: str) -> str:
    reverse: str = ""
    words: List[str] = s.split(" ")
    for i in range(len(words)-1, -1, -1):
        reverse += " "
        reverse += words[i]
    return reverse

def largestOddNumber(nums: str) -> str:
    for i in range(len(nums)-1, -1, -1):
        if int(nums[i]) % 2 != 0:
            return nums[0:i+1]
    return ""

def canConstruct(ransomNote: str, magazine: str) -> bool:
    bag: dict[str, int] = {}
    for s in magazine:
        if s in bag:
            bag[s] += 1
        else:
            bag[s] = 1
    for s in ransomNote:
        if s not in bag or bag[s] == 0:
            return False
        else:
            bag[s] -= 1
    return True

def mergeAlternately(s1: str, s2: str) -> str:
    newStr: str = ""
    i: int = 0
    while i < len(s1) or i < len(s2):
        if i < len(s1):
            newStr += s1[i]
        if i < len(s2):
            newStr += s2[i]
        i += 1
    return newStr

def reverseString(s: List[str]) -> None:
    for i in range(len(s)//2):
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]

def reverseVowels(word: str) -> str:
    s: List[str] = list(word)
    vowels: str = "aeiouAEIOU" 
    i: int = 0
    j: int = len(s) - 1
    while i <= j:
        if s[i] not in vowels:
            i += 1
        if s[j] not in vowels:
            j -= 1
        elif s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return "".join(s)

def removeStars(s: str) -> str:
    res: List[str] = []
    i: int = 0
    while i < len(s):
        if s[i] != "*":
            res.append(s[i])
        else:
            res.pop(-1)
        i += 1
    return "".join(res)

def isPalindrome(s: str) -> bool:
    ls: List[str] = list(s.lower())
    i: int = 0
    j: int = len(ls) - 1
    while i <= j:
        if not ls[i].isalnum():
            i += 1
        elif not ls[j].isalnum():
            j -= 1
        else:
            if ls[i] != ls[j]:
                return False
            i += 1
            j -= 1
    return True
