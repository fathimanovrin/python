cy=int(input("enter the current year"))
fy=int(input("enter the final year"))
ls=[]
for i in range(cy,fy+1):
    if(i%4==0 and i%100!=0) or i%400==0:
        ls.append(i)
print(ls)
