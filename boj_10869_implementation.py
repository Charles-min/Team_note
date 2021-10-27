# <boj 10869> 사칙연산 (implementation)
import time
start_t = time.time()

a, b = map(int, input().split())
print(a+b, a-b, a*b, a//b, a%b, sep='\n')

end_t = time.time()
print("time : ", end_t - start_t)
