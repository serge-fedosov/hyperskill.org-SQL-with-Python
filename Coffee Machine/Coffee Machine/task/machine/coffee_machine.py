need_water = 200
need_milk = 50
need_coffee_beans = 15

print("Write how many ml of water the coffee machine has:")
has_water = int(input())

print("Write how many ml of milk the coffee machine has:")
has_milk = int(input())

print("Write how many grams of coffee beans the coffee machine has:")
has_coffee_beans = int(input())

print("Write how many cups of coffee you will need:")
need_cups_coffee = int(input())
can_make = min(has_water // need_water, has_milk // need_milk, has_coffee_beans // need_coffee_beans)

if need_cups_coffee == can_make:
    print("Yes, I can make that amount of coffee")
elif need_cups_coffee < can_make:
    print(f"Yes, I can make that amount of coffee (and even {can_make - need_cups_coffee} more than that)")
else:
    print(f"No, I can make only {can_make} cups of coffee")
