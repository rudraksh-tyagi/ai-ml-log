# if (condition):
#     # code to execute if condition is True
# else:
#     # code to execute if condition is False

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are not an adult.")


# def check_adult(age):
#     if age >= 18:
#         return "You are an adult."
#     else:
#         return "You are not an adult."
def max_number(a, b , c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c    

max_num = max_number(10, 20, 15)
print("The maximum number is:", max_num)