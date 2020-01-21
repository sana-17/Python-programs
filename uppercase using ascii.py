str1= input ("Enter the string=")
for i in range (0,len(str1)):
    x=ord(str1[i])
    if x>=97 and x<=122:
      x=x-32
      y= chr (x)
      print (y, end="")
    else:
      x=x+32
      y= chr (x)
      print (y, end="")

