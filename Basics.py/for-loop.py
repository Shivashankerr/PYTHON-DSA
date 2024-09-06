#without range
li=[1,2,3,4,3,1,1]
ans=0
for i in li:
  if i==1: 
     ans=ans+1
print(ans)


#with range
li=[1,2,3,4,5,6]
ans=0
for i in range(5):
  if li[i]==1:
    ans=ans+1
print(ans)

#finding length
li=[1,23,45,6,7,8,3,4]
n=len(li)
print(n)

#problem
li=[6,8,9,5,4,6,5,2,6]
n=len(li)
ans=0
for i in range(n):
  if li[i]==6:
    ans=ans+1
print(ans)