def cool_gel(body_temp,bt_max ):
    if body_temp > bt_max:
        return("Releasing cool gel")

def stress_status(stress_index):
    if stress_index > 70:
        return("[! HIGH PANIC ]")
    elif stress_index > 40:
        return("[~ MODERATE ]")
    else:
        return("[+ CALM]")


try:
    location = input("Enter animal's location: ")
    stress_index = float(input("Enter animal's stress index: "))
    if stress_index < 0 or stress_index > 100:
        raise ValueError("Stress index must be in range of 0 to 100 ")
except ValueError as e:
    print(f"{e}\n Please enter valid inputs" )

stress_status(stress_index)