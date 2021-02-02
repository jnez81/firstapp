def solution(A, B):
    counter = 0
    s1 = sorted(A)
    s2 = sorted(B)
    if s1 != s2:
        for (i, j) in zip(s1, s2):
            if i != j: 
                counter += 1
    else: 
        return 0


print(solution("apple", "pear"))