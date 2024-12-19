# def main():
#     # Constants
#     PRICE_PER_PACKAGE = 99
#
#     # Input: Number of packages purchased
#     num_packages = int(input("Enter the number of packages purchased: "))
#
#     # Determine discount percentage based on quantity
#     if 10 <= num_packages <= 19:
#         discount_rate = 0.2
#     elif 20 <= num_packages <= 49:
#         discount_rate = 0.3
#     elif 50 <= num_packages <= 99:
#         discount_rate = 0.4
#     elif num_packages >= 100:
#         discount_rate = 0.5
#     else:
#         discount_rate = 0.0
#
#     # Calculations
#     total_before_discount = num_packages * PRICE_PER_PACKAGE
#     discount_amount = total_before_discount * discount_rate
#     total_after_discount = total_before_discount - discount_amount
#
#     # Output results
#     print(f"Discount Amount: ${discount_amount:.2f}")
#     print(f"Total Amount after Discount: ${total_after_discount:.2f}")
#
# # Run the program
# main()
#
#
# def main():
#
#     PRICE_PER_PACKAGE = 99
#
#     num_packages = int(input("Enter the number of packages purchased: "))
#
#     if 10 <= num_packages <= 19:
#         discount_rate = 0.2
#     elif 20 <= num_packages <= 49:
#         discount_rate = 0.3
#     elif 50 <= num_packages <= 99:
#         discount_rate = 0.4
#     elif num_packages >= 100:
#         discount_rate = 0.5
#     else:
#         discount_rate = 0.0
#
#     total_before_discount = num_packages * PRICE_PER_PACKAGE
#     discount_amount = total_before_discount * discount_rate
#     total_after_discount = total_before_discount - discount_amount
#
#     print(discount_amount)
#     print(total_after_discount)
# main()
#
# def main():
#     weight = float(input("Enter your weight in pounds: "))
#     height = float(input("Enter your height in inches: "))
#
#     bmi = (weight * 703) / (height ** 2)
#
#
#     if bmi < 18.5:
#         status = "Underweight"
#     elif 18.5 <= bmi <= 25:
#         status = "Optimal weight"
#     else:
#         status = "Overweight"
#
#
#     print(f"Your BMI is: {bmi:.2f}")
#     print(f"Weight Status: {status}")
#
#
# main()
#
#
# def main():
#     weight = float(input("Enter the weight of the package (in pounds): "))
#
#     if weight <= 2:
#         rate = 1.10
#     elif weight <= 6:
#         rate = 2.20
#     elif weight <= 10:
#         rate = 3.70
#     else:
#         rate = 3.80
#
#     shipping_charge = weight * rate
#
#     print(f"Shipping Charge: ${shipping_charge:.2f}")
#
# main()
#
#
# def main():
#     books_purchased = int(input("Enter the number of books purchased this month: "))
#
#     if books_purchased == 0:
#         points = 0
#     elif books_purchased == 1:
#         points = 5
#     elif books_purchased == 2:
#         points = 15
#     elif books_purchased == 3:
#         points = 30
#     else:
#         points = 60
#
#     print(f"Points awarded: {points}")
#
# main()
# import turtle
#
# def draw_circle(turtle, color, size, x ,y):
#     turtle.color(color)
#     for i in range(8):
#         turtle.forward(50)
#         turtle.right(45)
#     turtle.done
#
#
# tommy = turtle.Turtle()
# tommy.shape("turtle")
# tommy.speed(500)
#
# draw_circle(tommy, "red", 50, 20, 0)

def main():
    num_days = int(input("Enter the number of days worked: "))

    daily_salary = 0.01
    total_pay = 0.0

    print("\nDay\tSalary (in $)")
    print("------------------------")

    for day in range(1, num_days + 1):
        print(f"{day}\t${daily_salary:.2f}")
        total_pay += daily_salary
        daily_salary *= 2

    print("------------------------")
    print(f"Total Pay: ${total_pay:.2f}")

main()
