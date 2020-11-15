# Number of test cases
T = int(input())
# Loop over the test cases
for case in range(T):
    N, K, P = list(map(int, input().split()))
    stacks = []
    for _ in range(N):
        stacks.append(list(map(int, input().split())))
    for stack in stacks:
        for i in range(1, K):
            stack[i] += stack[i-1]
    dp = [[0]* (P)] * (N)
    for j in range(min(K,P)):
        dp[0][j] = stacks[0][j]
    for i in range(1, N):
        for j in range(P):
            

    # Print the answer
    print("Case #{}: {}".format(case, "result"))