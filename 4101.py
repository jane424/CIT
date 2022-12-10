while True:
  A, B = input().split()
  
  A = int(A)
  B = int(B)

  if A == 0 and B == 0:
    break  
  if A == B:
    print('No')
  if A > B:
    print('Yes')
  if B > A:
    print('No')
