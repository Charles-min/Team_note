# <boj 1789> 수들의 합 (그리디)
import time
start_t = time.time()

s = float(input())
s_copy = s
n = 1

while s_copy > 0:
  s_copy = s_copy - n
  n += 1

if n*(n-1)/2 <= s < n*(n+1)/2:
  print(n-1)
else:
  print(n-2)

end_t = time.time()
print("time : ", end_t - start_t)

'''

'''