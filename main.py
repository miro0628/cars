import car

looping = True
Bmw_svart = car.car("Bmw", "svart", 2)
Lada_blå = car.car("Lada", "blå", 2)
Bugatti_silver = car.car("Bugatti", "silver", 8)

carlist = [Bmw_svart, Lada_blå, Bugatti_silver]

print(Bmw_svart.getFabrikat())


while looping:
    i = 0

    for car in carlist:
        print(str(i+1) + "Fabrikat: "+ car.getFabrikat() + ", Color: " + car.getColor() )
        i += 1


    car_num = input("\noutput in carnum for selected car: ")
    print("\n One " + carlist[int(car_num)-1].Fabrikat + ", Color: " + carlist[int(car_num)-1].color)

    answer_user = input("\nDo you want to exit the program? y/n: ")

    if (answer_user == "y"):
        break