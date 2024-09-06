#Modulus
print(5%3)
print(6%3)
print(35%5)

#problem
li=[3,6,8,7,9]
for i in li:
  print(i)
  

#with condition
li=[3,6,8,7,9,15,12]
ans=0
for i in li:
  if i%5==0:
    ans=ans+1
  print(ans)