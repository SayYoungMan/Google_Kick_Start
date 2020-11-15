def isKick(idx):
    if S[idx:idx+4] == "KICK":
        return True
    else:
        return False

def isStart(idx):
    if S[idx:idx+5] == "START":
        return True
    else:
        return False

# Number of test cases
T = int(input())
# Loop over the test cases
for case in range(T):
    S = input()
    valid_kicks = 0
    counts = 0
    i = 0
    while i < len(S):
        if isKick(i):
            valid_kicks += 1
            i += 3
        elif isStart(i):
            counts += valid_kicks
            i += 5
        else:
            i += 1

    # Print the answer
    print("Case #{}: {}".format(case + 1, counts))