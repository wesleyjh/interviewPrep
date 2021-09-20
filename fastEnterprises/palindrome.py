
def fastPalindromeCheck(x):
    if x == x[::-1]:
        return True
    return False

word = 'racecar'
wordTwo = 'race car'

print(fastPalindromeCheck(word))
print(fastPalindromeCheck(wordTwo))