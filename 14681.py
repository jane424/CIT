X = int(input())
Y = int(input())
a = X > 0
b = X < 0
c = Y > 0
d = Y < 0
if a and c :
  print ("1")
if b and c :
  print ("2")
if b and d :
  print ("3")
if a and d :
  print ("4")
