import sys

input = lambda: sys.stdin.readline().strip()
print = lambda x: sys.stdout.write(str(x) + "\n")

string = input()
key = list(input())
len_key = len(key)

stack = list(string)
stack.reverse()

result = []
while stack:
  result.append(stack.pop())
  while result[-len_key:] == key:
    del result[-len_key:]

print("".join(result) if result else "FRULA")