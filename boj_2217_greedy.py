# <boj 2217> 로프 (그리디)
import time
start_t = time.time()

n = int(input())
k = []
for i in range(n):
  k.append(int(input()))

k.sort()
w = []

for i in range(0, n):
  w.append((n-i)*k[i])
w.sort()

print(w[n-1])

end_t = time.time()
print("time : ", end_t - start_t)

'''

'''