def palindrome(word):
    word = word.lower()
    return word[::-1] == word


print(palindrome("hello"))
print(palindrome("qazaq"))
