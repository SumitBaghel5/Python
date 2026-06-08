# age <= 13 == child
# age 13 -18 == teenager
# age >18 == adult

# age = int(input("Enter your age = "))
# if age < 13:
#     print("You are Child ")
# elif (13 < age < 18 ):
#     print("You are teenager ")
# else:
#     print("You are adult")

#  username = "admin" and password = "pass"
# user_name = input("Enter your username = ").lower()
# password = input("Enter your password = ").lower()
# if (user_name == "admin" and password == "pass"):
#     print("Login Successful")
# elif (user_name != "admin"):
#     print("wrong username")
# elif (password != "pass"):
# #     print("wrong Password")
# while True:
# #     # print("Helow World")

# # count = 1
# # while (count <= 5):
# #     print("Hi mona")
# #     count += 1

# i = 5 
# while(i>=0):
#     print(i)
#     i-=1

# num = int(input('Write your no'))
# count = 1
# while(count<=10):
#     print(num,"X",count,"=",num*count)
#     count += 1

i = 1
while(i<=10):
    if (i%2 == 0):
        i += 1
        continue
        
    print(i)
    i += 1