def ui(name,count,bc,bcp,bp,pc,pcp,pp,pw,cc,ccp,cp,cq,sc,scp,sp,sq,buc,bup,gc,gp):
    inner_width = 74
    def line(text):
        return (f"| {text:<{inner_width}} |")
   
    border_line = "=" * 78
    normal_line = "-" * 78

    print (border_line)
    print(line("                FOODSQUAT BURGER NUTRITION AND COST "))
    print(border_line)
    print(line(f"Customer Name:             {name} "))
    print(line(f"Quantity of Burgers:       {count} Burger(s) "))
    print(normal_line)
    print(line("CALORIES & COST BREAKDOWN (per burger)"))
    print(line(f" - Bun Base: {bc:.2f} kcal ({bcp:.2f}%)     | RM {bp:.2f}"))
    print(line(f" - Beef Patty: {pc:.2f} kcal ({pcp:.2f}%)   | RM {pp:.2f} ({pw:.1f}g)"))
    print(line(f" - Cheese Slice: {cc:.2f} kcal ({ccp:.2f}%) | RM {cp:.2f} ({cq} slice/s)"))
    print(line(f" - Extra Sauce: {sc:.2f} kcal ({scp:.2f}%)  | RM {sp:.2f} ({sq:.1f} tbsp)"))
    print(normal_line)
    print(line(f"TOTAL EACH BURGER : {buc:.2f} kcal | RM {bup:.2f}"))
    print(normal_line)
    print(line(f"GRAND TOTAL CALORIES: {gc:.2f} kcal"))
    print(line(f"TOTAL MENU COST: | RM {gp:.2f}"))
    print(border_line)
    print(line(" Eat Wisely for Healthy Living!"))
    print (border_line)

name = str(input("Enter customer name: "))
count = int(input("How many burgers are you ordering ? "))
patty_weight = float(input("Enter weight of patty per burger (in grams): "))
cheese_quant = int(input("Enter number of cheese slices per burger: "))
sauce_quant = int(input("Enter tablespoon of sauce per burger: "))
bun_cal = 150
patty_cal = 2.5 * patty_weight
cheese_cal = 70 * cheese_quant
sauce_cal = 60 * sauce_quant
bun_price = 2
patty_price = 0.04 * patty_weight
cheese_price = 1 * cheese_quant
sauce_price = 0.5 * sauce_quant
burger_cal = bun_cal + patty_cal + cheese_cal + sauce_cal
grand_cal = burger_cal * count
burger_price = bun_price + patty_price + cheese_price + sauce_price
grand_price = burger_price * count
bun_cal_percent = (bun_cal / burger_cal) * 100
patty_cal_perecent =(patty_cal / burger_cal) * 100
cheese_cal_percent = (cheese_cal / burger_cal) * 100
sauce_cal_percent = (sauce_cal / burger_cal) * 100

ui(name,count,bun_cal,bun_cal_percent,bun_price,patty_cal,patty_cal_perecent,patty_price,patty_weight,cheese_cal,cheese_cal_percent,cheese_price,cheese_quant,sauce_cal,sauce_cal_percent,sauce_price,sauce_quant,burger_cal,burger_price,grand_cal,grand_price)