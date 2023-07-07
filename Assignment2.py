#  Arithmetic operators
a=25
b=10
print("Addition is: ",a+b)
print("Subtraction is: ",a-b)
print("Multiplication is: ",a*b)
print("Division is: ",a/b)
print("Mod is: ",a%b)
print("Floor Division is: ",a//b)
print("Exponentation is: ",a**b)

# Assignment operators
a=50 ; a+=5
print("+=",a)
a=50  ; a-=5
print("-=",a)
a=50 ;a*=5
print("*=",a)
a=50 ;a/=5
print("/=",a)
a=50 ; a//=5
print("//=",a)
a=50 ; a%=5
print("%=",a)
a=50 ; a**=5
print("**=",a)

# Comparision operators
a=25 ; b=10
print("25>=10",a>=b)
print("25<=10",a<=b)
print("25==10",a==b)
print("25!=10",a!=b)
print("25<10",a<b)
print("25>10",a>b)

# Logical operators
a=True ; b=False
print("AND is:",a and b)
print("OR is:",a or b)
print("NOT is:",not b)


#  Bitwise operators
a=10 ;b=5
print("Bitwise & is:",a&b)
print("Bitwise | is:",a|b)
print("Bitwise ^ is:",a^b)
print("Bitwise >> is:",a>>2)
print("Bitwise << is:",a<<2)

# Identity operators
a=10 ; b=10.0
print("Is:",a is b)
print("Is not:",a is not b)

# Membership operators
a="Shrikant"
print("In","K" in a)
print("Not in","j" not in a)