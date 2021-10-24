# <문제7> 문자열 재정렬 (구현)
import time
start_t = time.time()

s = list(input())
s.sort()
sum = 0
result = []
for i in s:
  if ord(i) <= 57:
    sum += int(i)
  else:
    result.append(i)
result.append(str(sum))
print(''.join(result))

end_t = time.time()
print("time : ", end_t - start_t)

'''

'''