import math 
from datetime import datetime

current_date_and_time = datetime.now()

disc_rate = 0.10
tax_rate = 0.06

name = input("Enter your name: ")
print(f"welcome {name}")
width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
subtotal = float(input("Enter the subtotal: "))



#calculation

gamma = (width * ratio + 2540 * diameter)
volume = math.pi * width**2 * ratio * gamma // 10000000000

print(f"the volume is  {volume} cubic meter")


with open("volumes.txt", "at") as volume_file:
    print(f"{current_date_and_time:%Y-%m-%d}", file=volume_file)
#volume = math.pi * width**2 * ratio * gamma // 10000000000
#print (f"{current_date_and_time:%Y-%m-%d} {width: .2f}mm {ratio: .2f} {diameter: .2f}inches {volume: .2f}cubic meter ")

weekday = current_date_and_time.weekday()
if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * disc_rate, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount     

sales_tax = round(subtotal * tax_rate, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax

print(f"Total: {total:.2f}")