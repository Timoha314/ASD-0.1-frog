count = int(input())
Array = list(map(int, input().split()))

if count == 1:
    print(Array[0])
    print(1)
elif count < 3:
    print(-1)
else:
    dp = [-float('inf')] * (count + 1)
    Numbers = [-1] * (count + 1)
    dp[1] = Array[0]
    if count > 2:
        dp[2] = -float('inf')
    for i in range(3, count + 1):
        if dp[i - 2] > dp[i - 3]:
            dp[i] = dp[i - 2] + Array[i - 1]
            Numbers[i] = i - 2
        else:
            dp[i] = dp[i - 3] + Array[i - 1]
            Numbers[i] = i - 3

    result = dp[count]

    def find_path(Numbers, i):
        path = []
        while i > 0:
            path.append(i)
            i = Numbers[i]
        if path[-1] != 1:
            path.append(1)
        path.reverse()
        return path


    path = find_path(Numbers, count)
    print(result)
    print(" ".join(map(str, path)))
