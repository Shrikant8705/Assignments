print("__________")
print("   Break  ")
print("___________")
for i in range(0, 10):
    if i == 5:
        break
    else:
        print(i)
print("_______")
print("Continue")
print("_______")
for i in range(0, 10):
    if i == 5:
        continue
    else:
        print(i)
print("______")
print("Pass")
print("______")
for i in range(0, 10):
    if i == 5:
        pass
    else:
        print(i)
print("______")
print("forWithElse")
print("______")
for i in range(0, 10):
    print(i)
else:
        print("Hello,I'm for with else")

print("_____________")
print("whileWithElse")
print("_____________")
i=0
while i<10:
    print(i)
    i+=1
else:
        print("Hi,I'm while with else")
