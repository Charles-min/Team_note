# <문제> 1이 될 때까지 (그리디)
import time
start_t = time.time()

n, k = map(int, input().split())
count = 0

while n != 1:
  if n%k == 0:
    n = n // k
    count += 1
  else:
    n -= 1
    count += 1

print(count)
end_t = time.time()
print("time : ", end_t - start_t)


'''
풀이 
n, k = map(int, input().split())
result = 0

whlie True:
  target = (n // k) * k
  result += (n - target)
  n = target
  if n < k:
    break
  result += 1
  n //= k

result += (n - 1)
print(result)
'''