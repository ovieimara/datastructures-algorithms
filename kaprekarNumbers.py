

def kaprekarNumbers(p, q):
    result  = [str(i) for i in range(p, q+1) if isKaprekar(i)]
    print(' '.join(result) if result else 'INVALID RANGE')

def isKaprekar(n : int):
    p = len(str(n))
    beta = (n ** 2) % (10 ** p)
    alpha = ((n ** 2) - beta) / 10 ** p
    return alpha + beta == n

p = 1
q = 100
print(kaprekarNumbers(p, q))


