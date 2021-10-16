# <문제3> 모험가 길드 (그리디)
import time
start_t = time.time()

n = int(input())
data = list(map(int, (input().split())))
data.sort()

group = 0
count = 0

for i in data:
  count += 1
  if count >= i:
    group += 1
    count = 0
   
print(group)

end_t = time.time()
print("time : ", end_t - start_t)