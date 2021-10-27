# <boj 12100> 2048 easy (implementation)
import time
start_t = time.time()

n = int(input())
list = []
for i in range(n):
  list.append(list(map(int, input().split()))

max = 0

for i in range(n):
  for j in range(n):
    if max < list[i][j]:
      max = list[i][j]



end_t = time.time()
print("time : ", end_t - start_t)

'''

'''