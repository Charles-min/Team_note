# <문제6> 왕실의 나이트 (구현)
import time
start_t = time.time()

l = list(input())
count = 0

col = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
a = col[l[0]]
b = int(l[1])-1
x, y = a, b
dx = [1, -1, 2, -2]
dy = [1, -1, 2, -2]

for i in range(4):
  x += dx[i]
  if dx[i] == 1 or dx[i] == -1:
    for j in range(2):
      y += dy[j+2]
      if 0 <= x <= 7 and 0 <= y <= 7:
        count += 1
        x, y = a,b
      else:
        x, y = a,b
  else:
    for j in range(2):
      y += dy[j]
      if 0 <= x <= 7 and 0 <= y <= 7:
        count += 1
        x, y = a,b
      else:
        x, y = a,b
        
print(count)

end_t = time.time()
print("time : ", end_t - start_t)

'''
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
'''