
import bisect
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def binary_search_solution(arr,length,sum):
    new = list(arr)
    new.sort()
    for i in range(length-1):
        target = sum - arr[i]
        #check if target exists in sorted arra using binaary search, then make sure its two diff elements
        if index(new,target) != -1:
            if arr.index(target) != i:
                return [i+1,arr.index(target)+1]


num_cases = int(raw_input())
for _ in range(num_cases):
    sum = int(raw_input())
    length = int(raw_input())
    arr = [int(i) for i in raw_input().split(" ")]
    a,b = binary_search_solution(arr,length,sum)
    print "%i %i" %((a,b) if a<b else(b,a))
