from typing import List


def matchedParentheses(n):
    subs = []
    # generate(n*2, 0, [], subs)
    generate(n, n, [], subs)
    return subs

def generate(open: int, close: int, sub: List, subs: List):
    print(sub, open, close)
    if open <= 0 and close <= 0:
        # if close < 0:
        subs.append(''.join(sub))
        return

    if open > 0:
        sub.append('(')
        generate(open - 1, close, sub, subs)
        sub.pop()


    if close > open:
        sub.append(')')
        generate(open, close - 1, sub, subs)
        sub.pop()



# def generate(n: int, total: int, sub: List, subs: List) -> None:
#
#     if n == 0 or total < 0 or total > n:
#         if total == 0:
#             subs.append(''.join(sub))
#         return
#
#     sub.append('(')
#     generate(n - 1, total + 1, sub, subs)
#     sub.pop()
#     sub.append(')')
#     generate(n - 1, total - 1, sub, subs)
#     sub.pop()


res = matchedParentheses(3)
print(res)