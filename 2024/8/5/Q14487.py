n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
res = sum(lst[1:])
print(res)