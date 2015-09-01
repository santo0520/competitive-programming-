def solve(arr,len):
    """given sequence of array, return yes/no"""
    left_sum = 0
    right_sum= sum(arr[1:])
    #remenber to test edge case
    if left_sum == right_sum:
        return "YES"
    else:
        for idx in range(1,len):
            left_sum += arr[idx-1]
            right_sum -= arr[idx]
            if left_sum == right_sum:
                return "YES"
        return "NO"

#main
num_cases = int(raw_input())
for _ in range(num_cases):
    len = int(raw_input())
    arr = [int(i) for i in raw_input().split(" ")]
    print solve(arr,len)
