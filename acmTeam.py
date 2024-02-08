
def acmTeam(topic):
    teams = [topicsKnown(topic[i], topic[j]) for i in range(len(topic)) for j in range(i + 1, len(topic))]

    result = [str(team).count('1') for team in teams]

    max_topic = max(result)

    max_team = [r for r in result if r == max_topic]

    return [max_topic, len(max_team)]


def topicsKnown(x, y):
    return bin(int(x, 2) | int(y, 2))


# def topicsKnown(x, y):
#     subjects = []
#     # print(x, y)
#     for i in range(len(x)):
#         if any([int(x[i]), int(y[i])]):
#             subjects.append(i+1)
#
#     return subjects



topic = ['10101', '11110', '00010']
topic = [ '10101', '11100', '11010','00101']
res = acmTeam(topic)
print(res)