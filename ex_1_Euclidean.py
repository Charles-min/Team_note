# 유클리드 호제법 재귀함수 구현
  
import time
start_t = time.time()

def gcd(a, b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)

print(gcd(192, 162))

end_t = time.time()
print("time : ", end_t - start_t)

'''

'''