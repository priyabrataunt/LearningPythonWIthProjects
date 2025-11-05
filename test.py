nums = [3,4,5,6]
target = 7

indices = {}

for i, n in enumerate(nums):
    indices[n] = i

# for i, n in enumerate(nums):
#     diff = target - n
#     if diff in indices and indices[diff] != i:
#         return [i, indices[diff]]