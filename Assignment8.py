class A:
    a = None
    _b = None
    __c = None
    def __init__(self,a,b,c):
        self.a = a
        self._b = b
        self.__c = c

    def display(self):
        print("Class A")
        print(f"a : {self.a}, b = {self._b}, c = {self.__c}")
    
class B (A):
    def display(self):
        print("Class B")
        print(f"a = {self.a}, b = {self._b}",end = " ")
        try:
            print(f"c = {self.__c}")
        except Exception:
            print("\nException at line 29 of Assignment8.py, \'__c\' cannot be accesed because it is a private variable of class A")
    
b = B("Shrikant","Shedge","COB3")
b.display()