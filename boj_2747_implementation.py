# <boj 2747> 피보나치 수 (implementation)
import time
start_t = time.time()

def fibo(n):
  list = [0, 1]
  for i in range(2, n+1):
    c = list[i-1] + list[i-2]
    list.append(c)
  return list[n]

n = int(input())
print(fibo(n))

end_t = time.time()
print("time : ", end_t - start_t)

'''

'''