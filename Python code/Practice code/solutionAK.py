"""

"""

def solution(A, K):
    n = len(A)
    for i in range(n - 1):
        if (A[i] + 1 < A[i + 1]):
            return False
    if (A[0] != 1 and A[n - 1] > K):
        return False
    else:
        return True

print(solution([1,1,2,3,3,4,6], 6))