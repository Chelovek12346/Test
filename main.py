from collections import defaultdict
import heapq


n, m = map(int, input().split())

e = [list(map(int, input().split())) for _ in range(m)]
di = [30000]*(n+1)
di[1] = 0
for _ in range(n-1):
    for i in e:
        if di[i[0]] != 30000:
            di[i[1]] = min(di[i[1]], di[i[0]] + i[2])

print(*di[1:])




n,s,f = map(int,input().strip().split())

n = int(input())
l = [list(map(int,input().strip().split())) for _ in range(n)]
l = [[l[i][j] if l[i][j] != -1 else 1000000000000 for j in range(n)] for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            l[i][j] = min(l[i][j], l[i][k]+l[k][j])

m = 0
for i in range(n):
    for j in range(n):
        if l[i][j] != 1000000000000:
            m = max(m, l[i][j])
print(m)
# [print(*i) for i in l]



# d = defaultdict(set)
# w = set()
# h = [(0,s)]
# di = [1000000000000]*(n+1)
# di[s] = 0
#
# for i in range(n):
#     l = list(map(int,input().strip().split()))
#     for j in range(n):
#         if i != j and l[j] != -1:
#             d[i+1].add((j+1,l[j]))
#
# # print(d)
# while h:
#     # print(h)
#     r,v = heapq.heappop(h)
#     # print(r,v)
#     if v in w:
#         continue
#     w.add(v)
#     for i in d[v]:
#         if di[v]+i[1] < di[i[0]]:
#             di[i[0]] = di[v]+i[1]
#             heapq.heappush(h,(di[i[0]],i[0]))
#
# print(di[f] if di[f] != 1000000000000 else -1)