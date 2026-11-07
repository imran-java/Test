# Data lists for inputs
oxygen_list = []
animal_list = []
temp_list = []
hr_list = []
si_list = []
loc_list = []

# Dictionary storing 5 animal species with their normal ranges stored as tuples: 
# Format: (bt_min, bt_max, hr_min, hr_max)
species_ranges = {
    "Elephant": (35.5, 36.5, 25, 45),
    "Tiger": (37.5, 39.0, 60, 100),
    "Orangutan": (36.5, 37.5, 70, 120),
    "Sun Bear": (37.0, 38.5, 50, 90),
    "Malayan Tapir": (36.0, 38.0, 40, 70)
}

# make_line function is used to make sure output is limited to 74 characters.
def make_line(text):
    inner_width = 74
    return f"| {text:<{inner_width}} |"

# ui function for selection process and output display
def ui(animals_arg, bt, hr, si, loc, flagged_status):
    inner_width = 74
    border_line = "+" + "-" * (inner_width + 2) + "+"

    # Retrieve species-specific ranges from the tuple, with a fallback default if unknown
    bt_min, bt_max, hr_min, hr_max = species_ranges[animals_arg]
    # Logic to determine Body Temperature status using tuples and if-else
    if bt > bt_max:
        bt_status = "[! OVER HEATING]"
    elif bt < bt_min:
        bt_status = "[- LOW TEMP WARNING]"
    else:
        bt_status = "[+ NORMAL BODY TEMPERATURE]"

    # Logic to determine Heart Rate status using tuples and if-else
    if hr > hr_max:
        hr_status = "[! ELEVATED ]"
    elif hr < hr_min:
        hr_status = "[- LOW ]"
    else:
        hr_status = "[+ NORMAL]"

    # Stress Index status logic
    if si > 61:
        si_status = "[! HIGH PANIC ]"
    elif si > 30:
        si_status = "[~ MODERATE ]"
    else:
        si_status = "[+ CALM]"

    # Action determination based on flagged_status
    if flagged_status >= 3:
        action = "[ DISPATCH RESCUE TEAM ] [ SIMULATE HEATWAVE] [ MUTE ALARM ]"
    elif flagged_status == 2:
        action = "[ INCREASE GPS TRACK] [ ALERT RANGERS] [ MUTE ALARM ] "
    elif flagged_status == 1:
        action = "[ MONITOR CLOSELY ] [ CHECK SECTORS] [ MUTE ALARM ]"
    else:
        action = "[ ALL CLEAR ] [ ROUTINE CHECK ] [ MUTE ALARM ]"

    # Display layout
    print(border_line)
    print(make_line("                        BIOPULSE: WILDLIFE HEAT MONITOR"))
    print(border_line)
    print(make_line(f"Select Animal: [ {animals_arg} ]"))
    print(make_line(""))
    print(make_line("CURRENT VITALS (Live Stream):"))
    print(make_line(f"  • Body Temperature: {bt:<5}°C  {bt_status} (Range: {bt_min}-{bt_max}°C)"))
    print(make_line(f"  • Heart Rate:       {hr:<5} BPM {hr_status} (Range: {hr_min}-{hr_max} BPM)"))
    print(make_line(f"  • Stress Index:     {si:<5}%   {si_status}"))
    print(make_line(f"  • Location:         {loc}"))
    print(make_line(""))
    print(make_line("ACTIONS:"))
    print(make_line(f" {action}"))
    print(make_line(""))
    print(make_line("Location :"))
    print(make_line(" +---------------------------------------------------------------+"))
    print(make_line(f" | {loc:<61} |"))
    print(make_line(" +---------------------------------------------------------------+"))
    print(border_line + "\n")

# Welcome message
print("=" * 78)
print(make_line(f"Welcome to the Wildlife Heat Monitor System"))
print("-" * 78)
print(make_line(f"Supported Species: Elephant, Tiger, Orangutan, Sun Bear, Malayan Tapir"))
print(make_line(f"Please input the data (or type 'exit' to quit):"))
print("=" * 78)

# Input loop with error handling
while True:
    species = input("Enter Animal species: ").strip().title()

    if species.lower() == 'exit':
        break
    
    if species not in species_ranges:
        print("Species is not part of the monitoring program. (Tiger,Elephant,Orangutan,Sun Bear,Malayan Tapir)")
        continue

    try:
        bt = float(input("Enter Body Temperature (°C): "))
        if bt < 34 or bt > 42:
            raise ValueError("Body temperature is out of absolute safe range (34°C - 42°C).")

        hr = int(input("Enter Heart Rate (BPM): "))
        if hr < 20 or hr > 220:
            raise ValueError("Heart rate is out of absolute safe range (20 BPM - 220 BPM).")

        si = int(input("Enter Stress Index (%): "))
        if si < 0 or si > 100:
            raise ValueError("Stress index is out of normal range (0% - 100%).")

        loc = input("Enter Location: ").strip().upper()

        # Append valid inputs to lists
        animal_list.append(species)
        temp_list.append(bt)
        hr_list.append(hr)
        si_list.append(si)
        loc_list.append(loc)
        print("Data recorded successfully!\n")

    except ValueError as e:
        print(f"Error: {e}\nPlease try entering the data for this animal again.\n")

# Process and display summary reports for each recorded animal
print("\n" + "=" * 78)
print(make_line("                   KOGENERATING WILDLIFE MONITORING REPORTS..."))
print("=" * 78 + "\n")

for i in range(len(animal_list)):  
    current_animal = animal_list[i]
    bt = temp_list[i]
    hr = hr_list[i]
    si = si_list[i]
    
    # Fetch tuples for the current species
    if current_animal in species_ranges:
        bt_min, bt_max, hr_min, hr_max = species_ranges[current_animal]
    else:
        bt_min, bt_max, hr_min, hr_max = (36.0, 38.0, 60, 100)

    # Calculate flagged status based on species-specific ranges and if-else checks
    flagged_status = 0
    if bt > bt_max or bt < bt_min:
        flagged_status += 1
    if hr > hr_max or hr < hr_min:
        flagged_status += 1
    if si > 61:
        flagged_status += 2
    elif si > 30:
        flagged_status += 1

    # Call the UI display function
    ui(current_animal, bt, hr, si, loc_list[i], flagged_status)