month = input ("Please enter current month:").lower()
if month == "February":
  year = int(input ("Press 1 if it's a leap year or 0 for non leap year "))
  if year == 1:
    days = 3
  elif year == 0:
    days =2
elif month == "april" or "jun" or "september" or "november":
   days = 4
elif month == "january" or "march" or "mei" or "july" or "august" or "oktober" or "december":
  days = 5
else :
  print("Invalid month. Please check your spelling !")


api_list = []


for i in range(days):
  API = int(input(f"Please enter air pollution index for day {i + 1}: "))
  if API > 301:
    status = ("PRABOWOOOOOO")
    api_list.append(status)
  elif API >= 201 and API <= 300:
    status = ("Very Unhealthy ")
    api_list.append(status)
  elif API >= 101 and API <= 200:
    status = ("Unhealthy")
    api_list.append(status)
  elif API >= 51 and API <=100:
    status = ("Moderate ")
    api_list.append(status)
  elif API <= 50:
    status = ("Good ")
    api_list.append(status)

for i in range (days):
  print (f"Day API status {i +1} is {api_list [i]}")