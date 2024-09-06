#AND operator
#two sides condition should be true

if 1+2==3 and 2+5==7:
  print("Boooom")
else:
  print("chapri")


#condition false
if 1+2==3 and 2+5==10:
  print("Boooom")
else:
  print("chapri")


#OR operator
#one should be correct either left or right
if 1+2==3 or 2+5==9:
  print("Boooom")
else:
  print("chapri")

#problem 3 and 2 divided by same members in list find out

li=[12,3,4,2,18,6]
ans=0
for i in li:
  if i%3==0 and i%2==0:
    ans=ans+1
  print(ans)
  

#either 3 or 2 divided in the list
li=[12,3,4,2,18,6,5,9]
ans=0
for i in li:
  if i%3==0 or i%2==0:
    ans=ans+1
  print(ans)

