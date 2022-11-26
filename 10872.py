N = int(input())
a = 1

for i in range(1,N):
    a=i*a
  
if N == 0:
  print(1)
else:
  print(a*N)
