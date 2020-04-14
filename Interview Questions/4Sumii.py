from collections import defaultdict

def fourSum(A, B, C, D):
    """
    Return the number of tuple that sums to 0 taking one from each
    Store the sum of possible combinations in a Dict and check for negative sum in C and D
    """
    sum_dict = defaultdict(int)
    ans = 0
    for a in A:
        for b in B:
            sum_dict[-a-b]+=1

    for c  in C:
        for d in D:
            ans += sum_dict[c+d]


    return ans

print(fourSum([ 1, 2], [-2,-1], [-1, 2], [ 0, 2]))