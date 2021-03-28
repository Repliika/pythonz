#forLoops

'''
Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''
usernum = int(input("provide a number to print all smaller numbers "))

mylist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []
for nums in mylist:
    if nums < 5: #if num is less than 5 add it to new list
        newlist.append(nums)
        if nums < usernum: #if num in list is smaller than user input then print number from original list
            print(nums)

print(newlist) #prints new list of less than 5