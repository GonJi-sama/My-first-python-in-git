def sol(num, target):
    num_map = {}

    for i, n in enumerate(num):
        diff = target - n
        if diff in num_map:
            return [num_map[diff], i]
        num_map[n] = i

n = [2, 7, 11, 15]
t = 9
print(sol(n, t))