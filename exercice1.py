# print("Choose a score between 0 and 100.")
# score = int(input())

# while score != 101:
#     if score >= 90 and score <= 100:
#         print("A")
#     elif score >= 80 and score <= 89:
#         print("B")
#     elif score >= 70 and score <= 79:
#         print("C")
#     elif score >= 60 and score <= 69:
#         print("D")
#     elif score < 60:
#         print("F")
#     print("Choose a score between 0 and 100. Choose 101 to exit.")
#     score = int(input())
#     if score == 101:
#             print("Goodbye :)")


# x = 1
# while x == 1:
#     print("First number")
#     fn = int(input())
#     print("Second number")
#     sn = int(input())
#     print("Opperation symbol : + - * /")
#     os = input()
#     if os == "+":
#         rs = fn + sn
#         print(f"Result : {fn} {os} {sn} = {rs}")
#     if os == "-":
#         rs = fn - sn
#         print(f"Result : {fn} {os} {sn} = {rs}")
#     if os == "*":
#         rs = fn * sn
#         print(f"Result : {fn} {os} {sn} = {rs}")
#     if os == "/":
#         rs = fn / sn
#         print(f"Result : {fn} {os} {sn} = {rs}")
#     elif os != "+" and "-" and "*" and "/":
#         print("Error : not a correct opperation symbol !")


# print("Write a year")
# year = input()

# if year 


print("Welcome to movie ticket chooser !")
print("Select your option : C (child), A (adult) or S (Senior).")
option1 = input()
print("Select your option : MTF (Monday to Friday), SAT (saturday) or SUN (sunday)")
option2 = input()

if option1 == C:
    price1 = 5
elif option1 == A:
    price1 = 10
elif option1 == S:
    price1 = 8
if option2 == MTF:
    price2 = 0
elif option2 == SAT:
    price2 = 2
elif option2 == SUN:
    price2 = 3
print(f"Your ticket price is {price1+price2}.")