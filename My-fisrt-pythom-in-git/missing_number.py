nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

n = len(nums)
res = n * (n + 1) // 2
print(res - sum(nums))