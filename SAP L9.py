temp = float(input("Please enter temperature in cdegree Celsius: "))

if temp < 0 :
    print("It's freezinf!")
elif temp > 0 and temp < 15:
    print ("It's cold!")
elif temp >=15  and temp < 25:
    print ("It's warm!")
elif temp >= 25 and temp <35:
    print ("It's hot!")
elif temp >35:
    print("")
    if temp > 40:
     print ("Heatwave alert!")
    else: 
      print ("Stay hydrated!")