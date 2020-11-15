import numpy as np

T = int(input())
for x in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    mat = np.array(mat)
    diags = [mat.diagonal(i) for i in range(N-1, -N, -1)]
    maxCoin = max([sum(n.tolist()) for n in diags])
    print("Case #{}: {}".format(x+1, maxCoin))