# Retrieve number of test cases
T = int(input())
# Loop over the cases
for case in range(T):
    N, B = list(map(int, input().split()))
    A = list(map(int, input().split()))
    count_array = [0] * 1001
    for price in A:
        count_array[price] += 1
    total = 0
    count = 0
    i = 1
    while total <= B and i < 1001:
        while count_array[i] != 0:
            total += i
            if total > B:
                break
            count += 1
            count_array[i] -= 1
        i += 1
    print('Case #{}: {}'.format(case+1, count))
    
    