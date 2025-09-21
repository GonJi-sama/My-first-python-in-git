nums = [8, 6, 4, 2, 3, 5, 7, 0, 1] # Example input

n = len(nums) # Since one number is missing, the length of nums is n
res = n * (n + 1) // 2 # Sum of numbers from 0 to n
print(res - sum(nums)) # The missing number is the difference between the expected sum and the actual sum