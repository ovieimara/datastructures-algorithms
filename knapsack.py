


def maxKnapsack(items, max_weight):
    table = [[0 for _ in range(0, max_weight+1)] for _ in range(0, len(items))]
    picks = [['' for _ in range(0, max_weight + 1)] for _ in range(0, len(items))]

    max_value = 0
    max_idx = 0
    for i in range(0, max_weight+1):
        if items[0][1] <= i:
            table[0][i] = items[0][2]
            picks[0][i] = items[0][0]

    for i in range(1, len(items)):
        for j in range(0, max_weight+1):
            if items[i][1] > j:
                table[i][j] = table[i - 1][j]
                picks[i][j] = picks[i - 1][j]
            else:
                diff_in_weight = table[i - 1][j - items[i][1]]
                current = items[i][2]
                prev = table[i - 1][j]
                table[i][j] = max(prev, current + diff_in_weight)
                picks[i][j] = f"{items[i][0]} , {picks[i - 1][j - items[i][1]]}" if (current + diff_in_weight) > prev else picks[i - 1][j]

                # max_value = max(max_value, table[i][j])
                if max_value < table[i][j]:
                    max_value = table[i][j]
                    max_idx = (i, j)


    print(table)
    i, j = max_idx
    print(max_value, picks[i][j])
    return max_value



max_weight = 6
items = [['water', 3, 10], ['Book', 1, 3], ['Food', 2, 9], ['Jacket', 2, 5], ["Camera", 1, 6]]
val = maxKnapsack(items, max_weight)


def Items(prev, current):
    val = prev[1] + current[1]

