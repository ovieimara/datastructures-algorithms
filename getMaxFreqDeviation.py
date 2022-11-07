def getMaxFreqDeviation(s):
    charStore = {s[0]: 1}
    minSub = s[0]
    maxSub = s[0]
    minFreq = 1
    maxFreq = 1
    freqDeviation = 0

    for i in range(1, len(s)):
        char = s[i]
        if char == maxSub:
            print(maxFreq, minFreq)
            maxFreq += 1

        if char == minSub:
            minFreq += 1

        if char != minSub and char != maxSub:
            minFreq = 1
            minSub = char

        freqDeviation = max(freqDeviation, maxFreq - minFreq)
        print(maxFreq, freqDeviation, char, maxSub, minSub)

    return freqDeviation

s = 'aabb'
s = "bbacccabab"
s = "aaaaa"
s = "abdbcdacbcadbbe"
res = getMaxFreqDeviation(s)
print(res)


