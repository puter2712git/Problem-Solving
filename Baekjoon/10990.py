import sys
input = sys.stdin.readline

star_line = int(input().rstrip())

for i in range(star_line):
  for j in range(star_line - i - 1):
    print(' ', end='')
  
  print('*', end='')
  
  for j in range(i * 2 - 1):
    print(' ', end='')
    
  if not i == 0:
    print('*', end='')
    
  print()