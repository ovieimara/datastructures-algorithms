def IsAlmostPalindrome(word):
    i = 0
    j = len(word) - 1

    count = 0
    while i <= j:
        print(word[i], word[j], i, j, count)
        if word[i] != word[j]:
            count += 1

        i += 1
        j -= 1

    return True if count <= 1 else False

word = 'aabccbax'

res = IsAlmostPalindrome(word)
print(res)