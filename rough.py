# name = input("Enter your Name = ")
# age = int(input("Enter your Age = "))
# show_time = input("tpye Morning, Mid_Day, Evening = ")
# ticket_price = int(input("Ticket price"))
# student = input("Type Y or N =")
# discount_age = (age < 18) and (ticket_price-(20/100*ticket_price)) or (50 >= age >= 18) and (ticket_price-(10/100*ticket_price)) or (age >50) and (ticket_price-(30/100*ticket_price))
# discount_show_time = (show_time == "morning") and (ticket_price-(30/100*ticket_price)) or (show_time == "MidDay") and (ticket_price-(20/100*ticket_price)) or (show_time == "Evening") and (ticket_price-(10/100*ticket_price))
# discount_student = (student == "Y") and (ticket_price-(20/100*ticket_price)) or (student == "N" ) and (ticket_price-(10/100*ticket_price))

# final_price = ("Final Price of your movie ticket = " , ticket_price - (discount_age + discount_show_time + discount_student))
# print(name ,age , show_time , ticket_price , student , final_price, sep="\n")



# 1. Inputs and Data Types
name = input("Enter your Name = ")
age = int(input("Enter your Age = "))
show_time = input("Type Morning, Mid_Day, Evening = ")
ticket_price = int(input("Ticket price = "))
student = input("Type Y or N = ")

# 2. Age group math logic bina if-else ke
# (age < 18) True hoga to 1 banega, False hoga to 0 banega.
is_child = int(age < 18)
is_adult = int(18 <= age <= 50)
is_senior = int(age > 50)

# Alag-alag conditions ke discounts (Rupees mein)
discount_age_amt = (is_child * 0.20 * ticket_price) + (is_adult * 0.10 * ticket_price) + (is_senior * 0.30 * ticket_price)

# 3. Show Time aur Student ke liye Look-up Dictionaries (Data Types)
# Agar user "Morning" likhega to dictionary use 0.30 (30%) return karegii.
show_discounts = {"Morning": 0.30, "Mid_Day": 0.20, "Evening": 0.10}
student_discounts = {"Y": 0.20, "N": 0.10}

# .get() ka use karke value nikalna. Agar user galat type karega to 0 discount milega.
discount_show_amt = show_discounts.get(show_time, 0.0) * ticket_price
discount_student_amt = student_discounts.get(student, 0.0) * ticket_price

# 4. Total calculation (Sirf Operators ka use karke)
total_discount_saved = discount_age_amt + discount_show_amt + discount_student_amt
calculated_price = ticket_price - total_discount_saved

# 5. Output Formatting (Bina Tuple ke, taaki single line m print ho)
final_price = f"Final Price of your movie ticket = Rs. {calculated_price}"

# 6. Printing on different lines
print("\n--- RECEIPT ---")
print(name, age, show_time, ticket_price, student, final_price, sep="\n")