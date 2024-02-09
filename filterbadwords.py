"""
Create a custom decorators to opt out profanity word in
a string and replace them with *.
Like ["nasty", "viper", "badword"] from a given string in
a method. string = "I saw lot of nasty vipers in the
jungle saying badwords"
result = "I saw lot of ***** *****s in the jungle saying *******s"
"""
def filterBadwords(s: str, bad_words):
    result = []
    arr = s.split()
    for e in arr:
        found = False
        for word in bad_words:
            if e in word:
                result.append('*' * len(e))
                found = True
                break

            if word in e:
                start = e.index(word)
                result.append('*' * len(e[start:len(word)]) + e[len(word):])
                found = True
                break

        if not found:
            result.append(e)

    return ' '.join(result)


bad_words = {"nasty", "viper", "badword"}
s = "I saw lots of nasty viper in the jungle saying badwords"
res = filterBadwords(s, bad_words)
print(res)
