from collections import Counter

def matchingStrings(stringList, queries):
    # Write your code here
    counter = Counter(stringList)
    return [counter.get(q, 0) for q in queries]


