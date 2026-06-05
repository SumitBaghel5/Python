num_1 = int(input("enter 1st no ="))
num_2 = int(input("enter 2nd no ="))
num_3 = int(input("enter 3rd no ="))

# Logic: Check if num_1 is biggest, else check if num_2 is biggest, else it's num_3
result = (num_1 >= num_2 and num_1 >= num_3) and num_1 or \
(num_2 >= num_3) and num_2 or num_3

print("Largest is:", result)