class A:
    __length=0
    __breadth=0
    __area=0
    def __init__(self,l,w):
        self.__length=l
        self.__breadth=w
    def area1(self):
        self.__area=self.__length*self.__breadth
    def __lt__(self,other):
        if(self.__area<other.__area):
            return True
        else:
            return False
ob1=A(2,6)
ob1.area1()
ob2=A(4,5)
ob2.area1()
if ob1<ob2:
    print("ob2 is greater")
else:
    print("ob1 is greater")
        
