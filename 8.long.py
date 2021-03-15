n=int(input("enter the limit"))
ls=[]
long=0
print("enter list of word")
for i in range(n):
    a=input()
    ls.append(a)
    l=len(a)
    if(l>long):
        long=1
print(ls)
print("longest word",long)
