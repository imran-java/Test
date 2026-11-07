count = 0
total_disc = 0
total_sale = 0

print("=== PRINTSAVER CLUB PRINTING SYSTEM ===")
customer_1 = input("Enter customer name: ")
quantity_1 = int(input("Enter number of pages: "))
distance_1 = float(input("Enter delivery distance (km) : "))
status_1 = input("Are you a PrintSaverr Club member? (Y/N): ").upper()

if quantity_1 > 0 and quantity_1 <= 50:
    pr_cost1 = quantity_1 * 0.2
elif quantity_1 >= 51 and quantity_1 <= 100:
    pr_cost1 = quantity_1 * 0.15
elif quantity_1 > 100: 
    pr_cost1 = quantity_1 * 0.1

if distance_1 == 0:
    delivery_fee1 = 0
elif distance_1 > 0 and distance_1 <= 5:
    delivery_fee1 = 3
elif distance_1 > 5 and distance_1 <= 10:
    delivery_fee1 = 5
elif distance_1 > 10:
    delivery_fee1 = 8

if status_1 == "Y":
    discount_1 = pr_cost1 * 0.1
    if pr_cost1 >= 50:
        delivery_fee1 = 0
elif status_1 == "N":
    discount_1 = 0

final_price1 = pr_cost1 - discount_1 + delivery_fee1

print(f"\nCustomer: {customer_1}")
print(f"Printing Price: RM {pr_cost1:.2f}")
print(f"Discount: RM {discount_1:.2f}")
print(f"Delivery Fee: RM {delivery_fee1:.2f}")
print(f"Final Price: RM {final_price1:.2f}")

count +=1
total_disc += discount_1
total_sale += final_price1

proceed = input("\nAnymore order (Yes or No)?: ").title()

if proceed == "Yes":
    customer_2 = input("\nEnter customer name: ")
    quantity_2 = int(input("Enter number of pages: "))
    distance_2 = float(input("Enter delivery distance (km) : "))
    status_2 = input("Are you a PrintSaver Club member? (Y/N): ").upper()

    if quantity_2 > 0 and quantity_2 <= 50:
        pr_cost2 = quantity_2 * 0.2
    elif quantity_2 >= 51 and quantity_2 <= 100:
        pr_cost2 = quantity_2 * 0.15
    elif quantity_2 > 100: 
        pr_cost2 = quantity_2 * 0.1

    if distance_2 == 0:
        delivery_fee2 = 0
    elif distance_2 > 0 and distance_2 <= 5:
        delivery_fee2 = 3
    elif distance_2 > 5 and distance_2 <= 10:
        delivery_fee2 = 5
    elif distance_2 > 10:
        delivery_fee2 = 8

    if status_2 == "Y":
        discount_2 = pr_cost2 * 0.1
        if pr_cost2 >= 50:
            delivery_fee2 = 0

    elif status_2 == "N":
            discount_2 = 0
    final_price2 = pr_cost2 - discount_2 + delivery_fee2

    print(f"\nCustomer: {customer_2}")
    print(f"Printing Price: RM {pr_cost2:.2f}")
    print(f"Discount: RM {discount_2:.2f}")
    print(f"Delivery Fee: RM {delivery_fee2:.2f}")
    print(f"Final Price: RM {final_price2:.2f}")

    count +=1
    total_disc += discount_2
    total_sale += final_price2

print("\n=== COLLECTION SUMMARY ===")
print(f"Total customers: {count}")
print(f"Total Discount: RM {total_disc:.2f}")
print(f"Total Collected: RM {total_sale:.2f}")


