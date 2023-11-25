#complexity: Time: O(nlogn), space = O(n)
def permutationEquation(p):
    # Write your code here
    p_dict = get_dict(p)
    return [p_dict.get(v) for k, v in p_dict.items()]


def get_dict(p: list) -> dict:
    return dict(sorted({p[i]: i + 1 for i in range(len(p))}.items()))