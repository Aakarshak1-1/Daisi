def add(num1, num2):
    num1,num2=int(num1),int(num2)
    return num1+num2


# def sub(num1, num2):
#     num1,num2=int(num1),int(num2)
#     return num1-num2


# def mul(num1, num2):
#     num1,num2=int(num1),int(num2)
#     return num1*num2


# def floordiv(num1, num2):
#     num1,num2=int(num1),int(num2)
#     return num1//num2


# def div(num1, num2):
#     num1,num2=int(num1),int(num2)
#     return num1/num2


# def modulo(num1, num2):
#     num1,num2=int(num1),int(num2)
#     return num1 % num2


# def sqrt(num1):
#     num1=int(num1)
#     return num1**0.5


# def square(num1):
#     num1=int(num1)
#     return num1**2


# def cube(num1):
#     num1=int(num1)
#     return num1**3


# def power(num1, num2):
#     num1,num2=int(num1),int(num2)
#     return num1**num2


# def compute():
#     choice = input("Enter your choice \n")

#     if(choice == "sqrt" or choice == "cube" or choice == "square"):
#         num1 = float(input("Enter first number \n"))
#         if(choice == "sqrt"):
#             print("{} {} = {} \n".format(num1, choice, sqrt(num1)))
#         if(choice == "cube"):
#             print("{} {} = {} \n".format(num1, choice, cube(num1)))
#         if(choice == "square"):
#             print("{} {} = {} \n".format(num1, choice, square(num1)))
#     else:
#         num1, num2 = float(input("Enter first number \n")), float(
#             input("Enter second number \n"))
#         if(choice == "+"):
#             print("{} {} {} = {} \n".format(
#                 num1, choice, num2, add(num1, num2)))
#         elif(choice == "-"):
#             print("{} {} {} = {} \n".format(
#                 num1, choice, num2, sub(num1, num2)))
#         elif(choice == "/"):
#             print("{} {} {} = {} \n".format(
#                 num1, choice, num2, div(num1, num2)))
#         elif(choice == "//"):
#             print("{} {} {} = {} \n".format(
#                 num1, choice, num2, floordiv(num1, num2)))
#         elif(choice == "%"):
#             print("{} {} {} = {} \n".format(
#                 num1, choice, num2, modulo(num1, num2)))
#         elif(choice == "*"):
#             print("{} {} {} = {} \n".format(
#                 num1, choice, num2, mul(num1, num2)))
#         elif(choice == "**"):
#             print("{} {} {} = {} \n".format(
#                 num1, choice, num2, power(num1, num2)))


# if __name__ == "main":
#     result = compute()
