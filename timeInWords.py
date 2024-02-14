

def timeInWords(h, m):
    num2word = {0 : 'o\' clock', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one',
     22: 'twenty two', 23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight',
     29: 'twenty nine', 30: 'half'}

    h = int(h)
    m = int(m)
    first  = 'past' if 1 <= m <= 30 else "to"
    if 30 < m <= 59:
        m = 60 - m
        if h < 12:
            h += 1
        else:
            h = 1

    word_m = num2word.get(m)
    word_h = num2word.get(h)

    minu = '' if m == 15 or m == 30 else 'minute ' if m == 1 else 'minutes '

    return f'{word_m} {minu}{first} {word_h}' if m > 0 else f'{word_h} {word_m}'

h = 5
m = 0
m = 1
m = 10
m = 15
m = 30
m = 40
m = 45
m = 47
m = 28

h = 3
m = 00

h = 7
m = 15

h = 11
m = 59

h = 12
m = 00
m = 15
m = 30
m = 45

h = 11
m = 15
m = 30
m = 45

h = 6
m = '01'

h = 3
m = 15
m = 45



print(timeInWords(h, m))


