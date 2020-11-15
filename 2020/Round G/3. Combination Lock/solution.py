# Solution for Case 1 and Case 2 => O(W^2)

# # Number of test cases
# T = int(input())
# # Loop over the test cases
# for case in range(T):
#     W, N = list(map(int, input().split()))
#     wheels = list(map(int, input().split()))
#     minimum_moves = float('inf')
#     for target in wheels:
#         count = 0
#         for wheel in wheels:
#             if wheel >= target:
#                 count += min(N-wheel+target, wheel-target)
#             else:
#                 count += min(N+wheel-target, target-wheel)
#         minimum_moves = min(minimum_moves, count)

#     # Print the answer
#     print("Case #{}: {}".format(case + 1, minimum_moves))

# Solution for Case 3

# Number of test cases
T = int(input())
# Loop over the test cases
for case in range(T):
    W, N = list(map(int, input().split()))
    wheels = list(map(int, input().split()))
    minimum_moves = float('inf')
    for target in wheels:
        count = 0
        for wheel in wheels:
            if wheel >= target:
                count += min(N-wheel+target, wheel-target)
            else:
                count += min(N+wheel-target, target-wheel)
        minimum_moves = min(minimum_moves, count)

    # Print the answer
    print("Case #{}: {}".format(case + 1, minimum_moves))