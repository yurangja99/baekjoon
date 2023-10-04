import sys

input = lambda: sys.stdin.readline().strip()
print = lambda x: sys.stdout.write(str(x) + " ")

N = int(input())
A = list(map(int, input().split()))

NGF = [-1 for _ in A]
count = dict()

for a in A:
  if a not in count:
    count[a] = 1
  else:
    count[a] += 1

# store (idx, num)
stack = []
for idx, a in enumerate(A):
  while stack and stack[-1][1] != a and count[stack[-1][1]] < count[a]:
    i, _ = stack.pop()
    NGF[i] = a
  stack.append((idx, a))

for ngf in NGF:
  print(ngf)