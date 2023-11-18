def designerPdfViewer(h, word):
    # Write your code here
    # look_up = getLetterHeightDict(h)

    max_height = 0
    # for ch in word:
    #     max_height = max(max_height, look_up.get(ch, 0))

    # return max_height * len(word)

    for ch in word:
        max_height = max(max_height, h[ord(ch) - 97])

    return max_height * len(word)


def getLetterHeightDict(height):
    look_up = {}
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', '0', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    for h, ch in zip(height, alphabets):
        look_up[ch] = h

    return look_up