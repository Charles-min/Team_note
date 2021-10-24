# <문제5> 시각 (구현)
import time
start_t = time.time()

n = int(input())
time_h = [3, 13, 23]
time_s = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]
time_m = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]

result = 0

for h in range(0, n+1):
  if h in time_h:
    result += 3600
  else:
    for m in range(0, 60):
      if m in time_m:
        result += 60
      else:
        result += len(time_s)

print(result)

end_t = time.time()
print("time : ", end_t - start_t)

'''
h = int(input())
count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1
print(count)
'''