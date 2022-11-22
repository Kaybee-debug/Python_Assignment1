#Print character index
print("our string is 'Live Happily")

i = "Live Happily"
n = int( input("Enter the position in the string:  "))
x = len(i)

if n > x:
    print(n,"is out of the range")
elif i[n]  == "":
    print("Empty string")  
else:
    print(i[n])    







        









