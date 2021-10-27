# <boj 15953> 상금 헌터 (implementation)
import time
start_t = time.time()

t = int(input())
mylist = []
prize = []
for i in range(t):
  mylist.append(list(map(int, input().split())))

for i in range(t):  
  a = mylist[i][0]
  b = mylist[i][1]
  pa, pb, sum = 0, 0, 0
  if a == 0:
    sum = 0
  elif a == 1:
    pa = 5000000
    sum = pa
  elif 1 < a < 4:
    pa = 3000000
    sum = pa
  elif 4 <= a < 7:
    pa = 2000000
    sum = pa
  elif 7 <= a < 11:
    pa = 500000
    sum = pa
  elif 11 <= a < 16:
    pa = 300000
    sum = pa
  elif 16 <= a < 22:
    pa = 100000
    sum = pa

  if b == 0:
    sum += 0
  elif b == 1:
    pb = 5120000
    sum += pb
  elif 1 < b < 4:
    pb = 2560000
    sum += pb
  elif 4 <= b < 8:
    pb = 1280000
    sum += pb
  elif 8 <= b < 16:
    pb = 640000
    sum += pb
  elif 16 <= b < 32:
    pb = 320000
    sum += pb 
  prize.append(sum)

for i in range(t):
  print(prize[i])

end_t = time.time()
print("time : ", end_t - start_t)

'''

'''