#string
s="abcd"
print(s[2])

#string length
s="abcdef"
print(len(s))

#list length
li=[1,2,3,4,56]
print(len(li))

#to store that length
s="abcdef"
li=[1,2,3,4,56]
n=len(li)
print(n)

#reverse
s="abcd"
print(s[3]+s[2]+s[1]+s[0])

#using for loop
s="ABCD"
print(s[3]+s[2]+s[1]+s[0])
print(list(range(3,0,-1)))

#including zero should be print
s="ABCD"
print(s[3]+s[2]+s[1]+s[0])
print(list(range(3,-1,-1)))


#problem
s='ABCD'
ans=""
for i in range(3,-1,-1):
  ans=ans+s[i]
print(ans)  

#list reverse
li=[5,8,9,1]
for i in range(3,-1,-1):
  print(li[i])


#reverse string
s="abcdefghik"
n=len(s)
for i in range(n-1,-1,-1):
  print(s[i])


#reverse list
li=[10,20,30,40,50,60]
n=len(li)
for i in range(n-1,-1,-1):
  print(li[i])


#reverse string
s="abcdefghik"
n=len(s)
ans=""
for i in range(n-1,-1,-1):
   ans =ans+s[i]
print(ans)