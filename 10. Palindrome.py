# Variant 1
def isPalindrome(s):
 s = s.strip().lower()
 return s == s[::-1]
symbols = [
    "    aBC cba ",
    "a BCQcb a    ",
    " ab bca",
    "ab b a"
]
for symbol in symbols:
 print(isPalindrome(symbol))

#Variant 2
def is_palindrome1(s):
    s = s.strip().lower()
    if len(s) <= 1:
        return True
    if s[1] != s[-2]:
        return False
    if s[0] != s[-1]:
        return False
    return is_palindrome1(s[1:-1])
symbols1 = [
    "    aBC cba ",
    "a BCQcb a    ",
    " ab bca",
    "ab b a"
]
for symbol1 in symbols1:
    print(is_palindrome1(symbol1))