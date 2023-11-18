from collections import OrderedDict
def leaderBoard(ranked, player):
    results = []
    ranked = list(OrderedDict.fromkeys(ranked))
    for i in range(len(player)):
        play = player[i]
        while ranked and play >= ranked[-1]:
            ranked.pop()

        ranked.append(play)
        results.append(len(ranked))

    return results


def climbingLeaderboard(ranked, player):
    # Write your code here
    return leaderBoard(ranked, player)

# def climbingLeaderboard(ranked, player):
#     # Write your code here
#
#     ranks = sorted(ranked, reverse=True)
#     print(ranks)
#     # player.sort()
#
#     ranks_dict = getRanks(ranks)
#     n = len(ranked)
#     m = len(player)
#     i = 0
#     j = m - 1
#
#     results = [0] * m
#     while i < n and j >= 0:
#         rank = ranked[i]
#         play = player[j]
#
#         if play >= rank:
#             r = ranks_dict.get(rank)
#             results[j] = r
#             j -= 1
#
#         elif play < rank:
#             i += 1
#     # print(results, j)
#     for i in range(m - 1, -1, -1):
#         start = -1
#         val = 0
#         if results[i] == 0:
#             if start == -1:
#                 val = ranks_dict.get(ranked[-1])
#                 start = i
#             else:
#                 val = results[i + 1]
#
#             results[i] = val + 1
#
#     return results
#
#
# def getRanks(ranked):
#     ranks = {}
#     ranked.sort(reverse=True)
#     prev_rank = float("inf")
#
#     i = 0
#     while i < len(ranked):
#         num = ranked[i]
#         if num < prev_rank:
#             if len(ranks) <= 0:
#                 ranks[num] = 1
#             elif num < prev_rank:
#                 val = ranks.get(prev_rank, 0)
#                 ranks[num] = val + 1
#
#         prev_rank = num
#         i += 1
#
#     return ranks