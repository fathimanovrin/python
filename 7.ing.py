s=input("enter a word")
if s[-3:]=='ing':
    s+="ly"
else:
    s+="ing"
print(s)
