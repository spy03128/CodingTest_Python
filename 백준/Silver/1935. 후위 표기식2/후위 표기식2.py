import sys
input = sys.stdin.readline

N = int(input())
cal_list = input().strip()
cal_dict = dict()
li = list()

for i in range(N) :
  cal_dict[chr(ord('A') + i)] = int(input())

for c in cal_list :
  if c in ['+', '-', '/', '*'] :
    b = li.pop()
    a = li.pop()
    if c == '+' :
      a += b
    elif c == '-' :
      a -= b
    elif c == '/' :
      a /= b
    else :
      a *= b
    li.append(a)
  else :
    li.append(cal_dict[c])

print('{:.02f}'.format(li[0]))