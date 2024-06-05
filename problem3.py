# input at least 6 elements and display the list

li=set()

print("How many number you want to add in list. More thand 6.")
n=int(input())
while(n<2):
    n=int(input("Enter  a number more than 6: "))


print(f"Enter more then {n} Numbers in set: ")
for i in range(n):
    num = int(input())
    li.add(num)

print(li)

# using exception handeling allowing user to remove an element
try:
    rmv  = int(input("Enter a number you want to remove from list"))
    if rmv not in li:
        print("The given number is not present in the list")
    li.remove(rmv)
    print(li)

except Exception as e:
    print(type(e))

# Prompting user to discard an element from the list without error handling

se=li
d = int(input("If you want to Discard an element press 1 or Press 2 for Nothing."))
if d==1:
     se.discard(dsc)
print(se)

# error handle and pop the element
try:
    fl = int (input("Enter 1 for pop from the set: "))
    if fl==1:
        se.pop()
    print(se)

except Exception as e:
    print(type(e))


    


