print("Enter number of row that you want to design")
a = int(input())

print("press 1 for top to bottom design" , "Press 0 for top to bottom design")
b = int(input())
tf = bool(b)

if tf == True:
    for i in range(1, a+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

if tf == False:
    for i in range(a,0,-1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
