password = "1234"
limit = 1000
user_password = input("Enter your password: ")


if user_password != password:
    for i in range (2):
        user_password = input("Invalid password. Please try again \nEnter your password: ") 
        if user_password == password:
            balance = float(input("Enter your balance: "))                      
            withdraw = float(input("Enter withdrawal amout:"))
            if withdraw <= balance and withdraw <= limit:
                print( "Withdrawal successful")
            elif withdraw > balance:
                print("Insufficient balance") 
            elif withdraw > limit:
                print("Daily limti exceed")
        else:
            continue
    else:
        print("Too many attempt. Account blocked")
else:
    balance = float(input("Enter your balance: "))                      
    withdraw = float(input("Enter withdrawal amout:"))
    if withdraw <= balance and withdraw <= limit:
        print( "Withdrawal successful")
    elif withdraw > balance:
        print("Insufficient balance") 
    elif withdraw > limit:
        print("Daily limti exceed")


            
    

