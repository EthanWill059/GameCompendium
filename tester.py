racedistance = 15

cars = {"car1": 0, "car2": 0, "car3": 0, "car4": 0, "car5": 0, "car6": 0} # record distance the cars have traveled

for i in range(1,7): # set  the distances for the dictionary
    cars["car{}".format(i)] = racedistance # doing what it saysabove

print(cars)

cars["car1"] -= 1

print(cars)