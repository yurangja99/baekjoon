import sys
from itertools import product

input = lambda: sys.stdin.readline().strip()
print = lambda x: sys.stdout.write(str(x) + "\n")

N, M, K = map(int, input().split())

# board: N * M
board = [list(input()) for _ in range(N)]


# num_errors: N * M * 2
# stores how many squares to be re-colored
# num_errors[n][m][0]: left-upper square is white
# num_errors[n][m][1]: left-upper square is black
num_errors = [[[0, 0] for _ in range(M + 1)] for _ in range(N + 1)]


# f(n, m, c) = f(n - 1, m, c) + f(n, m - 1, c) - f(n - 1, m - 1, c) + g(n, m)
# f(n, m, c) = num_errors[n][m][c]
# g(n, m) = (1 if the square should be re-colored, 0 otherwise)
min_errors = 2000 * 2000
for n, m, c in product(range(1, N + 1), range(1, M + 1), range(2)):
  num_errors[n][m][c] = num_errors[n - 1][m][c]
  num_errors[n][m][c] += num_errors[n][m - 1][c]
  num_errors[n][m][c] -= num_errors[n - 1][m - 1][c]
  if board[n - 1][m - 1] == "BW"[(n + m + c) % 2]:
    num_errors[n][m][c] += 1
  
  if n >= K and m >= K:
    errors = num_errors[n][m][c]
    errors -= num_errors[n - K][m][c]
    errors -= num_errors[n][m - K][c]
    errors += num_errors[n - K][m - K][c]
    if errors < min_errors:
      min_errors = errors

print(min_errors)