
def simpleTextEditor(Q):
    S = []
    transactions = []

    for query in Q:
        q = query.split()
        op = q[0]
        string = q[1] if len(q) > 1 else '0'

        if op == '1':
            for char in string:
                S.append(char)
            transactions.append((op, string))

        elif op == '2':
            deletes = [S.pop() for _ in range(int(string))]
            transactions.append((op, ''.join(deletes[:: -1])))

        elif op == '3':
            print(S[int(string) - 1])

        elif op == '4':
            num, vals = transactions.pop() if transactions else (0, '')
            if num == '1':
                [S.pop() for _ in range(len(vals))]

            elif num == '2':
                for c in vals:
                    S.append(c)


Queries = ['1 abc', '3 3', '2 3', '1 xy', '3 2', '4', '4', '3 1']

simpleTextEditor(Queries)
