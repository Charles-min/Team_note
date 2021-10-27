# <boj 10162> 전자레인지 (그리디)
import time
start_t = time.time()

t = int(input())
f = -1
a, b, c = 0, 0, 0

if t % 10 != 0:
  print(f)
else:
  while t != 0:
    if t >= 300:
      a = t // 300
      t = t % 300
    elif 60 <= t < 300:
      b = t // 60
      t = t % 60
    else:
      c = t // 10
      t = t % 10
  print(a, b, c)

end_t = time.time()
print("time : ", end_t - start_t)

'''

'''
