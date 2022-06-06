import array as arr

def player1():
 x = input("Please enter the x :\n")
 x=int(x)
 y = input("Please enter the y :\n")
 y=int(y)
 f=1
 return x,y,f 

def player2():
 x = int(input("Please enter the x :\n"))
 y = int(input("Please enter the y :\n"))
 f=2
 return x,y,f


i=0
r=1
q=2
First_Row=arr.array('i', [8, 9, 5])
Sec_Row=arr.array('i', [4, 2, 3])
Ther_Row=arr.array('i', [6, 7, 3])
for i in range (0, 3):
    print (First_Row[i], end =" ")
print('\t')
for i in range (0, 3):
    print (Sec_Row[i], end =" ")
print('\t')
for i in range (0, 3):
    print (Ther_Row[i], end =" ")

print()
while (First_Row[i] != First_Row[r] and First_Row[r] != First_Row[q] or Sec_Row[i] != Sec_Row[r] and Sec_Row[r] != Sec_Row[q] or Ther_Row[i] != Ther_Row[r] and Ther_Row[r] != Ther_Row[q] or First_Row[i]!=Sec_Row[i] and Sec_Row[i]!=Ther_Row[i]):
 x,y,f=player1()
 if f == 1:
  if x==0 :
    First_Row[y]=0
  elif x==1:
    Sec_Row[y]==0
  elif x==2 :
    Ther_Row[y]==0

 elif f == 2:
   if x==0 :
    First_Row[y]=1
   elif x==1:
    Sec_Row[y]==1
   elif x==2 :
    Ther_Row[y]==1

 x,y,f=player2()
 if f == 1:
  if x==0 :
    First_Row[y]=0
  elif x==1:
    Sec_Row[y]==0
  elif x==2 :
    Ther_Row[y]==0

 elif f == 2:
   if x==0 :
    First_Row[y]=1
   elif x==1:
    Sec_Row[y]==1
   elif x==2 :
    Ther_Row[y]==1

 for i in range (0, 3):
    print (First_Row[i], end =" ")
 print('\t')
 for i in range (0, 3):
    print (Sec_Row[i], end =" ")
 print('\t')
 for i in range (0, 3):
    print (Ther_Row[i], end =" ")
 print('\t')
 for i in range (0, 3):
    print (First_Row[i], end =" ")
 print('\n')
 for i in range (0, 3):
    print (Sec_Row[i], end =" ")
 print('\n')
 for i in range (0, 3):
    print (Ther_Row[i], end =" ")
