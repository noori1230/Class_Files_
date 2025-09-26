index number is for only numbers
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
numbers[0] = 111
print("New list contents: ", numbers)  # Current list contents.
numbers[2] = 333
print("New list contents: ", numbers)  # Current list contents.
numbers[1] = 222
print("New list contents: ", numbers)  # Current list contents.
numbers[3] = 444
print("New list contents: ", numbers)  # Current list content
numbers[4] = 555
print("New list contents: ", numbers)  # Current list content
numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.
numbers[3] = numbers[0]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.
numbers[0] = numbers[3]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.
numbers = [10, 5, 7, 2, 1 ,2 , 23 , 45]
print("\nList length:", len(numbers))  # Printing the list's length.
numbers = [10, 5, 7, 2, 1]
del numbers[1]
print(len(numbers))
print(numbers)
numbers = [10, 5, 7, 2, 1]
del numbers[3]
print(len(numbers))
print(numbers)
#negative index list
numbers = [111, 7, 2, 1]
print(numbers[-1])
numbers = [111, 7, 2, 1]
print(numbers[-4])
numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-4])
