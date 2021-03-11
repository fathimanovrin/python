n=[1,2,3,4,5,6,7,8,9]
l=[]
for i in range(0,len(n)):
    if n[i]%2!=0:
        l.append(n[i])
print(l)
