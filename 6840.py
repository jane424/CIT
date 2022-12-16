A = int(input())
B = int(input())
C = int(input())

if C > A > B:
  print(A)

if B > A > C:
  print(A)
  
if A > B > C:
  print(B)

if C > B > A:
  print(B)

if A > C > B:
  print(C)

if B > C > A:
  print(C)
