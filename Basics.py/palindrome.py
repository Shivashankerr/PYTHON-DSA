#palindrome
#aba==>aba it ia palindrome
#abc==>cba it is not a palindrome
#when two strings are reversed it should be same content

#example1
s="abba"
if s=="abba":
  print("yes it is palindrome")
else:
  print("it is not a palindrome")


#example2
s="abccba"
rev=""
for i in range(len(s)-1,-1,-1):
     rev=rev+s[i]
if rev==s:
   print("yes")
else:
   print("no")