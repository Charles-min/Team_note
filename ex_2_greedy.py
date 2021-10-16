# <문제2> 곱하기 더하기 (그리디)
import time
start_t = time.time()

s = input()
s = list(map(int, s))
len = len(s)

result = 0

for num in range(0,len):
  if result < 2:
    result += s[num]
  else:
    result *= s[num]
  
print(result)
end_t = time.time()
print("time : ", end_t - start_t)

