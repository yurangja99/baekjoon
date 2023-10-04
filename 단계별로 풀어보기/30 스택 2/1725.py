import sys

input = lambda: sys.stdin.readline().strip()
print = lambda x: sys.stdout.write(str(x) + "\n")

N = int(input())
heights = [int(input()) for _ in range(N)]

# (idx, height)
stack = []

max_area = 0

for n, height in enumerate(heights + [0]):
  i = n
  while stack and stack[-1][1] > height:
    i, h = stack.pop()
    area = (n - i) * h
    if area > max_area:
      max_area = area
  stack.append((i, height))

print(max_area)