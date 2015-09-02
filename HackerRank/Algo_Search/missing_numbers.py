
def caching_sol(arr1,arr2):
    baseline = arr2[0]-101 # range from baseline to baseline + 200
    bucket = [0 for i in range(200)]
    for i in arr2:
        bucket[i-baseline] += 1
    for j in arr1:
        bucket[j-baseline] -= 1
    #look for diff between bucket1 and bucket2
    return [x+baseline for x in range(len(bucket)) if bucket[x] != 0]

#main
len1 = int(raw_input())
arr1 = [int(i) for i in raw_input().split(" ")]
len2 = int(raw_input())
arr2 = [int(i) for i in raw_input().split(" ")]

print " ".join([str(i) for i in caching_sol(arr1,arr2)])


